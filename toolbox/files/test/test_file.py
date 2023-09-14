"""Test the utilities for accessing files."""
import unittest
import zipfile
from unittest.mock import MagicMock, Mock, patch

import requests

from toolbox.files import (
    fetch_content,
    get_file_mode,
    read_file,
    read_zip_file,
    write_file,
)
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

    @test_cases(
        [
            [
                "default",
                "http://example.com/data",
                {},
                {"url": "http://example.com/data", "timeout": (6, 30)},
                b"0123456789ABCDEF",
                "0123456789ABCDEF",
                "0123456789ABCDEF",
            ],
            [
                "binary",
                "http://example.com/data",
                {"binary": True},
                {"url": "http://example.com/data", "timeout": (6, 30)},
                b"0123456789ABCDEF",
                "0123456789ABCDEF",
                b"0123456789ABCDEF",
            ],
            [
                "timeout",
                "http://example.com/data",
                {"timeout": 10},
                {"url": "http://example.com/data", "timeout": 10},
                b"0123456789ABCDEF",
                "0123456789ABCDEF",
                "0123456789ABCDEF",
            ],
            [
                "other params",
                "http://example.com/data",
                {"params": {}},
                {"url": "http://example.com/data", "timeout": (6, 30), "params": {}},
                b"0123456789ABCDEF",
                "0123456789ABCDEF",
                "0123456789ABCDEF",
            ],
        ]
    )
    @patch("requests.get")
    def test_fetch_content(
        self, _, url, params, called_with, content, text, expected, mock_request
    ):
        """Tests that a content can be fetched."""
        mock_response = Mock()
        mock_response.content = content
        mock_response.text = text
        mock_request.return_value = mock_response

        result = fetch_content(url, **params)

        self.assertEqual(result, expected)
        mock_request.assert_called_with(**called_with)

    @patch("requests.get")
    def test_fetch_content_failure(self, mock_request):
        """Tests that fetching a content can raise error."""
        url = "http://example.com/data"

        mock_response = Mock()
        mock_response.raise_for_status = Mock(side_effect=requests.HTTPError("foo"))
        mock_request.return_value = mock_response

        self.assertRaises(requests.HTTPError, lambda: fetch_content(url))

    @test_cases(
        [
            ["default", {}, "foo.bar"],
            ["filename given", {"filename": "bar.txt"}, "bar.txt"],
            ["extension given", {"ext": ".txt"}, "FOO.TXT"],
        ]
    )
    @patch("zipfile.ZipFile")
    def test_read_zip_file(self, _, params, filename, zip_mock):
        """Tests it reads a file from a Zip."""
        content = "0123456789ABCDEF"
        buffer = bytes(content, encoding="utf-8")

        zip_file_mock = MagicMock()
        zip_file_mock.return_value = zip_file_mock
        zip_file_mock.__enter__.return_value = zip_file_mock
        zip_file_mock.read.return_value = content

        zip_mock.return_value = zip_mock
        zip_mock.__enter__.return_value = zip_mock
        zip_mock.open.return_value = zip_file_mock
        zip_mock.infolist.return_value = [
            zipfile.ZipInfo("foo.bar"),
            zipfile.ZipInfo("FOO.TXT"),
            zipfile.ZipInfo("foo.baz"),
            zipfile.ZipInfo("bar.txt"),
        ]

        result = read_zip_file(buffer, **params)

        zip_mock.open.assert_called_once_with(filename, "r")

        self.assertEqual(result, content)

    @patch("zipfile.ZipFile")
    def test_read_zip_file_failure(self, zip_mock):
        """Tests it fails reading a file from a Zip."""
        buffer = b"12345"

        zip_mock.return_value = zip_mock
        zip_mock.__enter__.return_value = zip_mock
        zip_mock.infolist.return_value = [
            zipfile.ZipInfo("foo.bar"),
            zipfile.ZipInfo("foo.baz"),
        ]

        self.assertRaises(
            FileNotFoundError, lambda: read_zip_file(buffer, filename="foo.txt")
        )
        self.assertRaises(FileNotFoundError, lambda: read_zip_file(buffer, ext=".tx"))
