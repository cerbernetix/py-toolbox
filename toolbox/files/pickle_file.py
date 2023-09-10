"""
Defines a class for reading and writing pickle files.
"""
from __future__ import annotations

import pickle
from typing import Iterable

from toolbox.files.file_manager import FileManager

# The parameters that will be forwarded to the pickle reader
PICKLE_READER_PARAMS = [
    "fix_imports",
    "encoding",
    "errors",
    "buffers",
]

# The parameters that will be forwarded to the pickle writer
PICKLE_WRITER_PARAMS = [
    "protocol",
    "fix_imports",
    "buffer_callback",
]

# The parameters that will be forwarded to the file opener
FILE_OPEN_PARAMS = ["buffering", "errors", "closefd", "opener"]


class PickleFile(FileManager):
    """
    Defines a class for reading and writing pickle files.
    """

    def __init__(
        self,
        filename: str,
        create: bool = False,
        append: bool = False,
        read: bool = False,
        write: bool = False,
        **kwargs,
    ):
        """
        Creates a file manager for pickle files.

        Args:
            - filename (str): The path to the file to manage.
            - create (bool, optional): Expect to create the file. If it exists, it will be replaced.
            Defaults to False.
            - append (bool, optional): Expect to extend the file. Data will be added at the end.
            Defaults to False.
            - read (bool, optional): Expect to also read the file.
            Defaults to False.
            - write (bool, optional): Expect to also write to the file.
            Defaults to False.
            - protocol (int, optional): Tells the pickle writer to use the given protocol; supported
            protocols are 0 to HIGHEST_PROTOCOL. If a negative number is specified, HIGHEST_PROTOCOL
            is selected. When reading, the protocol version of the pickle is detected automatically.
            Defaults is DEFAULT_PROTOCOL.
            - fix_imports (bool, optional): If fix_imports is true and protocol is less than 3,
            pickle will try to map the new Python 3 names to the old module names used in Python 2,
            so that the pickle data stream is readable with Python 2. Defaults to True.
            - encoding (str, optional): Tell pickle how to decode 8-bit string instances pickled by
            Python 2. The encoding can be ‘bytes’ to read these 8-bit string instances as bytes objects.
            Using encoding='latin1' is required for unpickling NumPy arrays and instances of datetime,
            date and time pickled by Python 2. Defaults to ‘ASCII’.
            - errors (str, optional): Tell pickle how to decode 8-bit string instances pickled by
            Python 2. Defaults to ‘strict’.
            - buffers (optional): If buffers is None (the default), then all data necessary for
            deserialization must be contained in the pickle stream. This means that the buffer_callback
            argument was None when a Pickler was instantiated (or when dump() or dumps() was called). If
            buffers is not None, it should be an iterable of buffer-enabled objects that is consumed
            each time the pickle stream references an out-of-band buffer view. Such buffers have been
            given in order to the buffer_callback of a Pickler object.
            - buffer_callback (optional): If buffer_callback is None (the default), buffer views are
            serialized into file as part of the pickle stream. If buffer_callback is not None, then
            it can be called any number of times with a buffer view. If the callback returns a false
            value (such as None), the given buffer is out-of-band; otherwise the buffer is
            serialized in-band, i.e. inside the pickle stream. It is an error if buffer_callback is
            not None and protocol is None or smaller than 5. Defaults to None.
        """
        super().__init__(
            filename,
            binary=True,
            create=create,
            append=append,
            read=read,
            write=write,
            encoding=None,
            **{key: value for key, value in kwargs.items() if key in FILE_OPEN_PARAMS},
        )
        self._reader_args = {
            key: value for key, value in kwargs.items() if key in PICKLE_READER_PARAMS
        }
        self._writer_args = {
            key: value for key, value in kwargs.items() if key in PICKLE_WRITER_PARAMS
        }

    def read_file(self) -> list:
        """
        Reads all the content from the file.

        Note: If the file was already opened, it is first closed, then opened in read mode.

        Raises:
            OSError: If the file cannot be read.
            FileNotFoundError: If the file does not exist.

        Returns:
            list: The content read from the file.
        """
        return list(self)

    def write_file(self, data: Iterable) -> int:
        """
        Writes whole content to the file.

        Note: If the file was already opened, it is first closed, then opened in write mode.

        Args:
            - data (Iterable): The content to write to the file.

        Raises:
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.
        """
        size = 0
        with self.open(create=True):
            for row in data:
                size += self.write(row)

        return size

    def read(self) -> object:
        """
        Reads the next object from the file.

        Note: the file must be opened upfront.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be read.

        Returns:
            object: The object loaded from the file, or None if the file is at EOF.
        """
        if self._file is None:
            raise ValueError("The file must be opened before reading from it!")

        try:
            return pickle.load(self._file, **self._reader_args)
        except EOFError:
            return None

    def write(self, data: object) -> int:
        """
        Writes an object to the file.

        Note: the file must be opened upfront.

        Args:
            - data (object): The object to write to the file.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.
        """
        if self._file is None:
            raise ValueError("The file must be opened before writing to it!")

        return self._file.write(pickle.dumps(data, **self._writer_args))


