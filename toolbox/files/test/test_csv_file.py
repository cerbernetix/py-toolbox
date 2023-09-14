"""Test the class for reading and writing CSV files."""
import unittest
import zipfile
from typing import Iterator
from unittest.mock import MagicMock, Mock, patch

from toolbox.files import (
    CSV_DIALECT,
    CSV_ENCODING,
    CSVFile,
    read_csv_file,
    read_zip_csv,
    write_csv_file,
)
from toolbox.testing import test_cases

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

    @test_cases(
        [
            ["dictionaries", {}, CSV_LINES_STRING, CSV_LINES_DICT],
            [
                "fieldnames",
                {"fieldnames": ["first_name", "last_name", "age", "city"]},
                CSV_LINES_STRING,
                CSV_LINES_HEADLESS,
            ],
            ["list", {"fieldnames": False}, CSV_LINES_STRING, CSV_LINES_LIST],
            ["auto", {"dialect": "auto"}, CSV_LINES_STRING, CSV_LINES_DICT],
        ]
    )
    def test_read_file(self, _, params, data, expected):
        """Tests a file can be read at once."""
        file_path = "/root/folder/file"

        with patch("builtins.open") as mock_file_open:
            mock_file = MagicMock()
            mock_file.close = Mock()
            mock_file.read = Mock(return_value="".join(data))
            mock_file.__iter__.return_value = data
            mock_file_open.return_value = mock_file

            file = CSVFile(file_path, **params)

            result = file.read_file()
            self.assertIsInstance(result, list)
            self.assertEqual(result, expected)

            mock_file_open.assert_called_once()
            mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_read_file_iterator(self, mock_file_open):
        """Tests a file can be read at once using an iterator."""
        file_path = "/root/folder/file"

        mock_file = MagicMock()
        mock_file.close = Mock()
        mock_file.read = Mock(return_value="".join(CSV_LINES_STRING))
        mock_file.__iter__.return_value = CSV_LINES_STRING
        mock_file_open.return_value = mock_file

        file = CSVFile(file_path)

        result = file.read_file(iterator=True)
        self.assertIsInstance(result, Iterator)
        self.assertEqual(list(result), CSV_LINES_DICT)

        mock_file_open.assert_called_once()
        mock_file.close.assert_called_once()

    @test_cases(
        [
            ["dictionaries", {}, CSV_LINES_DICT, CSV_STRING],
            [
                "dictionaries with fieldnames=False",
                {"fieldnames": False},
                CSV_LINES_DICT,
                CSV_STRING,
            ],
            [
                "fieldnames",
                {"fieldnames": ["first_name", "last_name"], "extrasaction": "ignore"},
                CSV_LINES_DICT,
                "".join(CSV_LINES_REDUCED),
            ],
            ["list", {}, CSV_LINES_LIST[1:], "".join(CSV_LINES_STRING[1:])],
            [
                "list with fieldnames=False",
                {"fieldnames": False},
                CSV_LINES_LIST[1:],
                "".join(CSV_LINES_STRING[1:]),
            ],
            ["auto", {"dialect": "auto"}, CSV_LINES_DICT, CSV_STRING],
        ]
    )
    def test_write_file(self, _, params, data, expected):
        """Tests a file can be written at once."""
        file_path = "/root/folder/file"

        with patch("builtins.open") as mock_file_open:
            written = ""

            def write(line):
                nonlocal written
                written += line
                return len(line)

            mock_file = Mock()
            mock_file.write = Mock(side_effect=write)
            mock_file.close = Mock()
            mock_file_open.return_value = mock_file

            file = CSVFile(file_path, **params)

            self.assertEqual(file.write_file(data), len(expected))

            self.assertEqual(written, expected)

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

        result = read_csv_file(file_path)
        self.assertIsInstance(result, list)
        self.assertEqual(result, CSV_LINES_DICT)

        mock_file_open.assert_called_once()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_read_csv_file_iterator(self, mock_file_open):
        """Tests a file can be read at once using an iterator."""
        file_path = "/root/folder/file"

        mock_file = MagicMock()
        mock_file.close = Mock()
        mock_file.__iter__.return_value = CSV_LINES_STRING
        mock_file_open.return_value = mock_file

        result = read_csv_file(file_path, iterator=True)
        self.assertIsInstance(result, Iterator)
        self.assertEqual(list(result), CSV_LINES_DICT)

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

    @test_cases(
        [
            [
                "default",
                {},
                "FOO.CSV",
                CSV_STRING,
                CSV_LINES_DICT,
            ],
            [
                "filename given",
                {"filename": "bar.csv"},
                "bar.csv",
                CSV_STRING,
                CSV_LINES_DICT,
            ],
            [
                "fieldnames given",
                {"fieldnames": ["first_name", "last_name", "age", "city"]},
                "FOO.CSV",
                CSV_STRING,
                CSV_LINES_HEADLESS,
            ],
            [
                "fieldnames=False",
                {"fieldnames": False},
                "FOO.CSV",
                CSV_STRING,
                CSV_LINES_LIST,
            ],
            [
                "dialect auto",
                {"dialect": "auto"},
                "FOO.CSV",
                CSV_STRING,
                CSV_LINES_DICT,
            ],
        ]
    )
    @patch("zipfile.ZipFile")
    def test_read_zip_csv(self, _, params, filename, content, expected, zip_mock):
        """Tests it reads a CSV from a Zip."""
        buffer = bytes(content, encoding="utf-8")

        zip_content_mock = Mock()
        zip_content_mock.return_value = zip_content_mock
        zip_content_mock.decode.return_value = content

        zip_file_mock = MagicMock()
        zip_file_mock.return_value = zip_file_mock
        zip_file_mock.__enter__.return_value = zip_file_mock
        zip_file_mock.read.return_value = zip_content_mock

        zip_mock.return_value = zip_mock
        zip_mock.__enter__.return_value = zip_mock
        zip_mock.open.return_value = zip_file_mock
        zip_mock.infolist.return_value = [
            zipfile.ZipInfo("foo.bar"),
            zipfile.ZipInfo("FOO.CSV"),
            zipfile.ZipInfo("foo.baz"),
            zipfile.ZipInfo("bar.csv"),
        ]

        result = read_zip_csv(buffer, **params)

        zip_mock.open.assert_called_once_with(filename, "r")

        self.assertIsInstance(result, list)
        self.assertEqual(result, expected)

    @patch("zipfile.ZipFile")
    def test_read_zip_csv_iterator(self, zip_mock):
        """Tests it reads a CSV from a Zip using an iterator."""
        buffer = bytes(CSV_STRING, encoding="utf-8")

        zip_content_mock = Mock()
        zip_content_mock.return_value = zip_content_mock
        zip_content_mock.decode.return_value = CSV_STRING

        zip_file_mock = MagicMock()
        zip_file_mock.return_value = zip_file_mock
        zip_file_mock.__enter__.return_value = zip_file_mock
        zip_file_mock.read.return_value = zip_content_mock

        zip_mock.return_value = zip_mock
        zip_mock.__enter__.return_value = zip_mock
        zip_mock.open.return_value = zip_file_mock
        zip_mock.infolist.return_value = [
            zipfile.ZipInfo("foo.bar"),
            zipfile.ZipInfo("FOO.CSV"),
            zipfile.ZipInfo("foo.baz"),
            zipfile.ZipInfo("bar.csv"),
        ]

        result = read_zip_csv(buffer, iterator=True)

        zip_mock.open.assert_called_once_with("FOO.CSV", "r")

        self.assertIsInstance(result, Iterator)
        self.assertEqual(list(result), CSV_LINES_DICT)

    @patch("zipfile.ZipFile")
    def test_read_zip_csv_failure(self, zip_mock):
        """Tests it fails reading a CSV from a Zip."""
        buffer = b"12345"

        zip_mock.return_value = zip_mock
        zip_mock.__enter__.return_value = zip_mock
        zip_mock.infolist.return_value = [
            zipfile.ZipInfo("foo.bar"),
            zipfile.ZipInfo("foo.baz"),
        ]

        self.assertRaises(FileNotFoundError, lambda: read_zip_csv(buffer))
        self.assertRaises(FileNotFoundError, lambda: read_zip_csv(buffer, "foo.csv"))
