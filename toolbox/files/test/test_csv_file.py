"""Test the class for reading and writing CSV files."""
import unittest
from unittest.mock import MagicMock, Mock, patch

from toolbox.files import (
    CSV_DIALECT,
    CSV_ENCODING,
    CSVFile,
    read_csv_file,
    write_csv_file,
)

CSV_LINES_DICT = [
    {"first_name": "John", "last_name": "Smith", "age": "18", "city": "London"},
    {"first_name": "Jane", "last_name": "Doe", "age": "20", "city": "Paris"},
]
CSV_LINES_HEADLESS = [{key: key for key in CSV_LINES_DICT[0]}] + CSV_LINES_DICT
CSV_LINES_LIST = [
    ["first_name", "last_name", "age", "city"],
    ["John", "Smith", "18", "London"],
    ["Jane", "Doe", "20", "Paris"],
]
CSV_LINES_STRING = [
    '"first_name","last_name","age","city"\n',
    '"John","Smith","18","London"\n',
    '"Jane","Doe","20","Paris"\n',
]
CSV_LINES_REDUCED = [
    '"first_name","last_name"\n',
    '"John","Smith"\n',
    '"Jane","Doe"\n',
]
CSV_STRING = "".join(CSV_LINES_STRING)

# pylint: disable=protected-access


