"""A simple API for reading and writing CSV files.

Examples:
```python
from toolbox.files import CSVFile, read_csv_file, write_csv_file

filename = 'path/to/file.csv'
csv_data = [
    {'date': '2023-09-10', 'value': 42},
    {'date': '2023-09-11', 'value': 24},
    {'date': '2023-09-12', 'value': 44},
]

# Create a CSV file from the given data
write_csv_file(filename, csv_data, encoding='UTF-8', dialect='excel')

# Read the CSV data from an existing file
csv_data = read_csv_file(filename, encoding='UTF-8', dialect='excel')

# Use a file manager
csv = CSVFile(filename, encoding='UTF-8', dialect='excel')

# Create a CSV file from the given data
csv.write_file(csv_data)

# Read the CSV data from an existing file
csv_data = csv.read_file()

# Write CSV row by row
with csv.open(create=True):
    for row in csv_data:
        csv.write(row)

# Read all rows from the CSV
csv_data = [row for row in csv]

# Read the first row
with file:
    first = file.read()
```
"""
from __future__ import annotations

import csv
from typing import Iterable

from toolbox.files.file_manager import FileManager

# The default data encoding for CSV files
CSV_ENCODING = "utf-8"

# The default CSV dialect
CSV_DIALECT = "unix"

# The amount of bytes to read for auto-detecting the CSV dialect
CSV_SAMPLE_SIZE = 1024

# The parameters that will be forwarded to the CSV reader
CSV_READER_PARAMS = [
    "delimiter",
    "doublequote",
    "escapechar",
    "quotechar",
    "quoting",
    "skipinitialspace",
    "strict",
    "fieldnames",
    "restkey",
    "restval",
]

# The parameters that will be forwarded to the CSV writer
CSV_WRITER_PARAMS = [
    "delimiter",
    "doublequote",
    "escapechar",
    "lineterminator",
    "quotechar",
    "quoting",
    "skipinitialspace",
    "strict",
    "fieldnames",
    "restval",
    "extrasaction",
]

# The parameters that will be forwarded to the file opener
FILE_OPEN_PARAMS = ["buffering", "errors", "closefd", "opener"]


