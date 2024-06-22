"""Test the iterator for returning elements from nested iterables."""

import unittest

from cerbernetix.toolbox.iterators import iter_deep


class TestIterDeep(unittest.TestCase):
    """Test suite for the iterator for returning elements from nested iterables."""

    def test_scalars(self):
        """Test iter_deep accepts multiple scalars."""
        self.assertEqual([*iter_deep(True, "2", 3)], [True, "2", 3])

    def test_iterables(self):
        """Test iter_deep accepts multiple iterables."""
        self.assertEqual(
            [*iter_deep([True, False], ["1", "2"], [1, 2, 3])], [True, False, "1", "2", 1, 2, 3]
        )

    def test_nested_iterables(self):
        """Test iter_deep accepts multiple iterables."""
        self.assertEqual([*iter_deep(1, 2, [[3], [4, [5]]], 6)], [1, 2, 3, 4, 5, 6])
