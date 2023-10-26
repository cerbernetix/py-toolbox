"""Test the collection of decorators for testing purpose."""
import unittest
from typing import Callable
from unittest.mock import Mock, patch

from cerbernetix.toolbox.testing import test_cases


class TestParameters(unittest.TestCase):
    """Test suite for the collection of decorators for testing purpose."""

    def test_test_case_decorator(self):
        """Test the test_case decorator."""
        cases = [{"title": "foo"}]
        decorator = test_cases(cases)

        self.assertIsInstance(decorator, Callable)
        mock_test = Mock()

        wrapper = decorator(mock_test)

        self.assertIsInstance(wrapper, Callable)

        with patch.object(self, "subTest") as sub_test_mock:
            wrapper(self)

            mock_test.assert_called_once_with(self, title="foo")
            sub_test_mock.assert_called_once_with("foo")

    def test_test_case_decorator_failure(self):
        """Test the test_case fails when parameters are wrong."""
        with patch.object(self, "subTest") as sub_test_mock:
            self.assertRaises(ValueError, lambda: test_cases("foo"))
            self.assertRaises(ValueError, lambda: test_cases([]))

            sub_test_mock.assert_not_called()

    @test_cases(
        [
            ["title", [], {"title": "foo"}, "foo"],
            ["message", [], {"message": "foo"}, "foo"],
            ["_", [], {"_": "foo"}, "foo"],
            ["default", [], {"bar": "foo"}, "case 0"],
            ["first", ["foo"], {}, "foo"],
            ["none", [None], {}, "case 0"],
        ]
    )
    def test_test_case_title(self, _, args, kwargs, title):
        """Test the test_case define a title."""

        with patch.object(self, "subTest") as sub_test_mock:
            decorator = test_cases([args or kwargs])
            mock_test = Mock()
            wrapper = decorator(mock_test)
            wrapper(self)

            mock_test.assert_called_once_with(self, *args, **kwargs)
            sub_test_mock.assert_called_once_with(title)

    @test_cases(
        [
            {
                "_": "named params",
                "first": {"answer": 32},
                "second": [1, 2, 3],
            },
            ["positioned params", {"answer": 32}, [1, 2, 3]],
        ]
    )
    def test_test_case_params(self, _, first, second):
        """Test the test_case receives data."""

        self.assertEqual(first, {"answer": 32})
        self.assertEqual(second, [1, 2, 3])

    @test_cases(["single param"])
    def test_test_case_single_params(self, param):
        """Test the test_case receives data."""

        self.assertEqual(param, "single param")