class TestCSVFile(unittest.TestCase):
    """Test suite for the class for reading and writing CSV files."""

    def test_construction_default(self):
        """Tests the construction of a CSV file manager with default parameters."""
        file_path = "/root/folder/file"

        file = CSVFile(file_path)

        self.assertEqual(file.filename, file_path)
        self.assertFalse(file.binary)
        self.assertEqual(file.dialect, CSV_DIALECT)
        self.assertEqual(file.encoding, CSV_ENCODING)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {"newline": ""})
        self.assertEqual(file._reader_args, {})
        self.assertEqual(file._writer_args, {})

    def test_construction_params(self):
        """Tests the construction of a CSV file manager with specific parameters."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        dialect = "foo"

        file = CSVFile(
            file_path,
            encoding=encoding,
            dialect=dialect,
            delimiter=";",
            quotechar='"',
            lineterminator="\n",
        )

        self.assertEqual(file.filename, file_path)
        self.assertFalse(file.binary)
        self.assertEqual(file.encoding, encoding)
        self.assertEqual(file.dialect, dialect)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {"newline": ""})
        self.assertEqual(
            file._reader_args,
            {
                "delimiter": ";",
                "quotechar": '"',
            },
        )
        self.assertEqual(
            file._writer_args,
            {
                "delimiter": ";",
                "quotechar": '"',
                "lineterminator": "\n",
            },
        )

    @patch("builtins.open")
    def test_construction_open(self, mock_file_open):
        """Tests the construction of a CSV file manager with opening."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        newline = ""
        dialect = "foo"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        with CSVFile(
            file_path,
            read=True,
            encoding=encoding,
            dialect=dialect,
        ) as file:
            self.assertEqual(file.filename, file_path)
            self.assertFalse(file.binary)
            self.assertEqual(file.encoding, encoding)
            self.assertEqual(file.dialect, dialect)
            self.assertIs(file._file, mock_file)
            self.assertEqual(file._open_args, {"newline": ""})
            self.assertEqual(file._reader_args, {})
            self.assertEqual(file._writer_args, {})

        mock_file_open.assert_called_once_with(
            file_path,
            mode="rt",
            encoding=encoding,
            newline=newline,
        )

    @patch("builtins.open")
    def test_open(self, mock_file_open):
        """Test a file can be opened."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        newline = ""

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = CSVFile(file_path, encoding=encoding)

        self.assertIs(file.open(), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="rt",
            encoding=encoding,
            newline=newline,
        )

    @patch("builtins.open")
    def test_open_create(self, mock_file_open):
        """Test a file can be opened for writing."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = CSVFile(file_path)

        self.assertIs(file.open(create=True), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="wt",
            encoding=CSV_ENCODING,
            newline="",
        )

    @patch("builtins.open")
    def test_open_close(self, mock_file_open):
        """Tests a file is closed before opening again."""
        file_path = "/root/folder/file"

        file = CSVFile(file_path)

        mock_file = Mock()
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file._file = mock_file

        file.open()

        mock_file.close.assert_called_once()
        mock_file_open.assert_called_once()

    def test_close_explicit(self):
        """Tests an opened file can be closed explicitly."""
        file_path = "/root/folder/file"

        file = CSVFile(file_path)

        mock_file = Mock()
        mock_file.close = Mock()
        file._file = mock_file

        file.close()
        file.close()

        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_close_auto(self, mock_file_open):
        """Tests an opened file is automatically closed."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = CSVFile(file_path)

        with file.open():
            mock_file_open.assert_called_once()

        mock_file.close.assert_called_once()

    def test_read_file(self):
        """Tests a file can be read at once."""
        file_path = "/root/folder/file"

        test_cases = [
            {
                "message": "dictionaries",
                "params": {},
                "data": CSV_LINES_STRING,
                "expected": CSV_LINES_DICT,
            },
            {
                "message": "fieldnames",
                "params": {
                    "fieldnames": ["first_name", "last_name", "age", "city"],
                },
                "data": CSV_LINES_STRING,
                "expected": CSV_LINES_HEADLESS,
            },
            {
                "message": "list",
                "params": {
                    "fieldnames": False,
                },
                "data": CSV_LINES_STRING,
                "expected": CSV_LINES_LIST,
            },
            {
                "message": "auto",
                "params": {
                    "dialect": "auto",
                },
                "data": CSV_LINES_STRING,
                "expected": CSV_LINES_DICT,
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case.get("message")):
                with patch("builtins.open") as mock_file_open:
                    mock_file = MagicMock()
                    mock_file.close = Mock()
                    mock_file.read = Mock(return_value="".join(test_case.get("data")))
                    mock_file.__iter__.return_value = test_case.get("data")
                    mock_file_open.return_value = mock_file

                    file = CSVFile(file_path, **test_case.get("params"))

                    self.assertEqual(file.read_file(), test_case.get("expected"))

                    mock_file_open.assert_called_once()
                    mock_file.close.assert_called_once()

    def test_write_file(self):
        """Tests a file can be written at once."""
        file_path = "/root/folder/file"

        test_cases = [
            {
                "message": "dictionaries",
                "params": {},
                "data": CSV_LINES_DICT,
                "expected": CSV_STRING,
            },
            {
                "message": "fieldnames",
                "params": {
                    "fieldnames": ["first_name", "last_name"],
                    "extrasaction": "ignore",
                },
                "data": CSV_LINES_DICT,
                "expected": "".join(CSV_LINES_REDUCED),
            },
            {
                "message": "list",
                "params": {},
                "data": CSV_LINES_LIST[1:],
                "expected": "".join(CSV_LINES_STRING[1:]),
            },
            {
                "message": "auto",
                "params": {
                    "dialect": "auto",
                },
                "data": CSV_LINES_DICT,
                "expected": CSV_STRING,
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case.get("message")):
                with patch("builtins.open") as mock_file_open:
                    data = ""

                    def write(line):
                        nonlocal data
                        data += line
                        return len(line)

                    mock_file = Mock()
                    mock_file.write = Mock(side_effect=write)
                    mock_file.close = Mock()
                    mock_file_open.return_value = mock_file

                    file = CSVFile(file_path, **test_case.get("params"))

                    self.assertEqual(
                        file.write_file(test_case.get("data")),
                        len(test_case.get("expected")),
                    )

                    self.assertEqual(data, test_case.get("expected"))

                    mock_file_open.assert_called_once()
                    mock_file.write.assert_called()
                    mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_read(self, mock_file_open):
        """Tests a file can be read line by line."""
        file_path = "/root/folder/file"

        mock_file = MagicMock()
        mock_file.close = Mock()
        mock_file.__iter__.return_value = CSV_LINES_STRING
        mock_file_open.return_value = mock_file

        file = CSVFile(file_path)

        self.assertRaises(ValueError, file.read)

        with file.open():
            for line in CSV_LINES_DICT:
                self.assertEqual(file.read(), line)

            self.assertIsNone(file.read())

        mock_file_open.assert_called_once()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_write(self, mock_file_open):
        """Tests a file can be written line by line."""
        file_path = "/root/folder/file"

        data = ""

        def write(line):
            nonlocal data
            data += line
            return len(line)

        mock_file = Mock()
        mock_file.write = Mock(side_effect=write)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = CSVFile(file_path)

        self.assertRaises(ValueError, lambda: file.write(CSV_LINES_DICT))

        with file.open(create=True):
            for row in CSV_LINES_DICT:
                file.write(row)

        self.assertEqual(data, CSV_STRING)

        mock_file_open.assert_called_once()
        mock_file.write.assert_called()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_call(self, mock_file_open):
        """Test a file can be opened by calling the instance."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        newline = ""

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = CSVFile(file_path, encoding=encoding)

        self.assertIs(file(), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path, mode="rt", encoding=encoding, newline=newline
        )

    @patch("builtins.open")
    def test_context(self, mock_file_open):
        """Tests an opened file is automatically closed."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        with CSVFile(file_path):
            mock_file_open.assert_called_once_with(
                file_path,
                mode="rt",
                encoding=CSV_ENCODING,
                newline="",
            )

        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_iterator(self, mock_file_open):
        """Tests a file can be read as an iterable."""
        file_path = "/root/folder/file"

        mock_file = MagicMock()
        mock_file.close = Mock()
        mock_file.__iter__.return_value = CSV_LINES_STRING
        mock_file_open.return_value = mock_file

        file = CSVFile(file_path)

        for idx, value in enumerate(file):
            self.assertEqual(value, CSV_LINES_DICT[idx])

        mock_file_open.assert_called_once()
        mock_file.close.assert_called_once()

        mock_file_open.reset_mock()
        mock_file.reset_mock()

        self.assertEqual(list(file), CSV_LINES_DICT)

        mock_file_open.assert_called_once()
        mock_file.close.assert_called_once()


class TestCSVFileHelpers(unittest.TestCase):
    """Test suite for the CSV file helpers."""

    @patch("builtins.open")
    def test_read_csv_file(self, mock_file_open):
        """Tests a CSV file can be read at once."""
        file_path = "/root/folder/file"

        mock_file = MagicMock()
        mock_file.close = Mock()
        mock_file.__iter__.return_value = CSV_LINES_STRING
        mock_file_open.return_value = mock_file

        self.assertEqual(read_csv_file(file_path), CSV_LINES_DICT)

        mock_file_open.assert_called_once()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_write_csv_file(self, mock_file_open):
        """Tests a CSV file can be written at once."""
        file_path = "/root/folder/file"

        data = ""

        def write(line):
            nonlocal data
            data += line
            return len(line)

        mock_file = Mock()
        mock_file.write = Mock(side_effect=write)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        self.assertEqual(write_csv_file(file_path, CSV_LINES_DICT), len(CSV_STRING))

        self.assertEqual(data, CSV_STRING)

        mock_file_open.assert_called_once()
        mock_file.write.assert_called()
        mock_file.close.assert_called_once()
