"""Test the class for reading and writing pickle files."""
import pickle
import unittest
from typing import Iterator
from unittest.mock import Mock, mock_open, patch

from cerbernetix.toolbox.files import PickleFile
from cerbernetix.toolbox.files.pickle_file import read_pickle_file, write_pickle_file

# pylint: disable=protected-access

DATA_STRING = "foo"
DATA_DICT = {"name": "test", "level": 20, "keywords": ["one", "two"], "enabled": True}
DATA_LIST = [
    {"first_name": "John", "last_name": "Smith", "age": "18", "city": "London"},
    {"first_name": "Jane", "last_name": "Doe", "age": "20", "city": "Paris"},
]


class TestPickleFile(unittest.TestCase):
    """Test suite for the class for reading and writing pickle files."""

    def test_construction_default(self):
        """
        Tests the construction of a pickle file manager with default parameters
        """
        file_path = "/root/folder/file"

        file = PickleFile(file_path)

        self.assertEqual(file.filename, file_path)
        self.assertTrue(file.binary)
        self.assertIsNone(file.encoding)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {})
        self.assertEqual(file._reader_args, {})
        self.assertEqual(file._writer_args, {})

    def test_construction_params(self):
        """Tests the construction of a pickle file manager with specific parameters."""
        file_path = "/root/folder/file"
        buffering = 100
        protocol = 3
        fix_imports = False

        file = PickleFile(
            file_path,
            buffering=buffering,
            protocol=protocol,
            fix_imports=fix_imports,
        )

        self.assertEqual(file.filename, file_path)
        self.assertTrue(file.binary)
        self.assertIsNone(file.encoding)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {"buffering": buffering})
        self.assertEqual(
            file._reader_args,
            {
                "fix_imports": fix_imports,
            },
        )
        self.assertEqual(
            file._writer_args,
            {
                "protocol": protocol,
                "fix_imports": fix_imports,
            },
        )

    @patch("builtins.open")
    def test_construction_open(self, mock_file_open):
        """Tests the construction of a pickle file manager with opening."""
        file_path = "/root/folder/file"
        encoding = "ascii"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        with PickleFile(
            file_path,
            read=True,
            encoding=encoding,
        ) as file:
            self.assertEqual(file.filename, file_path)
            self.assertTrue(file.binary)
            self.assertIsNone(file.encoding)
            self.assertIs(file._file, mock_file)
            self.assertEqual(file._open_args, {})
            self.assertEqual(file._reader_args, {"encoding": encoding})
            self.assertEqual(file._writer_args, {})

        mock_file_open.assert_called_once_with(
            file_path,
            mode="rb",
            encoding=None,
        )

    @patch("builtins.open")
    def test_open(self, mock_file_open):
        """Test a file can be opened."""
        file_path = "/root/folder/file"
        encoding = "ascii"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = PickleFile(file_path, encoding=encoding)

        self.assertIs(file.open(), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="rb",
            encoding=None,
        )

    @patch("builtins.open")
    def test_open_create(self, mock_file_open):
        """Test a file can be opened for writing."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = PickleFile(file_path)

        self.assertIs(file.open(create=True), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="wb",
            encoding=None,
        )

    @patch("builtins.open")
    def test_open_close(self, mock_file_open):
        """Tests a file is closed before opening again."""
        file_path = "/root/folder/file"

        file = PickleFile(file_path)

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

        file = PickleFile(file_path)

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

        file = PickleFile(file_path)

        with file.open():
            mock_file_open.assert_called_once()

        mock_file.close.assert_called_once()

    def test_read_file(self):
        """Tests a file can be read at once."""
        file_path = "/root/folder/file"
        data = pickle.dumps(DATA_DICT) + pickle.dumps(DATA_LIST) + pickle.dumps(DATA_STRING)
        expected = [DATA_DICT, DATA_LIST, DATA_STRING]

        with patch("builtins.open", mock_open(read_data=data)) as mock_file_open:
            file = PickleFile(file_path)

            result = file.read_file()
            self.assertIsInstance(result, list)
            self.assertEqual(result, expected)

            mock_file_open.assert_called_once()

    def test_read_file_iterator(self):
        """Tests a file can be read at once using an iterator."""
        file_path = "/root/folder/file"
        data = pickle.dumps(DATA_DICT) + pickle.dumps(DATA_LIST) + pickle.dumps(DATA_STRING)
        expected = [DATA_DICT, DATA_LIST, DATA_STRING]

        with patch("builtins.open", mock_open(read_data=data)) as mock_file_open:
            file = PickleFile(file_path)

            result = file.read_file(iterator=True)
            self.assertIsInstance(result, Iterator)
            self.assertEqual(list(result), expected)

            mock_file_open.assert_called_once()

    def test_write_file(self):
        """Tests a file can be written at once."""
        file_path = "/root/folder/file"

        data = [DATA_DICT, DATA_LIST, DATA_STRING]
        expected = pickle.dumps(DATA_DICT) + pickle.dumps(DATA_LIST) + pickle.dumps(DATA_STRING)

        with patch("builtins.open", mock_open()) as mock_file_open:
            written = None

            def write(obj):
                nonlocal written
                if written is None:
                    written = obj
                else:
                    written += obj
                return len(obj)

            mock_write = Mock(side_effect=write)
            mock_file_open.return_value.write = mock_write

            file = PickleFile(file_path)

            self.assertEqual(
                file.write_file(data),
                len(expected),
            )

            self.assertEqual(written, expected)

            mock_file_open.assert_called_once()

    @patch("builtins.open")
    def test_read(self, mock_file_open):
        """Tests a file can be read line by line."""
        file_path = "/root/folder/file"

        data = pickle.dumps(DATA_STRING) + pickle.dumps(DATA_LIST) + pickle.dumps(DATA_DICT)
        expected = [DATA_STRING, DATA_LIST, DATA_DICT]

        with patch("builtins.open", mock_open(read_data=data)) as mock_file_open:
            file = PickleFile(file_path)

            self.assertRaises(ValueError, file.read)

            with file.open():
                for obj in expected:
                    self.assertEqual(file.read(), obj)

                self.assertIsNone(file.read())

            mock_file_open.assert_called_once()

    @patch("builtins.open")
    def test_write(self, mock_file_open):
        """Tests a file can be written line by line."""
        file_path = "/root/folder/file"

        data = [DATA_STRING, DATA_DICT, DATA_LIST]
        expected = pickle.dumps(DATA_STRING) + pickle.dumps(DATA_DICT) + pickle.dumps(DATA_LIST)

        with patch("builtins.open", mock_open()) as mock_file_open:
            written = None

            def write(obj):
                nonlocal written
                if written is None:
                    written = obj
                else:
                    written += obj
                return len(obj)

            mock_write = Mock(side_effect=write)
            mock_file_open.return_value.write = mock_write

            file = PickleFile(file_path)

            self.assertRaises(ValueError, lambda: file.write(data[0]))

            with file.open():
                for obj in data:
                    file.write(obj)

            self.assertEqual(written, expected)

            mock_file_open.assert_called_once()

    @patch("builtins.open")
    def test_call(self, mock_file_open):
        """Test a file can be opened by calling the instance."""
        file_path = "/root/folder/file"
        encoding = "ascii"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = PickleFile(file_path, encoding=encoding)

        self.assertIs(file(), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(file_path, mode="rb", encoding=None)

    @patch("builtins.open")
    def test_context(self, mock_file_open):
        """Tests an opened file is automatically closed."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        with PickleFile(file_path):
            mock_file_open.assert_called_once_with(
                file_path,
                mode="rb",
                encoding=None,
            )

        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_iterator(self, mock_file_open):
        """Tests a file can be read as an iterable."""
        file_path = "/root/folder/file"

        data = pickle.dumps(DATA_DICT) + pickle.dumps(DATA_LIST) + pickle.dumps(DATA_STRING)
        expected = [DATA_DICT, DATA_LIST, DATA_STRING]

        with patch("builtins.open", mock_open(read_data=data)) as mock_file_open:
            file = PickleFile(file_path)

            for idx, value in enumerate(file):
                self.assertEqual(value, expected[idx])

            mock_file_open.assert_called_once()

            mock_file_open.reset_mock()

            self.assertEqual(list(file), expected)

            mock_file_open.assert_called_once()