def read_pickle_file(filename: str, **kwargs) -> list:
    """
    Loads a list of objects from a file.

    Args:
        - filename (str): The path to the file to read.
        - fix_imports (bool, optional): If fix_imports is true and protocol is less than 3,
        pickle will try to map the new Python 3 names to the old module names used in Python 2,
        so that the pickle data stream is readable with Python 2. Defaults to True.
        - encoding (str, optional): Tell pickle how to decode 8-bit string instances pickled by
        Python 2. The encoding can be ‘bytes’ to read these 8-bit string instances as bytes objects.
        Using encoding='latin1' is required for unpickling NumPy arrays and instances of datetime,
        date and time pickled by Python 2. Defaults to ‘ASCII’.
        - errors (str, optional): Tell pickle how to decode 8-bit string instances pickled by
        Python 2. Defaults to ‘strict’.
        - buffers (optional): If buffers is None (the default), then all data necessary for
        deserialization must be contained in the pickle stream. This means that the buffer_callback
        argument was None when a Pickler was instantiated (or when dump() or dumps() was called). If
        buffers is not None, it should be an iterable of buffer-enabled objects that is consumed
        each time the pickle stream references an out-of-band buffer view. Such buffers have been
        given in order to the buffer_callback of a Pickler object.

    Raises:
        OSError: If the file cannot be read.
        FileNotFoundError: If the file does not exist.

    Returns:
        list: The list of objects read from the file.
    """
    return PickleFile(
        filename,
        **kwargs,
    ).read_file()


def write_pickle_file(filename: str, data: Iterable, **kwargs) -> int:
    """
    Writes a list of objects to a file.

    Args:
        - filename (str): The path to the file to write.
        - data (Iterable): The list of objects to write to the file.
        - protocol (int, optional): Tells the pickle writer to use the given protocol; supported
        protocols are 0 to HIGHEST_PROTOCOL. If a negative number is specified, HIGHEST_PROTOCOL
        is selected. Defaults is DEFAULT_PROTOCOL.
        - fix_imports (bool, optional): If fix_imports is true and protocol is less than 3,
        pickle will try to map the new Python 3 names to the old module names used in Python 2,
        so that the pickle data stream is readable with Python 2. Defaults to True.
        - buffer_callback (optional): If buffer_callback is None (the default), buffer views are
        serialized into file as part of the pickle stream. If buffer_callback is not None, then
        it can be called any number of times with a buffer view. If the callback returns a false
        value (such as None), the given buffer is out-of-band; otherwise the buffer is
        serialized in-band, i.e. inside the pickle stream. It is an error if buffer_callback is
        not None and protocol is None or smaller than 5. Defaults to None.

    Raises:
        OSError: If the file cannot be written.

    Returns:
        int: The number of bytes written to the file.
    """
    return PickleFile(
        filename,
        **kwargs,
    ).write_file(data)
