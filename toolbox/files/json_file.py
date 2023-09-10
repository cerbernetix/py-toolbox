"""
Defines a class for reading and writing JSON files.
"""
import json
from typing import Any

from toolbox.files.file_manager import FileManager

# The default data encoding for JSON files
JSON_ENCODING = "utf-8"

# The default indent for JSON files
JSON_INDENT = 4


class JSONFile(FileManager):
    """
    Defines a class for reading and writing JSON files.
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
        **kwargs,
    ):
        """
        Creates a file manager for JSON files.

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

    def read(self) -> Any:
        """
        Reads the content from the file.

        Note: the file must be opened upfront.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be read.

        Returns:
            Any: The data read from the file.
        """
        data = super().read()

        if not data:
            return None

        return json.JSONDecoder().decode(data)

    def write(self, data: Any) -> int:
        """
        Writes content to the file.

        Note: the file must be opened upfront.

        Args:
            data (Any): The content to write to the file.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.
        """
        return super().write(
            json.JSONEncoder(
                sort_keys=True,
                indent=self.indent,
            ).encode(data)
        )


def read_json_file(
    filename: str,
    encoding: str = JSON_ENCODING,
    **kwargs,
) -> Any:
    """
    Reads a JSON content from a file.

    Args:
        filename (str): The path to the file to read.
        encoding (str, optional): The file encoding. Defaults to JSON_ENCODING.

    Raises:
        OSError: If the file cannot be read.
        FileNotFoundError: If the file does not exist.

    Returns:
        Any: The data read from the JSON file.
    """
    return JSONFile(filename, encoding=encoding, **kwargs).read_file()


def write_json_file(
    filename: str,
    data: Any,
    encoding: str = JSON_ENCODING,
    indent: int = JSON_INDENT,
    **kwargs,
) -> int:
    """
    Writes a JSON content to a file.

    Args:
        filename (str): The path to the file to write.
        data (Any): The content to write to the file.
        encoding (str, optional): The file encoding. Defaults to JSON_ENCODING.
        indent (int, optional): The line indent. Defaults to JSON_INDENT.

    Raises:
        OSError: If the file cannot be written.

    Returns:
        int: The number of bytes written to the file.
    """
    return JSONFile(
        filename,
        encoding=encoding,
        indent=indent,
        **kwargs,
    ).write_file(data)
