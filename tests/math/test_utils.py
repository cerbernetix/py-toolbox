"""Test the set of helper functions related to math."""

import unittest

from cerbernetix.toolbox.math import limit, minmax, quantity


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

    def test_limit(self):
        """Test limit."""
        self.assertEqual(limit(1, 3, 7), 3)
        self.assertEqual(limit(5, 3, 7), 5)
        self.assertEqual(limit(9, 3, 7), 7)

    def test_quantity(self):
        """Test quantity."""
        self.assertEqual(quantity(5, 10), 5)
        self.assertEqual(quantity(0.1, 10), 1)
        self.assertEqual(quantity(0.33, 10), 3)
        self.assertEqual(quantity(0.99, 10), 9)
        self.assertEqual(quantity(1.0, 10), 10)
        self.assertEqual(quantity(1.5, 10), 1)
        self.assertEqual(quantity(-0.2, 10), 0)
        self.assertEqual(quantity(30, 10), 10)
