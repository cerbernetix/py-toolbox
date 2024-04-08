"""Test the set of helper functions related to math."""

import unittest

from cerbernetix.toolbox.math import minmax


class TestUtils(unittest.TestCase):
    """Test suite for the set of helper functions related to math."""

    def test_minmax(self):
        """Test minmax."""
        self.assertEqual(minmax([1]), (1, 1))
        self.assertEqual(minmax([1, 2]), (1, 2))
        self.assertEqual(minmax([2, 1]), (1, 2))
        self.assertEqual(minmax(*[1, 2]), (1, 2))
        self.assertEqual(minmax(*[2, 1]), (1, 2))
        self.assertEqual(minmax(1, 2), (1, 2))
        self.assertEqual(minmax(2, 1), (1, 2))
        self.assertEqual(minmax(3, 2, 6, 5, 4), (2, 6))
