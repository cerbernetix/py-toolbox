"""A simple API for reading and writing JSON files.

Examples:
```python
from cerbernetix.toolbox.files import JSONFile, read_json_file, write_json_file

filename = 'path/to/file.json'
json_data = [
    {'date': '2023-09-10', 'value': 42},
    {'date': '2023-09-11', 'value': 24},
    {'date': '2023-09-12', 'value': 44},
]

# Create a JSON file from the given data
write_json_file(filename, json_data, encoding='UTF-8', indent=2)

# Read the JSON data from an existing file
json_data = read_json_file(filename, encoding='UTF-8', indent=2)

# Use a file manager
json = JSONFile(filename, encoding='UTF-8', indent=2)

# Create a JSON file from the given data
json.write_file(json_data)

# Read the JSON data from an existing file
json_data = json.read_file()

# Write JSON content
with json.open(create=True):
    json.write(json_data)

# Read JSON content
with file:
    json_data = file.read()
```
"""

import json
from typing import Any

from cerbernetix.toolbox.files.file_manager import FileManager

# The default data encoding for JSON files
JSON_ENCODING = "utf-8"

# The default indent for JSON files
JSON_INDENT = 4

# The default value for whether or not to sort the keys in JSON files
JSON_SORT_KEYS = False

# The default value for whether or not to skip the keys not having an allowed type in JSON files
JSON_SKIP_KEYS = False

# The default value for escaping non-ascii chars in JSON files
JSON_ENSURE_ASCII = True


