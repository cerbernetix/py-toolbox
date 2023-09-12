"""Extends the default Python TestCase with more assertions.

Examples:
```python
from toolbox import testing

class TestMyStuff(testing.TestCase)
    def test_list(self):
        self.assertListsAlmostEqual(generator(), [1.23, 3.14, 1.61])

    def test_dict(self):
        self.assertListsAlmostEqual(create_dict(), {"value": 42.4242, "PI": 3.1415})
```
"""
import unittest
from typing import Iterable


class TestCase(unittest.TestCase):
    """Test class with additional assertions."""

    def assertListsAlmostEqual(
        self, first: Iterable[float], second: Iterable[float], places: int = 7
    ):
        """Asserts that 2 lists of float numbers are almost equal by the number of places.

        Args:
            first (Iterable[float]): The first list to compare.
            second (Iterable[float]): The second list to compare.
            places (int, optional): The number of decimal places under what the numbers must be
            equal. Defaults to 7.

        Raises:
            AssertionError: If the 2 lists are not almost equals by the number of places.

        Examples:
        ```python
        from toolbox import testing

        class TestMyStuff(testing.TestCase)
            def test_almost_equal(self):
                self.assertListsAlmostEqual(generator(), [1.23, 3.14, 1.61])
        ```
        """
        first_is_iterable = isinstance(first, Iterable)
        second_is_iterable = isinstance(second, Iterable)

        if not first_is_iterable and not second_is_iterable:
            return self.assertAlmostEqual(first, second, places)

        if not first_is_iterable or not second_is_iterable:
            raise AssertionError("first != second")

        first_iter = iter(first if not isinstance(first, dict) else first.values())
        second_iter = iter(second if not isinstance(second, dict) else second.values())

        while True:
            stop_left = False
            stop_right = False

            try:
                left = next(first_iter)
            except StopIteration:
                stop_left = True

            try:
                right = next(second_iter)
            except StopIteration:
                stop_right = True

            if (stop_left and not stop_right) or (not stop_left and stop_right):
                raise AssertionError("len(first) != len(second)")

            if stop_left or stop_right:
                break

            self.assertListsAlmostEqual(left, right, places)

    def assertListsNotAlmostEqual(
        self, first: Iterable[float], second: Iterable[float], places: int = 7
    ):
        """Asserts that 2 lists of float numbers are not almost equal by the number of places.

        Args:
            first (Iterable[float]): The first list to compare.
            second (Iterable[float]): The second list to compare.
            places (int, optional): The number of decimal places under what the numbers must be
            equal. Defaults to 7.

        Raises:
            AssertionError: If the 2 lists are almost equals by the number of places.

        Examples:
        ```python
        from toolbox import testing

        class TestMyStuff(testing.TestCase)
            def test_almost_equal(self):
                self.assertListsNotAlmostEqual(generator(), [1.23, 3.14, 1.61])
        ```
        """
        try:
            self.assertListsAlmostEqual(first, second, places)
        except AssertionError:
            pass
        else:
            raise AssertionError("lists are almost equal")
