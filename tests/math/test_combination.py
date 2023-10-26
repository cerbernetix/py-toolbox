"""Test the set of functions for working with combinations."""
import unittest

from cerbernetix.toolbox.math import get_combination_from_rank, get_combination_rank
from cerbernetix.toolbox.testing import test_cases


class TestCombination(unittest.TestCase):
    """Test suite for the set of functions for working with combinations."""

    @test_cases(
        [
            [[], 0, 0],
            [[], 1, 0],
            # start from 0, 5 choose 1
            [[0], 0, 0],
            [[1], 0, 1],
            [[2], 0, 2],
            [[3], 0, 3],
            [[4], 0, 4],
            # start from 1, 5 choose 1
            [[1], 1, 0],
            [[2], 1, 1],
            [[3], 1, 2],
            [[4], 1, 3],
            [[5], 1, 4],
            # start from 0, 5 choose 2
            [[0, 1], 0, 0],
            [[1, 0], 0, 0],
            [[0, 2], 0, 1],
            [[1, 2], 0, 2],
            [[0, 3], 0, 3],
            [[1, 3], 0, 4],
            [[2, 3], 0, 5],
            [[0, 4], 0, 6],
            [[1, 4], 0, 7],
            [[2, 4], 0, 8],
            [[3, 4], 0, 9],
            # start from 1, 5 choose 2
            [[1, 2], 1, 0],
            [[2, 1], 1, 0],
            [[1, 3], 1, 1],
            [[2, 3], 1, 2],
            [[1, 4], 1, 3],
            [[2, 4], 1, 4],
            [[3, 4], 1, 5],
            [[1, 5], 1, 6],
            [[2, 5], 1, 7],
            [[3, 5], 1, 8],
            [[4, 5], 1, 9],
            # start from 0, 5 choose 3
            [[0, 1, 2], 0, 0],
            [[2, 1, 0], 0, 0],
            [[0, 1, 3], 0, 1],
            [[0, 2, 3], 0, 2],
            [[1, 2, 3], 0, 3],
            [[0, 1, 4], 0, 4],
            [[0, 2, 4], 0, 5],
            [[1, 2, 4], 0, 6],
            [[0, 3, 4], 0, 7],
            [[1, 3, 4], 0, 8],
            [[2, 3, 4], 0, 9],
            # start from 1, 5 choose 3
            [[1, 2, 3], 1, 0],
            [[3, 1, 1], 1, 0],
            [[1, 2, 4], 1, 1],
            [[1, 3, 4], 1, 2],
            [[2, 3, 4], 1, 3],
            [[1, 2, 5], 1, 4],
            [[1, 3, 5], 1, 5],
            [[2, 3, 5], 1, 6],
            [[1, 4, 5], 1, 7],
            [[2, 4, 5], 1, 8],
            [[3, 4, 5], 1, 9],
            # start from 0, 5 choose 4
            [[0, 1, 2, 3], 0, 0],
            [[3, 1, 0, 2], 0, 0],
            [[0, 1, 2, 4], 0, 1],
            [[0, 1, 3, 4], 0, 2],
            [[0, 2, 3, 4], 0, 3],
            [[1, 2, 3, 4], 0, 4],
            # start from 1, 5 choose 4
            [[1, 2, 3, 4], 1, 0],
            [[4, 2, 1, 3], 1, 0],
            [[1, 2, 3, 5], 1, 1],
            [[1, 2, 4, 5], 1, 2],
            [[1, 3, 4, 5], 1, 3],
            [[2, 3, 4, 5], 1, 4],
            # start from 0, 5 choose 5
            [[0, 1, 2, 3, 4], 0, 0],
            # start from 1, 5 choose 5
            [[1, 2, 3, 4, 5], 1, 0],
            # start from 0, 12 choose 2
            [[10, 11], 0, 65],
            # start from 1, 12 choose 2
            [[11, 12], 1, 65],
            # start from 0, 12 choose 3
            [[9, 10, 11], 0, 219],
            # start from 1, 12 choose 3
            [[10, 11, 12], 1, 219],
        ]
    )
    def test_get_combination_rank(self, combination, offset, rank):
        """Test get_combination_rank."""
        self.assertEqual(get_combination_rank(combination, offset), rank)

    def test_get_combination_rank_error(self):
        """Test get_combination_rank errors."""
        self.assertRaises(ValueError, get_combination_rank, [-1])
        self.assertRaises(ValueError, get_combination_rank, [0], 1)
        self.assertRaises(ValueError, get_combination_rank, [-1, -1])
        self.assertRaises(ValueError, get_combination_rank, [0, 0], 1)

    @test_cases(
        [
            [0, 0, 0, []],
            [0, 0, 1, []],
            # start from 0, 5 choose 1
            [0, 1, 0, [0]],
            [1, 1, 0, [1]],
            [2, 1, 0, [2]],
            [3, 1, 0, [3]],
            [4, 1, 0, [4]],
            # start from 1, 5 choose 1
            [0, 1, 1, [1]],
            [1, 1, 1, [2]],
            [2, 1, 1, [3]],
            [3, 1, 1, [4]],
            [4, 1, 1, [5]],
            # start from 0, 5 choose  2
            [0, 2, 0, [0, 1]],
            [1, 2, 0, [0, 2]],
            [2, 2, 0, [1, 2]],
            [3, 2, 0, [0, 3]],
            [4, 2, 0, [1, 3]],
            [5, 2, 0, [2, 3]],
            [6, 2, 0, [0, 4]],
            [7, 2, 0, [1, 4]],
            [8, 2, 0, [2, 4]],
            [9, 2, 0, [3, 4]],
            # start from 1, 5 choose 2
            [0, 2, 1, [1, 2]],
            [1, 2, 1, [1, 3]],
            [2, 2, 1, [2, 3]],
            [3, 2, 1, [1, 4]],
            [4, 2, 1, [2, 4]],
            [5, 2, 1, [3, 4]],
            [6, 2, 1, [1, 5]],
            [7, 2, 1, [2, 5]],
            [8, 2, 1, [3, 5]],
            [9, 2, 1, [4, 5]],
            # start from 0, 5 choose 3
            [0, 3, 0, [0, 1, 2]],
            [1, 3, 0, [0, 1, 3]],
            [2, 3, 0, [0, 2, 3]],
            [3, 3, 0, [1, 2, 3]],
            [4, 3, 0, [0, 1, 4]],
            [5, 3, 0, [0, 2, 4]],
            [6, 3, 0, [1, 2, 4]],
            [7, 3, 0, [0, 3, 4]],
            [8, 3, 0, [1, 3, 4]],
            [9, 3, 0, [2, 3, 4]],
            # start from 1, 5 choose 3
            [0, 3, 1, [1, 2, 3]],
            [1, 3, 1, [1, 2, 4]],
            [2, 3, 1, [1, 3, 4]],
            [3, 3, 1, [2, 3, 4]],
            [4, 3, 1, [1, 2, 5]],
            [5, 3, 1, [1, 3, 5]],
            [6, 3, 1, [2, 3, 5]],
            [7, 3, 1, [1, 4, 5]],
            [8, 3, 1, [2, 4, 5]],
            [9, 3, 1, [3, 4, 5]],
            # start from 0, 5 choose 4
            [0, 4, 0, [0, 1, 2, 3]],
            [1, 4, 0, [0, 1, 2, 4]],
            [2, 4, 0, [0, 1, 3, 4]],
            [3, 4, 0, [0, 2, 3, 4]],
            [4, 4, 0, [1, 2, 3, 4]],
            # start from 1, 5 choose 4
            [0, 4, 1, [1, 2, 3, 4]],
            [1, 4, 1, [1, 2, 3, 5]],
            [2, 4, 1, [1, 2, 4, 5]],
            [3, 4, 1, [1, 3, 4, 5]],
            [4, 4, 1, [2, 3, 4, 5]],
            # start from 0, 5 choose 5
            [0, 5, 0, [0, 1, 2, 3, 4]],
            # start from 1, 5 choose 5
            [0, 5, 1, [1, 2, 3, 4, 5]],
            # start from 0, 12 choose  2
            [65, 2, 0, [10, 11]],
            # start from 1, 12 choose  2
            [65, 2, 1, [11, 12]],
            # start from 0, 12 choose  3
            [219, 3, 0, [9, 10, 11]],
            # start from 1, 12 choose  3
            [219, 3, 1, [10, 11, 12]],
        ]
    )
    def test_get_combination_from_rank(self, rank, length, offset, combination):
        """Test get_combination_from_rank."""
        self.assertEqual(get_combination_from_rank(rank, length, offset), combination)

    def test_get_combination_from_rank_error(self):
        """Test get_combination_from_rank errors."""
        self.assertRaises(ValueError, lambda: get_combination_from_rank(-1, 2))
        self.assertRaises(ValueError, lambda: get_combination_from_rank(0, -1, 4))