class JSONFile(FileManager):
    """Offers a simple API for reading and writing JSON files.

    The class binds a filename with a set of properties so that it can be opened in a consistent
    way.

    The read API reads all the content at once, and so do the write API too.

    Attributes:
        filename (str): The path to the file to manage.
        binary (bool): The type of file, say text. It must always be False.
        encoding (str, optional): The file encoding.
        indent (int, optional): The line indent.
        sort_keys (bool, optional): Whether or not to sort the keys.
        skip_keys (bool, optional): Whether or not to skip the keys not having an allowed type.
        ensure_ascii (bool, optional): Whether or not to escape non-ascii chars.

    Examples:
    ```python
    from cerbernetix.toolbox.files import JSONFile

    file = JSONFile("path/to/the/file.json", indent=4, encoding="UTF-8")

    # write content to the file
    file.write_file(json)

    # open the file, then read its content
    with file:
        json = file.read()

    # write data to the file
    with file(create=True):
        file.write(json)

    # load the whole file, handling internally its opening
    json = file.read_file()
    ```
    """

    def __init__(
        self,
        filename: str,
        create: bool = False,
        append: bool = False,
        read: bool = False,
        write: bool = False,
        encoding: str = JSON_ENCODING,
        indent: int = JSON_INDENT,
        sort_keys: bool = JSON_SORT_KEYS,
        skip_keys: bool = JSON_SKIP_KEYS,
        ensure_ascii: bool = JSON_ENSURE_ASCII,
        **kwargs,
    ):
        """Creates a file manager for JSON files.

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
            encoding (str, optional): The file encoding. Defaults to JSON_ENCODING.
            indent (int, optional): The line indent. Defaults to JSON_INDENT.
            sort_keys (bool, optional): Whether or not to sort the keys. Defaults to JSON_SORT_KEYS.
            skip_keys (bool, optional): Whether or not to skip the keys not having an allowed type.
            Defaults to JSON_SKIP_KEYS.
            ensure_ascii (bool, optional): Whether or not to escape non-ascii chars.
            Defaults to JSON_ENSURE_ASCII.

        Examples:
        ```python
        from cerbernetix.toolbox.files import JSONFile

        # Create a file manager
        file = JSONFile('path/to/filename')

        # File can be opened directly as the manager is created
        with JSONFile('path/to/filename') as file:
            data = file.read()

        with JSONFile('path/to/filename', create=True) as file:
            file.write(data)

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
        super().__init__(
            filename,
            binary=False,
            create=create,
            append=append,
            read=read,
            write=write,
            encoding=encoding,
            **kwargs,
        )
        self.indent = indent
        self.sort_keys = sort_keys
        self.skip_keys = skip_keys
        self.ensure_ascii = ensure_ascii

    def read(self) -> Any:
        """Reads the content from the file.

        Note: the file must be opened upfront.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be read.

        Returns:
            Any: The data read from the file.

        Examples:
        ```python
        from cerbernetix.toolbox.files import JSONFile

        file = JSONFile('path/to/filename')

        # When calling the read API, the whole JSON content is read from the file.
        with file:
            json = file.read()
        ```
        """
        data = super().read()

        if not data:
            return None

        return json.JSONDecoder().decode(data)

    def write(self, data: Any) -> int:
        """Writes content to the file.

        Note: the file must be opened upfront.

        Args:
            data (Any): The content to write to the file.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.

        Examples:
        ```python
        from cerbernetix.toolbox.files import JSONFile

        file = JSONFile('path/to/filename')

        # When calling the write API, the whole JSON is written to the file.
        with file(create=True):
            file.write(json)
        ```
        """
        return super().write(
            json.JSONEncoder(
                skipkeys=self.skip_keys,
                ensure_ascii=self.ensure_ascii,
                sort_keys=self.sort_keys,
                indent=self.indent,
            ).encode(data)
        )


def read_json_file(
    filename: str,
    encoding: str = JSON_ENCODING,
    **kwargs,
) -> Any:
    """Reads a JSON content from a file.

    Args:
        filename (str): The path to the file to read.
        encoding (str, optional): The file encoding. Defaults to JSON_ENCODING.

    Raises:
        OSError: If the file cannot be read.
        FileNotFoundError: If the file does not exist.

    Returns:
        Any: The data read from the JSON file.

    Examples:
    ```python
    from cerbernetix.toolbox.files import read_json_file

    json_data = read_json_file('path/to/file', encoding='UTF-8')
    ```
    """
    return JSONFile(filename, encoding=encoding, **kwargs).read_file()


def write_json_file(
    filename: str,
    data: Any,
    encoding: str = JSON_ENCODING,
    indent: int = JSON_INDENT,
    sort_keys: bool = JSON_SORT_KEYS,
    skip_keys: bool = JSON_SKIP_KEYS,
    ensure_ascii: bool = JSON_ENSURE_ASCII,
    **kwargs,
) -> int:
    """Writes a JSON content to a file.

    Args:
        filename (str): The path to the file to write.
        data (Any): The content to write to the file.
        encoding (str, optional): The file encoding. Defaults to JSON_ENCODING.
        indent (int, optional): The line indent. Defaults to JSON_INDENT.
        sort_keys (bool, optional): Whether or not to sort the keys. Defaults to JSON_SORT_KEYS.
        skip_keys (bool, optional): Whether or not to skip the keys not having an allowed type.
        Defaults to JSON_SKIP_KEYS.
        ensure_ascii (bool, optional): Whether or not to escape non-ascii chars.
        Defaults to JSON_ENSURE_ASCII.

    Raises:
        OSError: If the file cannot be written.

    Returns:
        int: The number of bytes written to the file.

    Examples:
    ```python
    from cerbernetix.toolbox.files import write_json_file

    json_data = [
        {'date': '2023-09-10', 'value': 42},
        {'date': '2023-09-11', 'value': 24},
        {'date': '2023-09-12', 'value': 44},
    ]

    write_json_file('path/to/file', json_data, encoding='UTF-8', indent=2)
    ```
    """
    return JSONFile(
        filename,
        encoding=encoding,
        indent=indent,
        sort_keys=sort_keys,
        skip_keys=skip_keys,
        ensure_ascii=ensure_ascii,
        **kwargs,
    ).write_file(data)
