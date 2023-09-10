"""
Test the utilities for accessing files.
"""
import unittest
from unittest.mock import Mock, patch

from toolbox.files import get_file_mode, read_file, write_file


class TestFileHelpers(unittest.TestCase):
    """
    Test suite for the file helpers.
    """

    def test_get_file_mode(self):
        """
        Tests the helper get_file_mode()
        """
        test_cases = [
            {
                "message": "default",
                "params": {},
                "expected": "rt",
            },
            {
                "message": "create",
                "params": {
                    "create": True,
                },
                "expected": "wt",
            },
            {
                "message": "create and read",
                "params": {
                    "create": True,
                    "read": True,
                },
                "expected": "w+t",
            },
            {
                "message": "append",
                "params": {
                    "append": True,
                },
                "expected": "at",
            },
            {
                "message": "append and read",
                "params": {
                    "append": True,
                    "read": True,
                },
                "expected": "a+t",
            },
            {
                "message": "read and write",
                "params": {
                    "write": True,
                },
                "expected": "r+t",
            },
            {
                "message": "read a binary file",
                "params": {
                    "binary": True,
                },
                "expected": "rb",
            },
            {
                "message": "create a binary file",
                "params": {
                    "create": True,
                    "binary": True,
                },
                "expected": "wb",
            },
            {
                "message": "append to a binary file",
                "params": {
                    "append": True,
                    "binary": True,
                },
                "expected": "ab",
            },
            {
                "message": "read and write a binary file",
                "params": {
                    "write": True,
                    "binary": True,
                },
                "expected": "r+b",
            },
            {
                "message": "create and read a binary file",
                "params": {
                    "create": True,
                    "read": True,
                    "binary": True,
                },
                "expected": "w+b",
            },
            {
                "message": "append and read a binary file",
                "params": {
                    "append": True,
                    "read": True,
                    "binary": True,
                },
                "expected": "a+b",
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case.get("message")):
                self.assertEqual(
                    get_file_mode(**test_case.get("params")),
                    test_case.get("expected"),
                )

    def test_read_file(self):
        """
        Tests a file can be read at once
        """
        file_path = "/root/folder/file"
        content = "foo"

        test_cases = [
            {
                "message": "default",
                "params": {},
                "expected": {
                    "mode": "rt",
                    "encoding": None,
                },
                "result": content,
            },
            {
                "message": "text",
                "params": {
                    "binary": False,
                    "encoding": "ascii",
                    "newline": "\n",
                },
                "expected": {
                    "mode": "rt",
                    "encoding": "ascii",
                    "newline": "\n",
                },
                "result": content,
            },
            {
                "message": "binary",
                "params": {
                    "binary": True,
                },
                "expected": {
                    "mode": "rb",
                    "encoding": None,
                },
                "result": content,
            },
            {
                "message": "params",
                "params": {
                    "encoding": "ascii",
                    "newline": "\n",
                    "buffer": 100,
                },
                "expected": {
                    "mode": "rt",
                    "encoding": "ascii",
                    "newline": "\n",
                    "buffer": 100,
                },
                "result": content,
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case.get("message")):
                with patch("builtins.open") as mock_file_open:
                    mock_file = Mock()
                    mock_file.read = Mock(return_value=content)
                    mock_file_open.return_value.__enter__.return_value = mock_file

                    self.assertEqual(
                        read_file(file_path, **test_case.get("params")), content
                    )

                    mock_file_open.assert_called_with(
                        file_path, **test_case.get("expected")
                    )
                    mock_file.read.assert_called_once()

    def test_write_file(self):
        """
        Tests that a file can be written
        """
        file_path = "/root/folder/file"
        content = "foo"
        count = 4

        test_cases = [
            {
                "message": "default",
                "params": {},
                "expected": {
                    "mode": "wt",
                    "encoding": None,
                },
                "result": content,
            },
            {
                "message": "text",
                "params": {
                    "binary": False,
                    "encoding": "ascii",
                    "newline": "\n",
                },
                "expected": {
                    "mode": "wt",
                    "encoding": "ascii",
                    "newline": "\n",
                },
                "result": content,
            },
            {
                "message": "binary",
                "params": {
                    "binary": True,
                },
                "expected": {
                    "mode": "wb",
                    "encoding": None,
                },
                "result": content,
            },
            {
                "message": "params",
                "params": {
                    "encoding": "ascii",
                    "newline": "\n",
                    "buffer": 100,
                },
                "expected": {
                    "mode": "wt",
                    "encoding": "ascii",
                    "newline": "\n",
                    "buffer": 100,
                },
                "result": content,
            },
        ]

        for test_case in test_cases:
            with self.subTest(test_case.get("message")):
                with patch("builtins.open") as mock_file_open:
                    mock_file = Mock()
                    mock_file.write = Mock(return_value=count)
                    mock_file_open.return_value.__enter__.return_value = mock_file

                    self.assertEqual(
                        write_file(file_path, content, **test_case.get("params")), count
                    )

                    mock_file_open.assert_called_with(
                        file_path, **test_case.get("expected")
                    )
                    mock_file.write.assert_called_with(content)
