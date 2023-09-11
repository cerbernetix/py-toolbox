"""Test the collection of utilities around file paths."""
import sys
import unittest
from pathlib import PurePath
from unittest.mock import Mock, patch

from toolbox.files import path


class TestFilePaths(unittest.TestCase):
    """Test suite for the file path helpers."""

    def test_get_module_path(self):
        """
        Tests the helper get_module_path().
        """
        mock_namespace = "app.package.module"
        mock_path = "/root/app/package/module.py"
        mock_folder = "/root/app/package"

        module_mock = Mock()
        module_mock.__file__ = mock_path
        module_mock.__path__ = mock_folder

        with patch.dict(sys.modules, {mock_namespace: module_mock}):
            result = path.get_module_path(mock_namespace)
            self.assertIsInstance(result, PurePath)
            self.assertEqual(str(result), mock_path)

        result = path.get_module_path("foo")
        self.assertIsInstance(result, PurePath)
        self.assertEqual(str(result), ".")

    def test_get_module_folder(self):
        """Tests the helper get_module_folder()."""
        mock_namespace = "app.package.module"
        mock_path = "/root/app/package/module.py"
        mock_folder = "/root/app/package"

        module_mock = Mock()
        module_mock.__file__ = mock_path
        module_mock.__path__ = mock_folder

        with patch.dict(sys.modules, {mock_namespace: module_mock}):
            result = path.get_module_folder_path(mock_namespace)
            self.assertIsInstance(result, PurePath)
            self.assertEqual(str(result), mock_folder)

        result = path.get_module_folder_path("foo")
        self.assertIsInstance(result, PurePath)
        self.assertEqual(str(result), ".")

    def test_get_application_path(self):
        """Tests the helper get_application_path()."""
        mock_namespace = "app"
        mock_path = "/root/app/package/module.py"
        mock_folder = "/root/app/package"
        mock_root = "/root/app"

        module_mock = Mock()
        module_mock.__file__ = mock_path
        module_mock.__path__ = mock_folder

        with patch.dict(sys.modules, {mock_namespace: module_mock}):
            result = path.get_application_path(mock_namespace)
            self.assertIsInstance(result, PurePath)
            self.assertEqual(str(result), mock_root)

        result = path.get_application_path("foo")
        self.assertIsInstance(result, PurePath)
        self.assertEqual(str(result), ".")

    def test_get_application_name(self):
        """Tests the helper get_application_name()."""
        mock_namespace = "app"
        mock_path = "/root/app/package/module.py"
        mock_folder = "/root/app/package"
        mock_name = "app"

        module_mock = Mock()
        module_mock.__file__ = mock_path
        module_mock.__path__ = mock_folder

        with patch.dict(sys.modules, {mock_namespace: module_mock}):
            result = path.get_application_name(mock_namespace)
            self.assertIsInstance(result, str)
            self.assertEqual(result, mock_name)

        result = path.get_application_name("foo")
        self.assertEqual(result, "")

    def test_get_file_path(self):
        """Tests the helper get_file_path()."""
        mock_namespace = "app"
        mock_path = "/root/app/package/module.py"
        mock_folder = "/root/app/package"
        mock_root = "/root/app"
        file_path = "subfolder/file"

        module_mock = Mock()
        module_mock.__file__ = mock_path
        module_mock.__path__ = mock_folder

        with patch.dict(sys.modules, {mock_namespace: module_mock}):
            result = path.get_file_path(file_path, mock_namespace)
            self.assertIsInstance(result, PurePath)
            self.assertEqual(str(result), f"{mock_root}/{file_path}")

        result = path.get_file_path(file_path, "foo")
        self.assertIsInstance(result, PurePath)
        self.assertEqual(str(result), file_path)

    def test_create_file_path(self):
        """Test the helper create_file_path()."""
        folder_path = "/root/folder"
        file_path = "/root/folder/file"

        with patch("os.path.isdir", return_value=True) as mock:
            result = path.create_file_path(file_path)
            self.assertTrue(result)
            mock.assert_called_once_with(folder_path)

        with patch("os.path.isdir", return_value=False) as mock_isdir:
            with patch("os.makedirs") as mock_makedirs:
                result = path.create_file_path(file_path)
                self.assertTrue(result)
                mock_isdir.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)

        with patch("os.path.isdir", return_value=False) as mock_isdir:
            with patch("os.makedirs", side_effect=OSError("error")) as mock_makedirs:
                result = path.create_file_path(file_path)
                self.assertFalse(result)
                mock_isdir.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)
                mock_makedirs.assert_called_once_with(folder_path)

    def test_delete_path_file(self):
        """Tests the helper delete_path() for deleting a file."""
        file_path = "/root/folder/file"

        with patch("os.path.isdir", return_value=False):
            with patch("os.remove") as mock:
                result = path.delete_path(file_path)
                self.assertTrue(result)
                mock.assert_called_once_with(file_path)

            with patch("os.remove", side_effect=OSError("error")) as mock:
                result = path.delete_path(file_path)
                self.assertFalse(result)
                mock.assert_called_once_with(file_path)

            with patch("os.remove", side_effect=FileNotFoundError("error")) as mock:
                result = path.delete_path(file_path)
                self.assertFalse(result)
                mock.assert_called_once_with(file_path)

    def test_delete_path_folder(self):
        """Tests the helper delete_path() for deleting a folder."""
        file_path = "/root/folder/subfolder"

        with patch("os.path.isdir", return_value=True):
            with patch("os.rmdir") as mock:
                result = path.delete_path(file_path)
                self.assertTrue(result)
                mock.assert_called_once_with(file_path)

            with patch("os.rmdir", side_effect=OSError("error")) as mock:
                result = path.delete_path(file_path)
                self.assertFalse(result)
                mock.assert_called_once_with(file_path)

            with patch("os.rmdir", side_effect=FileNotFoundError("error")) as mock:
                result = path.delete_path(file_path)
                self.assertFalse(result)
                mock.assert_called_once_with(file_path)
