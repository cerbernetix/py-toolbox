"""A simple class for reading and writing files.

Examples:
```python
from toolbox.files import FileManager

filename = 'path/to/file.txt'
data = "Some content"

# Manage a text file
file = FileManager(filename, encoding='UTF-8')

# Create the file
file.write_file(data)

# It can also be done using the open/write API
with file.open(create=True):
    file.write(data)

# Show the file
print(file.read_file(filename))

# It can also be done using the open/read API
with file:
    print(file.read())
```
"""
from __future__ import annotations

import os
from typing import Iterator

from toolbox.files.file import get_file_mode


class FileManager:
    """Offers a simple API for reading and writing files.

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
    ```python
    from toolbox.files import FileManager

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
        """Creates a file manager.

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

        Examples:
        ```python
        from toolbox.files import FileManager

        # Create a file manager
        file = FileManager('path/to/filename')

        # File can be opened directly as the manager is created
        with FileManager('path/to/filename') as file:
            data = file.read()

        with FileManager('path/to/filename', create=True) as file:
            file.write(data)
        ```
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
        """Opens the file for access.

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

        Examples:
        ```python
        from toolbox.files import FileManager

        file = FileManager('path/to/filename')

        # A file manager can open explicitly a file
        with file.open():
            data = file.read()

        with file.open(create=True):
            file.write(data)

        # It can also be opened implicitly
        with file:
            data = file.read()

        # To create the file while opening implicitly
        with file(create=True):
            file.write(data)

        # The file is also (re)opened when using the iteration protocol
        data = [dat for dat in file]
        ```
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
        """Closes the file.

        Note: it does nothing if the file is already closed.

        Returns:
            FileManager: Chains the instance.

        Examples:
        ```python
        from toolbox.files import FileManager

        file = FileManager('path/to/filename')

        # A file is closed implicitly when using the context manager
        with file:
            data = file.read()

        # However, open/close can be explicitly called
        file.open(create=True)
        file.write(data)
        file.close()
        ```
        """
        if self._file is not None:
            self._file.close()

        self._file = None

        return self

    def read_file(self) -> str | bytes:
        """Reads all the content from the file.

        Note: If the file was already opened, it is first closed, then opened in read mode.

        Raises:
            OSError: If the file cannot be read.
            FileNotFoundError: If the file does not exist.

        Returns:
            str|bytes: The content read from the file.

        Examples:
        ```python
        from toolbox.files import FileManager

        file = FileManager('path/to/filename')

        # A file can be read all at once
        data = file.read_file()
        ```
        """
        with self.open():
            return self.read()

    def write_file(self, data: str | bytes) -> int:
        """Writes whole content to the file.

        Note: If the file was already opened, it is first closed, then opened in write mode.

        Args:
            data (str|bytes): The content to write to the file.

        Raises:
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.

        Examples:
        ```python
        from toolbox.files import FileManager

        file = FileManager('path/to/filename')

        # A file can be written all at once
        file.write_file(data)
        ```
        """
        with self.open(create=True):
            return self.write(data)

    def read(self) -> str | bytes:
        """Reads the next content from the file.

        Note: the file must be opened upfront.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be read.

        Returns:
            str|bytes: The content loaded from the file, or None if the file is at EOF.

        Examples:
        ```python
        from toolbox.files import FileManager

        file = FileManager('path/to/filename')

        # When calling the read API, the next chunk in the file is read.
        # With the base class, all the content is read.
        with file:
            data = file.read()
        ```
        """
        if self._file is None:
            raise ValueError("The file must be opened before reading from it!")

        return self._file.read() or None

    def write(self, data: str | bytes) -> int:
        """Writes content to the file.

        Note: the file must be opened upfront.

        Args:
            data (str|bytes): The content to write to the file.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.

        Examples:
        ```python
        from toolbox.files import FileManager

        file = FileManager('path/to/filename')

        # When calling the write API, a chunk of data is written to the file.
        with file(create=True):
            file.write(data)
        ```
        """
        if self._file is None:
            raise ValueError("The file must be opened before writing to it!")

        return self._file.write(data)

    def exists(self) -> bool:
        """Tells if the file already exists.

        Returns:
            bool: Returns True if the file exists, False otherwise.

        Examples:
        ```python
        from toolbox.files import FileManager

        file = FileManager('path/to/filename')

        # Read only if the file exists
        if file.exists():
            with file:
                data = file.read()
        ```
        """
        return os.path.exists(self.filename)

    def delete(self, must_exist: bool = False) -> bool:
        """Deletes the file.

        Args:
            must_exist (bool, optional): Deletes the file only if it exists. Defaults to False.

        Returns:
            bool: Returns True if the file has been deleted, False otherwise.

        Examples:
        ```python
        from toolbox.files import FileManager

        file = FileManager('path/to/filename')

        # Delete if the file exists
        file.delete(True)

        # Delete the file anyway, will raise an error if the file does not exist
        file.delete()
        ```
        """
        if must_exist and not self.exists():
            return False

        os.remove(self.filename)

        return True

    def __call__(
        self,
        create: bool = False,
        append: bool = False,
        read: bool = False,
        write: bool = False,
    ) -> FileManager:
        """Opens the file for access.

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
        """Opens the context for accessing the file.

        Note: it does nothing if the file is already open.

        Returns:
            FileManager: Chains the instance.
        """
        if self._file is None:
            self.open()

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        """Closes the context for accessing the file.

        Note: it does nothing if the file is already closed.

        Returns:
            bool: If the return value is `True`, Python will make any exception silent.
            Otherwise, it doesn’t silence the exception.
        """
        self.close()

        # Do not silent the exceptions, if any
        return False

    def __iter__(self) -> Iterator:
        """Turns the FileManager into an iterator for reading the file chunk by chunk.

        Note: If the file was already opened, it is first closed, then opened in read mode.

        Raises:
            OSError: If the file cannot be read.
            FileNotFoundError: If the file does not exist.

        Yields:
            Iterator: Starts the iteration protocol.
        """
        return self.open()

    def __next__(self) -> str | bytes:
        """Gets the next chunk from the file.

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
