"""Test the base class for reading and writing files."""
import unittest
from time import time
from unittest.mock import Mock, patch

from toolbox.files import FileManager

# pylint: disable=protected-access


class TestFileManager(unittest.TestCase):
    """Test suite for the base class for reading and writing files."""

    def test_construction_default(self):
        """Tests the construction of a file manager with default parameters."""
        file_path = "/root/folder/file"

        file = FileManager(file_path)

        self.assertEqual(file.filename, file_path)
        self.assertFalse(file.binary)
        self.assertIsNone(file.encoding)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {})

    def test_construction_text(self):
        """Tests the construction of a file manager for a text file."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        newline = "\n"

        file = FileManager(file_path, encoding=encoding, newline=newline)

        self.assertEqual(file.filename, file_path)
        self.assertFalse(file.binary)
        self.assertEqual(file.encoding, encoding)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {"newline": newline})

    def test_construction_binary(self):
        """Tests the construction of a file manager for a binary file."""
        file_path = "/root/folder/file"
        encoding = "ascii"

        file = FileManager(file_path, binary=True, encoding=encoding)

        self.assertEqual(file.filename, file_path)
        self.assertTrue(file.binary)
        self.assertIsNone(file.encoding)
        self.assertIsNone(file._file)
        self.assertEqual(file._open_args, {})

    @patch("builtins.open")
    def test_construction_open(self, mock_file_open):
        """Tests the construction of a file manager with opening."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        newline = "\n"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        with FileManager(
            file_path,
            read=True,
            encoding=encoding,
            newline=newline,
        ) as file:
            self.assertEqual(file.filename, file_path)
            self.assertFalse(file.binary)
            self.assertEqual(file.encoding, encoding)
            self.assertIs(file._file, mock_file)
            self.assertEqual(
                file._open_args,
                {
                    "newline": newline,
                },
            )

        mock_file_open.assert_called_once_with(
            file_path,
            mode="rt",
            encoding=encoding,
            newline=newline,
        )

    def test_dirname(self):
        """Tests that the folder path can be extracted."""
        file_path = "/root/folder/file.txt"

        file = FileManager(file_path)

        self.assertEqual(file.dirname, "/root/folder")

    def test_basename(self):
        """Tests that the file name can be extracted."""
        file_path = "/root/folder/file.txt"

        file = FileManager(file_path)

        self.assertEqual(file.basename, "file.txt")

    def test_name(self):
        """Tests that the file name without the extension can be extracted."""
        file_path = "/root/folder/file.txt"

        file = FileManager(file_path)

        self.assertEqual(file.name, "file")

    def test_extension(self):
        """Tests that the file extension can be extracted."""
        file_path = "/root/folder/file.txt"

        file = FileManager(file_path)

        self.assertEqual(file.ext, ".txt")

    def test_size(self):
        """Tests that the file size can be read."""
        file_path = "/root/folder/file"

        file = FileManager(file_path)
        size = 128

        # The file exists
        with patch("os.path.exists", return_value=True) as mock_exist:
            with patch("os.path.getsize", return_value=size) as mock_size:
                self.assertEqual(file.size, size)

                mock_exist.assert_called_once_with(file.filename)
                mock_size.assert_called_once_with(file.filename)

        # The file does not exist
        with patch("os.path.exists", return_value=False):
            with patch("os.path.getsize", return_value=size) as mock_size:
                self.assertEqual(file.size, 0)

                mock_exist.assert_called_once_with(file.filename)
                mock_size.assert_not_called()

    def test_date(self):
        """Tests that the file date can be read."""
        file_path = "/root/folder/file"

        file = FileManager(file_path)
        date = time() - 3600

        # The file exists
        with patch("os.path.exists", return_value=True) as mock_exist:
            with patch("os.path.getmtime", return_value=date) as mock_date:
                self.assertEqual(file.date, date)

                mock_exist.assert_called_once_with(file.filename)
                mock_date.assert_called_once_with(file.filename)

        # The file does not exist
        with patch("os.path.exists", return_value=False):
            with patch("os.path.getmtime", return_value=date) as mock_date:
                self.assertEqual(file.date, 0)

                mock_exist.assert_called_once_with(file.filename)
                mock_date.assert_not_called()

    def test_age(self):
        """Tests that the file age can be read."""
        file_path = "/root/folder/file"

        file = FileManager(file_path)
        age = 3600
        date = time() - age

        # The file exists
        with patch("os.path.exists", return_value=True) as mock_exist:
            with patch("os.path.getmtime", return_value=date) as mock_date:
                self.assertAlmostEqual(file.age, age, 0)

                mock_exist.assert_called_once_with(file.filename)
                mock_date.assert_called_once_with(file.filename)

        # The file does not exist
        with patch("os.path.exists", return_value=False):
            with patch("os.path.getmtime", return_value=date) as mock_date:
                self.assertEqual(file.age, 0)

                mock_exist.assert_called_once_with(file.filename)
                mock_date.assert_not_called()

    @patch("builtins.open")
    def test_open(self, mock_file_open):
        """Test a file can be opened."""
        file_path = "/root/folder/file"
        encoding = "ascii"
        newline = "\n"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path, encoding=encoding, newline=newline)

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

        file = FileManager(file_path)

        self.assertIs(file.open(create=True), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="wt",
            encoding=None,
        )

    @patch("builtins.open")
    def test_open_append(self, mock_file_open):
        """Test a file can be opened for writing."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path)

        self.assertIs(file.open(append=True), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="at",
            encoding=None,
        )

    @patch("builtins.open")
    def test_open_text(self, mock_file_open):
        """Test a file can be opened with text mode."""
        file_path = "/root/folder/file"
        encoding = "ascii"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path, encoding=encoding)

        self.assertIs(file.open(), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="rt",
            encoding=encoding,
        )

    @patch("builtins.open")
    def test_open_binary(self, mock_file_open):
        """Test a file can be opened with binary mode."""
        file_path = "/root/folder/file"
        encoding = "ascii"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path, binary=True, encoding=encoding)

        self.assertIs(file.open(), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="rb",
            encoding=None,
        )

    @patch("builtins.open")
    def test_open_close(self, mock_file_open):
        """Tests a file is closed before opening again."""
        file_path = "/root/folder/file"

        file = FileManager(file_path)

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

        file = FileManager(file_path)

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

        file = FileManager(file_path)

        with file.open():
            mock_file_open.assert_called_once()

        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_read_file(self, mock_file_open):
        """Tests a file can be read at once."""
        file_path = "/root/folder/file"
        content = "foo"
        encoding = "ascii"

        mock_file = Mock()
        mock_file.read = Mock(return_value=content)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path, encoding=encoding)

        self.assertEqual(file.read_file(), content)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="rt",
            encoding=encoding,
        )
        mock_file.read.assert_called_once()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_read_file_opened(self, mock_file_open):
        """Tests a file can be read at once even if file is already opened."""
        file_path = "/root/folder/file"
        content = "foo"

        mock_file = Mock()
        mock_file.read = Mock(return_value=content)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path)

        file.open()

        self.assertEqual(file.read_file(), content)

        mock_file_open.assert_called()
        mock_file.read.assert_called_once()
        mock_file.close.assert_called()

    @patch("builtins.open")
    def test_write_file(self, mock_file_open):
        """Tests a file can be written at once."""
        file_path = "/root/folder/file"
        content = "foo"
        encoding = "ascii"

        count = 4
        mock_file = Mock()
        mock_file.write = Mock(return_value=count)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path, encoding=encoding)

        self.assertEqual(file.write_file(content), count)

        mock_file_open.assert_called_once_with(
            file_path,
            mode="wt",
            encoding=encoding,
        )
        mock_file.write.assert_called_with(content)
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_write_file_opened(self, mock_file_open):
        """Tests a file can be written at once even if file is already opened."""
        file_path = "/root/folder/file"
        content = "foo"

        count = 4
        mock_file = Mock()
        mock_file.write = Mock(return_value=count)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path)

        file.open()

        self.assertEqual(file.write_file(content), count)

        mock_file_open.assert_called()
        mock_file.write.assert_called_with(content)
        mock_file.close.assert_called()

    @patch("builtins.open")
    def test_read(self, mock_file_open):
        """Tests a file can be read."""
        file_path = "/root/folder/file"
        content = "foo"

        mock_file = Mock()
        mock_file.read = Mock(side_effect=lambda: content)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path)

        self.assertRaises(ValueError, file.read)

        with file.open():
            self.assertEqual(file.read(), content)

            content = ""
            self.assertIsNone(file.read())

        mock_file_open.assert_called_once()
        mock_file.read.assert_called()
        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_write(self, mock_file_open):
        """Tests a file can be written."""
        file_path = "/root/folder/file"
        content = "foo"

        count = 4
        mock_file = Mock()
        mock_file.write = Mock(return_value=count)
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path)

        self.assertRaises(ValueError, lambda: file.write(content))

        with file.open(create=True):
            self.assertEqual(file.write(content), count)

        mock_file_open.assert_called_once()
        mock_file.write.assert_called_with(content)
        mock_file.close.assert_called_once()

    def test_exists(self):
        """Tests that the file exists."""
        file_path = "/root/folder/file"

        file = FileManager(file_path)

        # The file exists
        with patch("os.path.exists", return_value=True):
            self.assertTrue(file.exists())

        # The file does not exist
        with patch("os.path.exists", return_value=False):
            self.assertFalse(file.exists())

    def test_delete(self):
        """Tests that the file is deleted."""
        file_path = "/root/folder/file"

        file = FileManager(file_path)

        # Delete the file anyway
        with patch("os.remove") as mock:
            self.assertTrue(file.delete())
            mock.assert_called_once_with(file.filename)

        # Delete only if exist
        with patch("os.remove") as mock:
            # The file does not exist
            with patch("os.path.exists", return_value=False):
                self.assertFalse(file.delete(True))
                mock.assert_not_called()

            # The file exists
            with patch("os.path.exists", return_value=True):
                self.assertTrue(file.delete(True))
                mock.assert_called_once()

    def test_create_path(self):
        """Tests that the path to the file is created."""
        folder_path = "/root/folder"
        file_path = "/root/folder/file"

        file = FileManager(file_path)

        with patch("os.path.isdir", return_value=True) as mock:
            result = file.create_path()
            self.assertTrue(result)
            mock.assert_called_once_with(folder_path)

        with patch("os.path.isdir", return_value=False) as mock_isdir:
            with patch("os.makedirs") as mock_makedirs:
                result = file.create_path()
                self.assertTrue(result)
                mock_isdir.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)

        with patch("os.path.isdir", return_value=False) as mock_isdir:
            with patch("os.makedirs", side_effect=OSError("error")) as mock_makedirs:
                result = file.create_path()
                self.assertFalse(result)
                mock_isdir.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)

    @patch("builtins.open")
    def test_call(self, mock_file_open):
        """Test a file can be opened by calling the instance."""
        file_path = "/root/folder/file"
        encoding = "ascii"

        mock_file = Mock()
        mock_file_open.return_value = mock_file

        file = FileManager(file_path, binary=True, encoding=encoding)

        self.assertIs(file(create=True), file)

        self.assertIs(file._file, mock_file)

        mock_file_open.assert_called_once_with(file_path, mode="wb", encoding=None)

    @patch("builtins.open")
    def test_context(self, mock_file_open):
        """Tests an opened file is automatically closed."""
        file_path = "/root/folder/file"

        mock_file = Mock()
        mock_file.close = Mock()
        mock_file_open.return_value = mock_file

        with FileManager(file_path):
            mock_file_open.assert_called_once_with(
                file_path,
                mode="rt",
                encoding=None,
            )

        mock_file.close.assert_called_once()

    @patch("builtins.open")
    def test_iterator(self, mock_file_open):
        """Tests a file can be read as an iterable."""
        file_path = "/root/folder/file"
        content = "foo"
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

        file = FileManager(file_path)

        for value in file:
            self.assertEqual(value, content)

        mock_file_open.assert_called_once()
        mock_file.read.assert_called()
        mock_file.close.assert_called_once()

        mock_file_open.reset_mock()
        mock_file.reset_mock()

        index = 0
        self.assertEqual(list(file), [content])

        mock_file_open.assert_called_once()
        mock_file.read.assert_called()
        mock_file.close.assert_called_once()
