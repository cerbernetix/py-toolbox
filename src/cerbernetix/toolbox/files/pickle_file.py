"""A simple API for reading and writing pickle files.

Examples:
```python
from cerbernetix.toolbox.files import PickleFile, read_pickle_file, write_pickle_file

filename = 'path/to/file.pkl'
data = [
    {'date': '2023-09-10', 'value': 42},
    {'date': '2023-09-11', 'value': 24},
    {'date': '2023-09-12', 'value': 44},
]

# Create a Pickle file from the given data
write_pickle_file(filename, data)

# Read the Pickle data from an existing file
data = read_pickle_file(filename)

# Use a file manager
pickle = PickleFile(filename)

# Create a Pickle file from the given data
pickle.write_file(data)

# Read the Pickle data from an existing file
data = pickle.read_file()

# Write Pickle object by object
with pickle.open(create=True):
    for obj in data:
        pickle.write(obj)

# Read all objects from the Pickle
data = [obj for obj in pickle]

# Read the first object
with file:
    first = file.read()
```
"""
from __future__ import annotations

import pickle
from typing import Iterable

from cerbernetix.toolbox.files.file_manager import FileManager

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
    """Offers a simple API for reading and writing pickle files.

    The class binds a filename with a set of properties so that it can be opened in a consistent
    way.

    The read API does not allow to size the data to read. However, it reads the file record by
    record.

    Attributes:
        filename (str): The path to the file to manage.
        binary (bool): The type of file, say binary. It must always be True.

    Examples:
    ```python
    from cerbernetix.toolbox.files import PickleFile

    file = PickleFile("path/to/the/file")

    # write some objects to the file
    with file(create=True):
        file.write(users)
        file.write(profiles)

    # read the records from the file
    with file:
        users = file.read()
        profiles = file.read()

    # gets the records in a list
    data = [obj for obj in file]

    # write records to the file
    file.write_file(data)

    # load the whole file, handling internally its opening
    data = file.read_file()
    ```
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
        """Creates a file manager for pickle files.

        Args:
            filename (str): The path to the file to manage.
            create (bool, optional): Expect to create the file. If it exists, it will be replaced.
            Defaults to False.
            append (bool, optional): Expect to extend the file. Data will be added at the end.
            Defaults to False.
            read (bool, optional): Expect to also read the file.
            Defaults to False.
            write (bool, optional): Expect to also write to the file.
            Defaults to False.
            protocol (int, optional): Tells the pickle writer to use the given protocol; supported
            protocols are 0 to HIGHEST_PROTOCOL. If a negative number is specified, HIGHEST_PROTOCOL
            is selected. When reading, the protocol version of the pickle is detected automatically.
            Defaults is DEFAULT_PROTOCOL.
            fix_imports (bool, optional): If fix_imports is true and protocol is less than 3,
            pickle will try to map the new Python 3 names to the old module names used in Python 2,
            so that the pickle data stream is readable with Python 2. Defaults to True.
            encoding (str, optional): Tell pickle how to decode 8-bit string instances pickled by
            Python 2. The encoding can be ‘bytes’ to read these 8-bit string instances as bytes objects.
            Using encoding='latin1' is required for unpickling NumPy arrays and instances of datetime,
            date and time pickled by Python 2. Defaults to ‘ASCII’.
            errors (str, optional): Tell pickle how to decode 8-bit string instances pickled by
            Python 2. Defaults to ‘strict’.
            buffers (optional): If buffers is None (the default), then all data necessary for
            deserialization must be contained in the pickle stream. This means that the buffer_callback
            argument was None when a Pickler was instantiated (or when dump() or dumps() was called). If
            buffers is not None, it should be an iterable of buffer-enabled objects that is consumed
            each time the pickle stream references an out-of-band buffer view. Such buffers have been
            given in order to the buffer_callback of a Pickler object.
            buffer_callback (optional): If buffer_callback is None (the default), buffer views are
            serialized into file as part of the pickle stream. If buffer_callback is not None, then
            it can be called any number of times with a buffer view. If the callback returns a false
            value (such as None), the given buffer is out-of-band; otherwise the buffer is
            serialized in-band, i.e. inside the pickle stream. It is an error if buffer_callback is
            not None and protocol is None or smaller than 5. Defaults to None.

        Examples:
        ```python
        from cerbernetix.toolbox.files import PickleFile

        # Create a file manager
        file = PickleFile('path/to/filename')

        # File can be opened directly as the manager is created
        with PickleFile('path/to/filename') as file:
            data = file.read()

        with PickleFile('path/to/filename', create=True) as file:
            file.write(data)

        # A file manager can open explicitly a file
        with file.open():
            obj = file.read()

        with file.open(create=True):
            file.write(obj)

        # It can also be opened implicitly
        with file:
            obj = file.read()

        # To create the file while opening implicitly
        with file(create=True):
            file.write(obj)

        # The file is also (re)opened when using the iteration protocol
        data = [obj for obj in file]
        ```
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

    def read_file(self, iterator: bool = False) -> Iterable:
        """Reads all the content from the file.

        The returned value can be either a list (default) or an iterator (when the iterator
        parameter is True).

        Note: If the file was already opened, it is first closed, then opened in read mode.

        Args:
            iterator (bool, optional): When True, the function will return an iterator instead of a
            list. Defaults to False.

        Raises:
            OSError: If the file cannot be read.
            FileNotFoundError: If the file does not exist.

        Returns:
            Iterable: The content read from the file.

        Examples:
        ```python
        from cerbernetix.toolbox.files import PickleFile

        file = PickleFile('path/to/filename')

        # A file can be read all at once
        data = file.read_file()

        # An iterator can be returned instead of a list
        for obj in file.read_file(iterator=True):
            print(obj)
        ```
        """
        if iterator:
            return self.close()

        return list(self)

    def write_file(self, data: Iterable) -> int:
        """Writes whole content to the file.

        Note: If the file was already opened, it is first closed, then opened in write mode.

        Args:
            data (Iterable): The content to write to the file.

        Raises:
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.

        Examples:
        ```python
        from cerbernetix.toolbox.files import PickleFile

        file = PickleFile('path/to/filename')

        # A file can be written all at once
        file.write_file(data)
        ```
        """
        size = 0
        with self.open(create=True):
            for row in data:
                size += self.write(row)

        return size

    def read(self) -> object:
        """Reads the next object from the file.

        Note: the file must be opened upfront.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be read.

        Returns:
            object: The object loaded from the file, or None if the file is at EOF.

        Examples:
        ```python
        from cerbernetix.toolbox.files import PickleFile

        file = PickleFile('path/to/filename')

        # When calling the read API, the next object in the file is read.
        with file:
            obj1 = file.read()
            obj2 = file.read()

        # The objects can also be read using the iteration protocol
        data = [obj for obj in file]
        ```
        """
        if self._file is None:
            raise ValueError("The file must be opened before reading from it!")

        try:
            return pickle.load(self._file, **self._reader_args)
        except EOFError:
            return None

    def write(self, data: object) -> int:
        """Writes an object to the file.

        Note: the file must be opened upfront.

        Args:
            data (object): The object to write to the file.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.

        Examples:
        ```python
        from cerbernetix.toolbox.files import PickleFile

        file = PickleFile('path/to/filename')

        # When calling the write API, an object is written to the file.
        with file(create=True):
            file.write(object1)
            file.write(object2)
        ```
        """
        if self._file is None:
            raise ValueError("The file must be opened before writing to it!")

        return self._file.write(pickle.dumps(data, **self._writer_args))


