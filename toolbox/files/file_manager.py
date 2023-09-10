"""
A simple class for reading and writing files.
"""
from __future__ import annotations

from typing import Iterator

from toolbox.files.file import get_file_mode


class FileManager:
    """
    Offers a simple API for reading and writing files.

    The class binds a filename with a set of properties so that it can be opened in a consistent
    way.

    The read API does not allow to size the data to read. The FileManager reads all the content.
    However, it comes better with the specialized child classes, which can read chunks of the file
    based on a specific format. See CSVFile, JSONFile, or PickleFile for more information.

    Attributes:
        filename (str): The path to the file to manage.
        binary (bool): The type of file: binary (True) or text (False).
        encoding (str, optional): The file encoding, only needed for text files.

    Examples:
    ```
    file = FileManager("path/to/the/file", binary=False, encoding="UTF-8")

    # open the file, then read its content
    with file:
        content = file.read()

    # write data to the file
    with file(create=True):
        for chunk in data:
            file.write(chunk)

    # load the whole file, handling internally its opening
    content = file.read_file()
    ```
    """

    def __init__(
        self,
        filename: str,
        binary: bool = False,
        create: bool = False,
        append: bool = False,
        read: bool = False,
        write: bool = False,
        encoding: str = None,
        **kwargs,
    ):
        """
        Creates a file manager.

        Args:
            filename (str): The path to the file to manage.
            binary (bool, optional): The type of file: binary (True) or text (False).
            Defaults to False.
            create (bool, optional): Expect to create the file. If it exists, it will be replaced.
            Defaults to False.
            append (bool, optional): Expect to extend the file. Data will be added at the end.
            Defaults to False.
            read (bool, optional): Expect to also read the file.
            Defaults to False.
            write (bool, optional): Expect to also write to the file.
            Defaults to False.
            encoding (str, optional): The file encoding, only needed for text files.
            Defaults to None.
        """
        self.filename = filename
        self.binary = binary
        self.encoding = encoding if not binary else None
        self._file = None
        self._open_args = kwargs

        if create or append or read or write:
            self.open(create, append, read, write)

    def open(
        self,
        create: bool = False,
        append: bool = False,
        read: bool = False,
        write: bool = False,
    ) -> FileManager:
        """
        Opens the file for access.

        Note: If the file was already opened, it is first closed.

        Args:
            create (bool, optional): Expect to create the file. If it exists, it will be replaced.
            Defaults to False.
            append (bool, optional): Expect to extend the file. Data will be added at the end.
            Defaults to False.
            read (bool, optional): Expect to also read the file.
            Defaults to False.
            write (bool, optional): Expect to also write to the file.
            Defaults to False.

        Returns:
            FileManager: Chains the instance.
        """
        self.close()

        self._file = open(
            self.filename,
            mode=get_file_mode(create, append, read, write, self.binary),
            encoding=self.encoding,
            **self._open_args,
        )

        return self

    def close(self) -> FileManager:
        """
        Closes the file.

        Note: it does nothing if the file is already closed.

        Returns:
            FileManager: Chains the instance.
        """
        if self._file is not None:
            self._file.close()

        self._file = None

        return self

    def read_file(self) -> str | bytes:
        """
        Reads all the content from the file.

        Note: If the file was already opened, it is first closed, then opened in read mode.

        Raises:
            OSError: If the file cannot be read.
            FileNotFoundError: If the file does not exist.

        Returns:
            str|bytes: The content read from the file.
        """
        with self.open():
            return self.read()

    def write_file(self, data: str | bytes) -> int:
        """
        Writes whole content to the file.

        Note: If the file was already opened, it is first closed, then opened in write mode.

        Args:
            data (str|bytes): The content to write to the file.

        Raises:
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.
        """
        with self.open(create=True):
            return self.write(data)

    def read(self) -> str | bytes:
        """
        Reads the next content from the file.

        Note: the file must be opened upfront.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be read.

        Returns:
            str|bytes: The content loaded from the file, or None if the file is at EOF.
        """
        if self._file is None:
            raise ValueError("The file must be opened before reading from it!")

        return self._file.read() or None

    def write(self, data: str | bytes) -> int:
        """
        Writes content to the file.

        Note: the file must be opened upfront.

        Args:
            data (str|bytes): The content to write to the file.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.
        """
        if self._file is None:
            raise ValueError("The file must be opened before writing to it!")

        return self._file.write(data)

    def __call__(
        self,
        create: bool = False,
        append: bool = False,
        read: bool = False,
        write: bool = False,
    ) -> FileManager:
        """
        Opens the file for access.

        Note: If the file was already opened, it is first closed.

        Args:
            create (bool, optional): Expect to create the file. If it exists, it will be replaced.
            Defaults to False.
            append (bool, optional): Expect to extend the file. Data will be added at the end.
            Defaults to False.
            read (bool, optional): Expect to also read the file.
            Defaults to False.
            write (bool, optional): Expect to also write to the file.
            Defaults to False.

        Returns:
            FileManager: Chains the instance.
        """
        return self.open(create, append, read, write)

    def __enter__(self) -> FileManager:
        """
        Opens the context for accessing the file.

        Note: it does nothing if the file is already open.

        Returns:
            FileManager: Chains the instance.
        """
        if self._file is None:
            self.open()

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        """
        Closes the context for accessing the file.

        Note: it does nothing if the file is already closed.

        Returns:
            bool: If the return value is `True`, Python will make any exception silent.
            Otherwise, it doesn’t silence the exception.
        """
        self.close()

        # Do not silent the exceptions, if any
        return False

    def __iter__(self) -> Iterator:
        """
        Turns the FileManager into an iterator for reading the file chunk by chunk.

        Note: If the file was already opened, it is first closed, then opened in read mode.

        Raises:
            OSError: If the file cannot be read.
            FileNotFoundError: If the file does not exist.

        Yields:
            Iterator: Starts the iteration protocol.
        """
        return self.open()

    def __next__(self) -> str | bytes:
        """
        Gets the next chunk from the file.

        Note: the file must be opened upfront.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be read.
            StopIteration: Stops the iteration if there is no more data.

        Returns:
            str | bytes: The chunk of data read from the file.
        """
        data = self.read()

        if data is None:
            self.close()
            raise StopIteration

        return data
