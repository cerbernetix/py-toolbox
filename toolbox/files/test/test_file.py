"""Test the utilities for accessing files."""
import unittest
from unittest.mock import Mock, patch

from toolbox.files import get_file_mode, read_file, write_file
from toolbox.testing import test_cases


class TestFileHelpers(unittest.TestCase):
    """Test suite for the file helpers."""

    @test_cases(
        [
            ["default", {}, "rt"],
            ["create", {"create": True}, "wt"],
            ["create and read", {"create": True, "read": True}, "w+t"],
            ["append", {"append": True}, "at"],
            ["append and read", {"append": True, "read": True}, "a+t"],
            ["read and write", {"write": True}, "r+t"],
            ["read a binary file", {"binary": True}, "rb"],
            ["create a binary file", {"create": True, "binary": True}, "wb"],
            ["append to a binary file", {"append": True, "binary": True}, "ab"],
            ["read and write a binary file", {"write": True, "binary": True}, "r+b"],
            [
                "create and read a binary file",
                {"create": True, "read": True, "binary": True},
                "w+b",
            ],
            [
                "append and read a binary file",
                {"append": True, "read": True, "binary": True},
                "a+b",
            ],
        ]
    )
    def test_get_file_mode(self, _, params, expected):
        """Tests the helper get_file_mode()."""

        self.assertEqual(
            get_file_mode(**params),
            expected,
        )

    @test_cases(
        [
            ["default", {}, {"mode": "rt", "encoding": None}],
            [
                "text",
                {"binary": False, "encoding": "ascii", "newline": "\n"},
                {"mode": "rt", "encoding": "ascii", "newline": "\n"},
            ],
            ["binary", {"binary": True}, {"mode": "rb", "encoding": None}],
            [
                "params",
                {"encoding": "ascii", "newline": "\n", "buffer": 100},
                {"mode": "rt", "encoding": "ascii", "newline": "\n", "buffer": 100},
            ],
        ]
    )
    def test_read_file(self, _, params, open_params):
        """Tests a file can be read at once."""
        file_path = "/root/folder/file"
        content = "foo"

        with patch("builtins.open") as mock_file_open:
            mock_file = Mock()
            mock_file.read = Mock(return_value=content)
            mock_file_open.return_value.__enter__.return_value = mock_file

            self.assertEqual(
                read_file(file_path, **params),
                content,
            )

            mock_file_open.assert_called_with(file_path, **open_params)
            mock_file.read.assert_called_once()

    @test_cases(
        [
            ["default", {}, {"mode": "wt", "encoding": None}],
            [
                "text",
                {"binary": False, "encoding": "ascii", "newline": "\n"},
                {"mode": "wt", "encoding": "ascii", "newline": "\n"},
            ],
            ["binary", {"binary": True}, {"mode": "wb", "encoding": None}],
            [
                "params",
                {"encoding": "ascii", "newline": "\n", "buffer": 100},
                {"mode": "wt", "encoding": "ascii", "newline": "\n", "buffer": 100},
            ],
        ]
    )
    def test_write_file(self, _, params, open_params):
        """Tests that a file can be written."""
        file_path = "/root/folder/file"
        content = "foo"
        count = len(content)

        with patch("builtins.open") as mock_file_open:
            mock_file = Mock()
            mock_file.write = Mock(return_value=count)
            mock_file_open.return_value.__enter__.return_value = mock_file

            self.assertEqual(
                write_file(file_path, content, **params),
                count,
            )

            mock_file_open.assert_called_with(file_path, **open_params)
            mock_file.write.assert_called_with(content)