class CSVFile(FileManager):
    """Offers a simple API for reading and writing CSV files.

    The class binds a filename with a set of properties so that it can be opened in a consistent
    way.

    The read API does not allow to size the data to read. However, it reads the file row by row.

    Attributes:
        filename (str): The path to the file to manage.
        binary (bool): The type of file, say text. It must always be False.
        encoding (str, optional): The file encoding.
        dialect (str, optional): The CSV dialect to use. If 'auto' is given, the reader will try
        detecting the CSV dialect by reading a sample at the head of the file.

    Examples:
    ```python
    from toolbox.files import CSVFile

    file = CSVFile("path/to/the/file", dialect='excel', encoding="UTF-8")

    # write rows to the file
    file.write_file(csv)

    # read the first row of the CSV
    with file.open():
        first = file.read()

    # gets the CSV in a list
    csv = [row for row in file]

    # write data to the file
    with file(create=True):
        for row in csv:
            file.write(row)

    # load the whole file, handling internally its opening
    csv = file.read_file()
    ```
    """

    def __init__(
        self,
        filename: str,
        create: bool = False,
        append: bool = False,
        read: bool = False,
        write: bool = False,
        encoding: str = CSV_ENCODING,
        dialect: str = CSV_DIALECT,
        **kwargs,
    ):
        r"""Creates a file manager for CSV files.

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
            encoding (str, optional): The file encoding. Defaults to CSV_ENCODING.
            dialect (str, optional): The CSV dialect to use. If 'auto' is given, the reader will
            try detecting the CSV dialect by reading a sample at the head of the file.
            Defaults to CSV_DIALECT.
            delimiter (str, optional): A one-character string used to separate fields.
            Defaults to ",".
            doublequote (bool, optional): Controls how instances of quotechar appearing inside a
            field should themselves be quoted. When True, the character is doubled. When False, the
            escapechar is used as a prefix to the quotechar. Defaults to True.
            escapechar (str, optional):  A one-character string used by the writer to escape the
            delimiter if quoting is set to QUOTE_NONE and the quotechar if doublequote is False.
            On reading, the escapechar removes any special meaning from the following character.
            Defaults to None, which disables escaping.
            lineterminator (str, optional): The string used to terminate lines produced by the
            writer. Defaults to "\r\n".
            quotechar (str, optional): A one-character string used to quote fields containing
            special characters, such as the delimiter or quotechar, or which contain new-line
            characters. Defaults to '"'.
            quoting (bool, optional): Controls when quotes should be be generated by the writer,
            or recognized by the reader. It can take on any of the QUOTE_* constants.
            Defaults to QUOTE_MINIMAL.
            skipinitialspace (bool, optional): When True, spaces immediately following the
            delimiter are ignored. The default is False.
            strict (bool, optional):  When True, raise exception Error on bad CSV input.
            Defaults to False.
            fieldnames (sequence, optional): The name of each column in the CSV. Depending on the
            access mode, the manner how fieldnames is consumed differs.

            When reading, if fieldnames is omitted, the values in the first row of the file will be
            used as the fieldnames. Regardless of how the fieldnames are determined, the dictionary
            preserves their original ordering.

            If a row has more fields than fieldnames, the remaining data is put in a list and stored
            with the fieldname specified by restkey (which defaults to None). If a non-blank row has
            fewer fields than fieldnames, the missing values are filled-in with the value of restval
            (which defaults to None).

            For reading headless CSV, set fieldnames to False.

            When writing, if fieldnames is omitted and the first row is a dictionary, its keys will
            be used as fieldnames. Every subsequent row will need to be dictionaries as well. If the
            first row is a sequence, no header will be added, and all subsequent row will need to be
            sequences as well.

            The fieldnames sequence identify the order in which values from the rows are written to
            the file. The optional restval parameter specifies the value to be written if the
            dictionary is missing a key in fieldnames. If the current row contains a key not found
            in fieldnames, the optional extrasaction parameter indicates what action to take. If it
            is set to 'raise', the default value, a ValueError is raised. If it is set to 'ignore',
            extra values in the row are ignored. Any other optional or keyword arguments are passed
            to the underlying writer instance.

        Examples:
        ```python
        from toolbox.files import CSVFile

        # Create a file manager
        file = CSVFile('path/to/filename')

        # File can be opened directly as the manager is created
        with CSVFile('path/to/filename') as file:
            csv_data = file.read()

        with CSVFile('path/to/filename', create=True) as file:
            file.write(csv_data)

        # A file manager can open explicitly a file
        with file.open():
            row = file.read()

        with file.open(create=True):
            file.write(row)

        # It can also be opened implicitly
        with file:
            row = file.read()

        # To create the file while opening implicitly
        with file(create=True):
            file.write(row)

        # The file is also (re)opened when using the iteration protocol
        csv_data = [row for row in file]
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
            newline="",
            **{key: value for key, value in kwargs.items() if key in FILE_OPEN_PARAMS},
        )
        self.dialect = dialect
        self._reader_args = {
            key: value for key, value in kwargs.items() if key in CSV_READER_PARAMS
        }
        self._writer_args = {
            key: value for key, value in kwargs.items() if key in CSV_WRITER_PARAMS
        }
        self._reader = None
        self._writer = None

    def close(self) -> CSVFile:
        """Closes the file.

        Note: it does nothing if the file is already closed.

        Returns:
            CSVFile: Chains the instance.

        Examples:
        ```python
        from toolbox.files import CSVFile

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
        super().close()

        self._reader = None
        self._writer = None

        return self

    def read_file(self) -> list[dict | list]:
        """Reads all the content from the file.

        Note: If the file was already opened, it is first closed, then opened in read mode.

        Raises:
            OSError: If the file cannot be read.
            FileNotFoundError: If the file does not exist.

        Returns:
            list[dict | list]: The content read from the file.

        Examples:
        ```python
        from toolbox.files import CSVFile

        file = CSVFile('path/to/filename')

        # A file can be read all at once
        data = file.read_file()
        ```
        """
        return list(self)

    def write_file(self, data: Iterable[dict | list]) -> int:
        """Writes whole content to the file.

        Note: If the file was already opened, it is first closed, then opened in write mode.

        Args:
            data (Iterable[dict | list]): The content to write to the file.

        Raises:
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.

        Examples:
        ```python
        from toolbox.files import CSVFile

        file = CSVFile('path/to/filename')

        # A file can be written all at once
        file.write_file(data)
        ```
        """
        size = 0
        with self.open(create=True):
            for row in data:
                size += self.write(row)

        return size

    def read(self) -> dict | list:
        """Reads the next content from the file.

        Note: the file must be opened upfront.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be read.

        Returns:
            dict | list: The content loaded from the file, or None if the file is at EOF.

        Examples:
        ```python
        from toolbox.files import CSVFile

        file = CSVFile('path/to/filename')

        # When calling the read API, the next row in the file is read.
        with file:
            row1 = file.read()
            row2 = file.read()

        # The CSV rows can also be read using the iteration protocol
        csv_data = [row for row in file]
        ```
        """
        if self._file is None:
            raise ValueError("The file must be opened before reading from it!")

        if self._reader is None:
            kwargs = self._reader_args.copy()

            if kwargs.get("fieldnames") is False:
                reader = csv.reader
                kwargs.pop("fieldnames")
            else:
                reader = csv.DictReader

            dialect = self.dialect
            if dialect == "auto":
                dialect = csv.Sniffer().sniff(self._file.read(CSV_SAMPLE_SIZE))
                self._file.seek(0)

            self._reader = reader(self._file, dialect=dialect, **kwargs)

        try:
            return next(self._reader)
        except StopIteration:
            return None

    def write(self, data: dict | list) -> int:
        """Writes content to the file.

        Note: the file must be opened upfront.

        Args:
            data (dict | list): The content to write to the file.

        Raises:
            ValueError: If the file is not opened.
            OSError: If the file cannot be written.

        Returns:
            int: The number of bytes written.

        Examples:
        ```python
        from toolbox.files import CSVFile

        file = CSVFile('path/to/filename')

        # When calling the write API, a CSV row is written to the file.
        with file(create=True):
            file.write(row1)
            file.write(row2)
        ```
        """
        if self._file is None:
            raise ValueError("The file must be opened before writing to it!")

        count = 0

        if self._writer is None:
            kwargs = self._writer_args.copy()

            if isinstance(data, dict):
                header = True

                if "fieldnames" not in kwargs or kwargs.get("fieldnames") is False:
                    kwargs["fieldnames"] = data.keys()

                writer = csv.DictWriter
            else:
                if "fieldnames" in kwargs:
                    kwargs.pop("fieldnames")

                header = False
                writer = csv.writer

            dialect = self.dialect
            if dialect == "auto":
                dialect = CSV_DIALECT

            self._writer = writer(self._file, dialect=dialect, **kwargs)

            if header:
                count += self._writer.writeheader()

        return count + self._writer.writerow(data)


def read_csv_file(
    filename: str,
    encoding: str = CSV_ENCODING,
    dialect: str = CSV_DIALECT,
    **kwargs,
) -> list[dict | list]:
    """Reads a CSV content from a file.

    Args:
        filename (str): The path to the file to read.
        encoding (str, optional): The file encoding. Defaults to CSV_ENCODING.
        dialect (str, optional): The CSV dialect to use. If 'auto' is given, the reader will
        try detecting the CSV dialect by reading a sample at the head of the file.
        Defaults to CSV_DIALECT.
        delimiter (str, optional): A one-character string used to separate fields.
        Defaults to ','.
        doublequote (bool, optional): Controls how instances of quotechar appearing inside a
        field should themselves be quoted. When True, the character is doubled. When False, the
        escapechar is used as a prefix to the quotechar. Defaults to True.
        escapechar (str, optional):  A one-character string used to removes any special meaning
        from the following character. Defaults to None, which disables escaping.
        quotechar (str, optional): A one-character string used to quote fields containing
        special characters, such as the delimiter or quotechar, or which contain new-line
        characters. Defaults to '"'.
        quoting (bool, optional): Controls when quotes should be be recognized by the reader.
        It can take on any of the QUOTE_* constants. Defaults to QUOTE_MINIMAL.
        skipinitialspace (bool, optional): When True, spaces immediately following the
        delimiter are ignored. The default is False.
        strict (bool, optional):  When True, raise exception Error on bad CSV input.
        Defaults to False.
        fieldnames (sequence, optional): The name of each column in the CSV. If fieldnames is
        omitted, the values in the first row of the file will be used as the fieldnames. Regardless
        of how the fieldnames are determined, the dictionary preserves their original ordering.
        If a row has more fields than fieldnames, the remaining data is put in a list and stored
        with the fieldname specified by restkey (which defaults to None). If a non-blank row has
        fewer fields than fieldnames, the missing values are filled-in with the value of restval
        (which defaults to None).

        For reading headless CSV, set fieldnames to False.

    Raises:
        OSError: If the file cannot be read.
        FileNotFoundError: If the file does not exist.

    Returns:
        list[dict | list]: The data read from the CSV file.

    Examples:
    ```python
    from toolbox.files import read_csv_file

    csv_data = read_csv_file('path/to/file', encoding='UTF-8', dialect='excel')
    ```
    """
    return CSVFile(
        filename,
        encoding=encoding,
        dialect=dialect,
        **kwargs,
    ).read_file()


def write_csv_file(
    filename: str,
    data: Iterable[dict | list],
    encoding: str = CSV_ENCODING,
    dialect: str = CSV_DIALECT,
    **kwargs,
) -> int:
    r"""Writes a CSV content to a file.

    Args:
        filename (str): The path to the file to write.
        data (Iterable[dict | list]): The content to write to the file.
        encoding (str, optional): The file encoding. Defaults to CSV_ENCODING.
        dialect (str, optional): The CSV dialect to use. Defaults to CSV_DIALECT.
        delimiter (str, optional): A one-character string used to separate fields.
        Defaults to ','.
        doublequote (bool, optional): Controls how instances of quotechar appearing inside a
        field should themselves be quoted. When True, the character is doubled. When False, the
        escapechar is used as a prefix to the quotechar. Defaults to True.
        escapechar (str, optional):  A one-character string used by the writer to escape the
        delimiter if quoting is set to QUOTE_NONE and the quotechar if doublequote is False.
        Defaults to None, which disables escaping.
        lineterminator (str, optional): The string used to terminate lines produced by the
        writer. Defaults to "\r\n".
        quotechar (str, optional): A one-character string used to quote fields containing
        special characters, such as the delimiter or quotechar, or which contain new-line
        characters. Defaults to '"'.
        quoting (bool, optional): Controls when quotes should be be generated by the writer.
        It can take on any of the QUOTE_* constants. Defaults to QUOTE_MINIMAL.
        skipinitialspace (bool, optional): When True, spaces immediately following the
        delimiter are ignored. The default is False.
        strict (bool, optional):  When True, raise exception Error on bad CSV input.
        Defaults to False.
        fieldnames (sequence, optional): The name of each column in the CSV. If fieldnames is
        omitted and the first row is a dictionary, its keys will be used as fieldnames. Every
        subsequent row will need to be dictionaries as well. If the first row is a sequence, no
        header will be added, and all subsequent row will need to be sequences as well.

        The fieldnames sequence identify the order in which values from the rows are written to
        the file. The optional restval parameter specifies the value to be written if the
        dictionary is missing a key in fieldnames. If the current row contains a key not found
        in fieldnames, the optional extrasaction parameter indicates what action to take. If it
        is set to 'raise', the default value, a ValueError is raised. If it is set to 'ignore',
        extra values in the row are ignored. Any other optional or keyword arguments are passed
        to the underlying writer instance.

    Raises:
        OSError: If the file cannot be written.

    Returns:
        int: The number of bytes written to the file.

    Examples:
    ```python
    from toolbox.files import write_csv_file

    csv_data = [
        {'date': '2023-09-10', 'value': 42},
        {'date': '2023-09-11', 'value': 24},
        {'date': '2023-09-12', 'value': 44},
    ]

    write_csv_file('path/to/file', csv_data, encoding='UTF-8', dialect='excel')
    ```
    """
    return CSVFile(
        filename,
        encoding=encoding,
        dialect=dialect,
        **kwargs,
    ).write_file(data)
