"""A collection of utilities for accessing files.

Examples:
```python
from toolbox.files import get_file_mode, read_file, write_file

# get_file_mode() is used to build a file access mode.
# For example to create a text file:
with open('path/to/file', get_file_mode(create=True)) as file:
    file.write('some content')

# Create a text file
text = 'Some content'
write_file('path/to/file', text, encoding='UTF-8')

# Create a binary file
data = b'...'
write_file('path/to/file', data, binary=True)

# Load a text file
text = read_file('path/to/file', encoding='UTF-8')

# Load a binary file
data = read_file('path/to/file', binary=True)
```
"""


def get_file_mode(
    create: bool = False,
    append: bool = False,
    read: bool = False,
    write: bool = False,
    binary: bool = False,
) -> str:
    """Gets the file access mode given the expectations.

    The file access mode is defined by a string that contains flags for selecting the modes.
    More info at https://docs.python.org/3/library/functions.html#open

    Args:
        create (bool, optional): Expect to create the file. If it exists, it will be replaced.
        Defaults to False.
        append (bool, optional): Expect to extend the file. Data will be added at the end.
        Defaults to False.
        read (bool, optional): Expect to also read the file.
        Defaults to False.
        write (bool, optional): Expect to also write to the file.
        Defaults to False.
        binary (bool, optional): Expect the file to be binary (text otherwise).
        Defaults to False.

    Returns:
        str: A string representing the file access mode.

    Examples:
    ```python
    from toolbox.files import get_file_mode

    # Create a text file
    with open('path/to/file', get_file_mode(create=True)) as file:
        file.write('some content')

    # Append to a text file
    with open('path/to/file', get_file_mode(append=True)) as file:
        file.write('some content')

    # Read a text file
    with open('path/to/file', get_file_mode()) as file:
        text = file.read()

    # Create a binary file
    with open('path/to/file', get_file_mode(create=True, binary=True)) as file:
        file.write(b'...')

    # Read a binary file
    with open('path/to/file', get_file_mode(binary=True)) as file:
        data = file.read()
    ```
    """
    if append:
        mode = "a"

        if read:
            mode += "+"

    elif create:
        mode = "w"

        if read:
            mode += "+"

    else:
        mode = "r"

        if write:
            mode += "+"

    if binary:
        mode += "b"
    else:
        mode += "t"

    return mode


def read_file(
    filename: str,
    binary: bool = False,
    encoding: str = None,
    **kwargs,
) -> str | bytes:
    """Reads a content from a file.

    Args:
        filename (str): The path to the file to read.
        binary (bool, optional): The type of file: binary (True) or text (False).
        Defaults to False.
        encoding (str, optional): The file encoding, only needed for text files.
        Defaults to None.

    Raises:
        OSError: If the file cannot be read.
        FileNotFoundError: If the file does not exist.

    Returns:
        str|bytes: The content read from the file.

    Examples:
    ```python
    from toolbox.files import read_file

    # Load a text file
    text = read_file('path/to/file', encoding='UTF-8')

    # Load a binary file
    data = read_file('path/to/file', binary=True)
    ```
    """
    with open(
        filename,
        mode=get_file_mode(binary=binary),
        encoding=encoding,
        **kwargs,
    ) as file:
        return file.read()


def write_file(
    filename: str,
    data: str | bytes,
    binary: bool = False,
    encoding: str = None,
    **kwargs,
) -> int:
    """Writes a content to a file.

    Args:
        filename (str): The path to the file to write.
        data (str|bytes): The content to write to the file.
        binary (bool, optional): The type of file: binary (True) or text (False).
        Defaults to False.
        encoding (str, optional): The file encoding, only needed for text files.
        Defaults to None.

    Raises:
        OSError: If the file cannot be written.

    Returns:
        int: The number of bytes written to the file.

    Examples:
    ```python
    from toolbox.files import write_file

    # Create a text file
    text = 'Some content'
    write_file('path/to/file', text, encoding='UTF-8')

    # Create a binary file
    data = b'...'
    write_file('path/to/file', data, binary=True)
    ```
    """
    with open(
        filename,
        mode=get_file_mode(create=True, binary=binary),
        encoding=encoding,
        **kwargs,
    ) as file:
        return file.write(data)
