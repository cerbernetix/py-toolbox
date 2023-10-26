"""A collection of utilities for accessing files.

Examples:
```python
from cerbernetix.toolbox.files import fetch_content, get_file_mode, read_file, read_zip_file, write_file

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

# Fetch text content from a remote address
text = fetch_content("http://example.com/text")

# Fetch binary content from a remote address
data = fetch_content("http://example.com/data", binary=True)

# Considering the fetched content is a zip archive, extract the first file
content = read_zip_file(data)
```
"""
import os
import zipfile
from io import BytesIO

import requests


def get_file_mode(
    create: bool = False,
    append: bool = False,
    read: bool = False,
    write: bool = False,
    binary: bool = False,
) -> str:
    """Gets the file access mode given the expectations.

    The file access mode is defined by a string that contains flags for selecting the modes.
    For more info see [builtin open](https://docs.python.org/3/library/functions.html#open).

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
    from cerbernetix.toolbox.files import get_file_mode

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
    from cerbernetix.toolbox.files import read_file

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
    from cerbernetix.toolbox.files import write_file

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


def fetch_content(
    url: str,
    binary: bool = False,
    timeout: int | tuple = (6, 30),
    **kwargs,
) -> str | bytes:
    """Downloads content from the given URL.

    It uses an HTTP/GET request to fetch the remote data.

    Under the hood, it relies on requests to process the query.

    Args:
        url (str): The URL of the content to fetch.
        binary (bool): Tells if the content is binary (True) or text (False). When True,
        the function will return a bytes sequence, otherwise it will return a string sequence.
        timeout (int | tuple): The request timeout. Defaults to (6, 30).
        **kwargs: Additional parameters for the GET request. For more info, see [requests/api](https://requests.readthedocs.io/en/latest/api/).

    Raises:
        requests.RequestException: There was an ambiguous exception that occurred while handling
        the request.
        requests.ConnectionError: A Connection error occurred.
        requests.HTTPError: An HTTP error occurred.
        requests.URLRequired: A valid URL is required to make a request.
        requests.TooManyRedirects: Too many redirects.
        requests.ConnectTimeout: The request timed out while trying to connect to the remote server.
        Requests that produced this error are safe to retry.
        requests.ReadTimeout: The server did not send any data in the allotted amount of time.
        requests.Timeout: The request timed out. Catching this error will catch both ConnectTimeout
        and ReadTimeout errors.

    Returns:
        str | bytes: Returns a bytes buffer.

    Examples:
    ```python
    from cerbernetix.toolbox.files import fetch_content

    # Fetch text content from a remote address
    text = fetch_content("http://example.com/text")

    # Fetch binary content from a remote address
    data = fetch_content("http://example.com/data", binary=True)
    ```
    """
    response = requests.get(url=url, timeout=timeout, **kwargs)
    response.raise_for_status()
    return response.content if binary else response.text


def read_zip_file(buffer: bytes, filename: str = None, ext: str = None) -> bytes:
    """Extracts a file content from a Zip archive.

    If a filename is given, the corresponding file will be extracted from the archive. Otherwise,
    if a file extension is given, the first file having this extension in the archive will be
    extracted. If no filename nor extension is given, the fist available file is extracted.

    Args:
        buffer (bytes): A buffer of bytes representing the Zip archive.
        filename (str, optional): The name of the file to extract from the zip. If omitted, and the
        extension is given, the first file having the extension will be selected. Otherwise, the
        first available file will be selected. Defaults to None.
        ext (str, optional): The extension of the file to extract from the zip. This value is used
        if the filename is omitted, and in this case, the first file having the extension will be
        selected. Defaults to None.

    Raises:
        FileNotFoundError: If the file does not exist.

    Returns:
        bytes: The content of the file extracted from the Zip archive.

    Examples:
    ```python
    from cerbernetix.toolbox.files import read_zip

    with open('path/to/file.zip', 'rb') as file:
        zip = file.read()

        # The first file in the archive will be extracted
        data = read_zip(zip)

        # The specified file will be extracted from the archive
        data = read_zip(zip, filename='foo')

        # The first file having the extension will be extracted from the archive
        data = read_zip(zip, ext='.txt')
    ```
    """
    with zipfile.ZipFile(BytesIO(buffer)) as zip_file:
        found = False
        for info in zip_file.infolist():
            if filename:
                if filename == info.filename:
                    found = True
                    break

            elif ext:
                _, file_extension = os.path.splitext(info.filename)
                if file_extension.lower() == ext:
                    filename = info.filename
                    found = True
                    break
            else:
                filename = info.filename
                found = True
                break

        if not found:
            raise FileNotFoundError("The file does not exist in the archive.")

        with zip_file.open(filename, "r") as file:
            return file.read()
