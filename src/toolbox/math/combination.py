"""A set of functions for working with combinations.

Examples:
```python
from toolbox.math import get_combination_rank, get_combination_from_rank

# Get the rank of a combination of 3 numbers
print(get_combination_rank([1, 3, 5]))

# Get the combination of 3 numbers ranked at position 5
print(list(get_combination_from_rank(5, 3)))
```
"""
from math import comb
from typing import Iterable


def get_combination_rank(combination: Iterable[int], offset: int = 0) -> int:
    """Gets the rank of a combination.

    The combination is sorted before computing the rank.

    The rank starts at 0.
    The values in the combination must start at 0. Negative numbers will raise an error.

    Args:
        combination (Iterable[int]): The combination to rank.
        offset (int, optional): An offset to remove from the values if they don't start at 0.
        Defaults to 0.

    Raises:
        ValueError: If the combination contains negative values.

    Returns:
        int: The rank of the combination, starting at 0.

    Examples:
    ```python
    from toolbox.math import get_combination_rank

    # Get the rank of a combination of 3 numbers
    print(get_combination_rank([1, 3, 5]))
    ```
    """
    rank = 0
    for index, value in enumerate(sorted(combination)):
        value -= offset

        if value == index:
            continue

        rank += comb(value, index + 1)

    return rank


def get_combination_from_rank(rank: int, length: int = 2, offset: int = 0) -> list[int]:
    """Gets the combination corresponding to a particular rank.

    The rank must start at 0.

    Args:
        rank (int): The rank of the combination.
        length (int, optional): The length of the combination. Defaults to 2.
        offset (int, optional): An offset to add to the values if they must not start at 0.
        Defaults to 0.

    Raises:
        ValueError: If the rank is negative.
        ValueError: If the length is negative

    Returns:
        list[int]: The combination corresponding to the rank, sorted by ascending values.

    Examples:
    ```python
    from toolbox.math import get_combination_from_rank

    # Get the combination of 3 numbers ranked at position 5
    print(list(get_combination_from_rank(5, 3)))
    ```
    """
    if rank < 0:
        raise ValueError("The rank must not be negative")

    if length < 0:
        raise ValueError("The length must not be negative")

    if length == 0:
        return []

    if length == 1:
        return [rank + offset]

    combination = [0] * length

    binomial = 0
    val = 0
    b = 1
    while b <= rank:
        val += 1
        binomial = b
        b = (b * (val + length)) // val

    for index in range(length - 1, 1, -1):
        rank -= binomial
        binomial = (binomial * (index + 1)) // (val + index)
        combination[index] = val + index + offset

        while binomial > rank:
            val -= 1
            binomial = (binomial * val) // (val + index)

    combination[1] = val + 1 + offset
    combination[0] = rank - binomial + offset

    return combination
