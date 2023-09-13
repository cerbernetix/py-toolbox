"""Test the collection of data mappers."""
import unittest

from toolbox.data import boolean, passthrough
from toolbox.testing import test_cases


class TestDataMappers(unittest.TestCase):
    """Test suite for the collection of data mappers."""

    @test_cases(
        [
            ["None", None, None],
            ["string", "foo", "foo"],
            ["int", 42, 42],
            ["float", 3.14, 3.14],
            ["list", [1, 2, 3], [1, 2, 3]],
            ["dict", {"a": 1, "b": 2}, {"a": 1, "b": 2}],
            ["set", {1, 2, 3}, {1, 2, 3}],
        ]
    )
    def test_passthrough(self, _, value_set, value_get):
        """Test the value is returned as it is."""
        self.assertEqual(passthrough(value_set), value_get)

    @test_cases(
        [
            # False values
            [None, False],
            [False, False],
            ["false", False],
            ["False", False],
            ["FALSE", False],
            ["off", False],
            ["Off", False],
            ["OFF", False],
            ["0", False],
            [0, False],
            [[], False],
            [(), False],
            [{}, False],
            # True values
            [True, True],
            ["true", True],
            ["True", True],
            ["TRUE", True],
            ["on", True],
            ["On", True],
            ["ON", True],
            ["1", True],
            ["00", True],
            [[1, 2, 3], True],
            [(1, 2, 3), True],
            [{1, 2, 3}, True],
            [{"a": 1, "b": 2, "c": 3}, True],
        ]
    )
    def test_boolean(self, value_set, value_get):
        """Test the value is converted to boolean."""
        self.assertEqual(boolean(value_set), value_get)
