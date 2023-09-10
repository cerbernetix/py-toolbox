"""Test the class for reading and writing JSON files."""
import unittest
from unittest.mock import Mock, patch

from toolbox.files import (
    JSON_ENCODING,
    JSON_INDENT,
    JSONFile,
    read_json_file,
    write_json_file,
)

JSON_DATA = {"name": "test", "level": 20, "keywords": ["one", "two"], "enabled": True}
JSON_STRING = """{
    "enabled": true,
    "keywords": [
        "one",
        "two"
    ],
    "level": 20,
    "name": "test"
}"""

# pylint: disable=protected-access


class TestJSONFile(unittest.TestCase):
    """Test suite for the class for reading and writing JSON files."""

    def test_construction_default(self):
        """Tests the construction of a JSON file manager with default parameters."""
        file_path = "/root/folder/file"

        file = JSONFile(file_path)

        self.assertEqual(file.filename, file_path)
        self.assertFalse(file.binary)
        self.assertEqual(file.indent, JSON_INDENT)
        self.assertEqual(file.encoding, JSON_ENCODING)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {})

    def test_construction_params(self):
        """Tests the construction of a JSON file manager with specific parameters."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        indent = 2
        newline = "\n"

        file = JSONFile(file_path, encoding=encoding, indent=indent, newline=newline)

        self.assertEqual(file.filename, file_path)
        self.assertFalse(file.binary)
        self.assertEqual(file.indent, indent)
        self.assertEqual(file.encoding, encoding)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {"newline": newline})

    @patch("builtins.open")
    def test_construction_open(self, mock_file_open):
        """Tests the construction of a JSON file manager with opening."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        indent = 2
        newline = "\n"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        with JSONFile(
            file_path,
            read=True,
            encoding=encoding,
            indent=indent,
            newline=newline,
        ) as file:
            self.assertEqual(file.filename, file_path)
            self.assertFalse(file.binary)
            self.assertEqual(file.encoding, encoding)
            self.assertEqual(file.indent, indent)
            self.assertIs(file._file, mock_file)
            self.assertEqual(file._open_args, {"newline": newline})

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
        newline = "\n"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = JSONFile(file_path, encoding=encoding, newline=newline)

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

        file = JSONFile(file_path)

        self.assertIs(file.open(create=True), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="wt",
            encoding=JSON_ENCODING,
        )

    @patch("builtins.open")
    def test_open_close(self, mock_file_open):
        """Tests a file is closed before opening again."""
        file_path = "/root/folder/file"

        file = JSONFile(file_path)

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

        file = JSONFile(file_path)

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

        file = JSONFile(file_path)

        with file.open():
            mock_file_open.assert_called_once()

        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_read_file(self, mock_file_open):
        """Tests a file can be read at once."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file.read = Mock(return_value=JSON_STRING)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = JSONFile(file_path)

        self.assertEqual(file.read_file(), JSON_DATA)

        mock_file_open.assert_called_once()
        mock_file.read.assert_called_once()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_write_file(self, mock_file_open):
        """Tests a file can be written at once."""
        file_path = "/root/folder/file"

        count = len(JSON_STRING)
        mock_file = Mock()
        mock_file.write = Mock(return_value=count)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = JSONFile(file_path)

        self.assertEqual(file.write_file(JSON_DATA), count)

        mock_file_open.assert_called_once()
        mock_file.write.assert_called_with(JSON_STRING)
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_read(self, mock_file_open):
        """Tests a file can be read."""
        file_path = "/root/folder/file"
        content = JSON_STRING

        mock_file = Mock()
        mock_file.read = Mock(side_effect=lambda: content)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = JSONFile(file_path)

        self.assertRaises(ValueError, file.read)

        with file.open():
            self.assertEqual(file.read(), JSON_DATA)

            content = ""
            self.assertIsNone(file.read())

        mock_file_open.assert_called_once()
        mock_file.read.assert_called()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_write(self, mock_file_open):
        """Tests a file can be written."""
        file_path = "/root/folder/file"

        count = len(JSON_STRING)
        mock_file = Mock()
        mock_file.write = Mock(return_value=count)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = JSONFile(file_path)

        self.assertRaises(ValueError, lambda: file.write(JSON_DATA))

        with file.open(create=True):
            self.assertEqual(file.write(JSON_DATA), count)

        mock_file_open.assert_called_once()
        mock_file.write.assert_called_with(JSON_STRING)
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_call(self, mock_file_open):
        """Test a file can be opened by calling the instance."""
        file_path = "/root/folder/file"
        encoding = "ascii"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = JSONFile(file_path, encoding=encoding)

        self.assertIs(file(create=True), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(file_path, mode="wt", encoding=encoding)

    @patch("builtins.open")
    def test_context(self, mock_file_open):
        """Tests an opened file is automatically closed."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        with JSONFile(file_path):
            mock_file_open.assert_called_once_with(
                file_path,
                mode="rt",
                encoding=JSON_ENCODING,
            )

        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_iterator(self, mock_file_open):
        """Tests a file can be read as an iterable."""
        file_path = "/root/folder/file"
        content = JSON_STRING
        count = 1
        index = 0

        def read():
            nonlocal index
            index += 1

            if index <= count:
                return content

            return ""

        mock_file = Mock()
        mock_file.read = Mock(side_effect=read)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = JSONFile(file_path)

        for value in file:
            self.assertEqual(value, JSON_DATA)

        mock_file_open.assert_called_once()
        mock_file.read.assert_called()
        mock_file.close.assert_called_once()

        mock_file_open.reset_mock()
        mock_file.reset_mock()

        index = 0
        self.assertEqual(list(file), [JSON_DATA])

        mock_file_open.assert_called_once()
        mock_file.read.assert_called()
        mock_file.close.assert_called_once()


class TestJSONFileHelpers(unittest.TestCase):
    """Test suite for the JSON file helpers."""

    @patch("builtins.open")
    def test_read_json_file(self, mock_file_open):
        """Tests a JSON file can be read at once."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file.read = Mock(return_value=JSON_STRING)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        self.assertEqual(read_json_file(file_path), JSON_DATA)

        mock_file_open.assert_called_once()
        mock_file.read.assert_called_once()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_write_json_file(self, mock_file_open):
        """Tests a JSON file can be written at once."""
        file_path = "/root/folder/file"

        count = len(JSON_STRING)
        mock_file = Mock()
        mock_file.write = Mock(return_value=count)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        self.assertEqual(write_json_file(file_path, JSON_DATA), count)

        mock_file_open.assert_called_once()
        mock_file.write.assert_called_with(JSON_STRING)
        mock_file.close.assert_called_once()
