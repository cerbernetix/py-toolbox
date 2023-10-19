"""Test the set of functions for working with combinations."""
import unittest
from typing import Iterator

from toolbox.math import get_combination_from_rank, get_combination_rank
from toolbox.testing import test_cases


class TestCombination(unittest.TestCase):
    """Test suite for the set of functions for working with combinations."""

    @test_cases(
        [
            [[1], 5, 1],
            [[2], 5, 2],
            [[3], 5, 3],
            [[4], 5, 4],
            [[5], 5, 5],
            [[1, 2], 5, 1],
            [[2, 1], 5, 1],
            [[1, 3], 5, 2],
            [[1, 4], 5, 3],
            [[1, 5], 5, 4],
            [[2, 3], 5, 5],
            [[2, 4], 5, 6],
            [[2, 5], 5, 7],
            [[3, 4], 5, 8],
            [[3, 5], 5, 9],
            [[4, 5], 5, 10],
            [[1, 2, 3], 5, 1],
            [[3, 2, 1], 5, 1],
            [[1, 2, 4], 5, 2],
            [[1, 2, 5], 5, 3],
            [[1, 3, 4], 5, 4],
            [[1, 3, 5], 5, 5],
            [[1, 4, 5], 5, 6],
            [[2, 3, 4], 5, 7],
            [[2, 3, 5], 5, 8],
            [[2, 4, 5], 5, 9],
            [[3, 4, 5], 5, 10],
            [[1, 2, 3, 4], 5, 1],
            [[4, 2, 1, 3], 5, 1],
            [[1, 2, 3, 5], 5, 2],
            [[1, 2, 4, 5], 5, 3],
            [[1, 3, 4, 5], 5, 4],
            [[2, 3, 4, 5], 5, 5],
            [[1, 2, 3, 4, 5], 5, 1],
            [[11, 12], 12, 66],
            [[10, 11, 12], 12, 220],
        ]
    )
    def test_get_combination_rank(self, combination, max_value, rank):
        """Test get_combination_rank."""
        self.assertEqual(get_combination_rank(combination, max_value), rank)

    def test_get_combination_rank_error(self):
        """Test get_combination_rank errors."""
        self.assertRaises(ValueError, get_combination_rank, [1, 2], 0)
        self.assertRaises(ValueError, get_combination_rank, [], 2)
        self.assertRaises(ValueError, get_combination_rank, [0], 2)

    @test_cases(
        [
            [1, 1, 5, [1]],
            [2, 1, 5, [2]],
            [3, 1, 5, [3]],
            [4, 1, 5, [4]],
            [5, 1, 5, [5]],
            [1, 2, 5, [1, 2]],
            [2, 2, 5, [1, 3]],
            [3, 2, 5, [1, 4]],
            [4, 2, 5, [1, 5]],
            [5, 2, 5, [2, 3]],
            [6, 2, 5, [2, 4]],
            [7, 2, 5, [2, 5]],
            [8, 2, 5, [3, 4]],
            [9, 2, 5, [3, 5]],
            [10, 2, 5, [4, 5]],
            [1, 3, 5, [1, 2, 3]],
            [2, 3, 5, [1, 2, 4]],
            [3, 3, 5, [1, 2, 5]],
            [4, 3, 5, [1, 3, 4]],
            [5, 3, 5, [1, 3, 5]],
            [6, 3, 5, [1, 4, 5]],
            [7, 3, 5, [2, 3, 4]],
            [8, 3, 5, [2, 3, 5]],
            [9, 3, 5, [2, 4, 5]],
            [10, 3, 5, [3, 4, 5]],
            [1, 4, 5, [1, 2, 3, 4]],
            [2, 4, 5, [1, 2, 3, 5]],
            [3, 4, 5, [1, 2, 4, 5]],
            [4, 4, 5, [1, 3, 4, 5]],
            [5, 4, 5, [2, 3, 4, 5]],
            [1, 5, 5, [1, 2, 3, 4, 5]],
            [66, 2, 12, [11, 12]],
            [220, 3, 12, [10, 11, 12]],
        ]
    )
    def test_get_combination_from_rank(self, rank, length, max_value, combination):
        """Test get_combination_from_rank."""
        iterator = get_combination_from_rank(rank, length, max_value)
        self.assertIsInstance(iterator, Iterator)
        self.assertEqual(list(iterator), combination)

    def test_get_combination_from_rank_error(self):
        """Test get_combination_from_rank errors."""
        self.assertRaises(ValueError, lambda: list(get_combination_from_rank(0, 2, 4)))
        self.assertRaises(ValueError, lambda: list(get_combination_from_rank(1, 0, 4)))
        self.assertRaises(ValueError, lambda: list(get_combination_from_rank(1, 2, 0)))
        self.assertRaises(ValueError, lambda: list(get_combination_from_rank(11, 2, 5)))