def read_pickle_file(filename: str, iterator: bool = False, **kwargs) -> Iterable:
    """Loads a list of objects from a file.

    The returned value can be either a list (default) or an iterator (when the iterator parameter
    is True).

    Args:
        filename (str): The path to the file to read.
        iterator (bool, optional): When True, the function will return an iterator instead of a
        list. Defaults to False.
        fix_imports (bool, optional): If fix_imports is true and protocol is less than 3,
        pickle will try to map the new Python 3 names to the old module names used in Python 2,
        so that the pickle data stream is readable with Python 2. Defaults to True.
        encoding (str, optional): Tell pickle how to decode 8-bit string instances pickled by
        Python 2. The encoding can be ‘bytes’ to read these 8-bit string instances as bytes objects.
        Using encoding='latin1' is required for unpickling NumPy arrays and instances of datetime,
        date and time pickled by Python 2. Defaults to ‘ASCII’.
        errors (str, optional): Tell pickle how to decode 8-bit string instances pickled by
        Python 2. Defaults to ‘strict’.
        buffers (optional): If buffers is None (the default), then all data necessary for
        deserialization must be contained in the pickle stream. This means that the buffer_callback
        argument was None when a Pickler was instantiated (or when dump() or dumps() was called). If
        buffers is not None, it should be an iterable of buffer-enabled objects that is consumed
        each time the pickle stream references an out-of-band buffer view. Such buffers have been
        given in order to the buffer_callback of a Pickler object.

    Raises:
        OSError: If the file cannot be read.
        FileNotFoundError: If the file does not exist.

    Returns:
        Iterable: The list of objects read from the file.

    Examples:
    ```python
    from cerbernetix.toolbox.files import read_pickle_file

    data = read_pickle_file('path/to/file')

    # An iterator can be returned instead of a list
    for obj in read_pickle_file('path/to/file', iterator=True):
        print(obj
    ```
    """
    return PickleFile(
        filename,
        **kwargs,
    ).read_file(iterator)


def write_pickle_file(filename: str, data: Iterable, **kwargs) -> int:
    """Writes a list of objects to a file.

    Args:
        filename (str): The path to the file to write.
        data (Iterable): The list of objects to write to the file.
        protocol (int, optional): Tells the pickle writer to use the given protocol; supported
        protocols are 0 to HIGHEST_PROTOCOL. If a negative number is specified, HIGHEST_PROTOCOL
        is selected. Defaults is DEFAULT_PROTOCOL.
        fix_imports (bool, optional): If fix_imports is true and protocol is less than 3,
        pickle will try to map the new Python 3 names to the old module names used in Python 2,
        so that the pickle data stream is readable with Python 2. Defaults to True.
        buffer_callback (optional): If buffer_callback is None (the default), buffer views are
        serialized into file as part of the pickle stream. If buffer_callback is not None, then
        it can be called any number of times with a buffer view. If the callback returns a false
        value (such as None), the given buffer is out-of-band; otherwise the buffer is
        serialized in-band, i.e. inside the pickle stream. It is an error if buffer_callback is
        not None and protocol is None or smaller than 5. Defaults to None.

    Raises:
        OSError: If the file cannot be written.

    Returns:
        int: The number of bytes written to the file.

    Examples:
    ```python
    from cerbernetix.toolbox.files import write_pickle_file

    data = [
        {'date': '2023-09-10', 'value': 42},
        {'date': '2023-09-11', 'value': 24},
        {'date': '2023-09-12', 'value': 44},
    ]

    write_pickle_file('path/to/file', data)
    ```
    """
    return PickleFile(
        filename,
        **kwargs,
    ).write_file(data)