class TestPickleFileHelpers(unittest.TestCase):
    """Test suite for the pickle file helpers."""

    @patch("builtins.open")
    def test_read_pickle_file(self, mock_file_open):
        """Tests a pickle file can be read at once."""
        file_path = "/root/folder/file"
        data = pickle.dumps(DATA_DICT) + pickle.dumps(DATA_LIST) + pickle.dumps(DATA_STRING)
        expected = [DATA_DICT, DATA_LIST, DATA_STRING]

        with patch("builtins.open", mock_open(read_data=data)) as mock_file_open:
            result = read_pickle_file(file_path)
            self.assertIsInstance(result, list)
            self.assertEqual(result, expected)

            mock_file_open.assert_called_once()

    @patch("builtins.open")
    def test_read_pickle_file_iterator(self, mock_file_open):
        """Tests a pickle file can be read at once using an iterator."""
        file_path = "/root/folder/file"
        data = pickle.dumps(DATA_DICT) + pickle.dumps(DATA_LIST) + pickle.dumps(DATA_STRING)
        expected = [DATA_DICT, DATA_LIST, DATA_STRING]

        with patch("builtins.open", mock_open(read_data=data)) as mock_file_open:
            result = read_pickle_file(file_path, iterator=True)
            self.assertIsInstance(result, Iterator)
            self.assertEqual(list(result), expected)

            mock_file_open.assert_called_once()

    @patch("builtins.open")
    def test_write_pickle_file(self, mock_file_open):
        """Tests a pickle file can be written at once."""
        file_path = "/root/folder/file"

        data = [DATA_DICT, DATA_LIST, DATA_STRING]
        expected = pickle.dumps(DATA_DICT) + pickle.dumps(DATA_LIST) + pickle.dumps(DATA_STRING)

        with patch("builtins.open", mock_open()) as mock_file_open:
            file = None

            def write(obj):
                nonlocal file
                if file is None:
                    file = obj
                else:
                    file += obj
                return len(obj)

            mock_write = Mock(side_effect=write)
            mock_file_open.return_value.write = mock_write

            self.assertEqual(write_pickle_file(file_path, data), len(expected))

            self.assertEqual(file, expected)

            mock_file_open.assert_called_once()
