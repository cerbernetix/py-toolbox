"""A set of functions for working with combinations.

Examples:
```python
from toolbox.math import get_combination_index, get_combination_from_index

# Get the index of a combination
print(get_combination_index([1,3,5], 8))

# Get the combination from an index
print(list(get_combination_from_index(5, 8)))
```
"""
from math import comb
from typing import Iterable, Iterator


def get_combination_index(combination: Iterable[int], max_value: int = 52) -> int:
    """Gets the index of a combination.

    The values in the combination must be in the range 1..max_value included.

    The first index is 1.
    The last index if equal to `comb(12, len(combination))`

    The combination is sorted before computing the index.

    Args:
        combination (Iterable[int]): The combination to index.
        max_value (int, optional): The maximum value for the combination. Defaults to 52.

    Raises:
        ValueError: If the max_value is lower than 1.
        ValueError: If the combination is empty.
        ValueError: If the combination contains values lower than 1.

    Returns:
        int: The index of the combination.

    Examples:
    ```python
    from toolbox.math import get_combination_index

    # Get the index of a combination for 3 numbers out of 8
    print(get_combination_index([1,3,5], 8))
    ```
    """
    combination = sorted(combination)
    length = len(combination)

    if max_value < 1:
        raise ValueError("The max value must not be lower than 1")

    if not length:
        raise ValueError("The combination must contain values")

    index = comb(max_value, length)
    for idx in range(length):
        value = combination[idx]
        if value < 1:
            raise ValueError("The combination must not contain values lower than 1")
        index -= comb(max_value - value, length - idx)

    return index


def get_combination_from_index(
    index: int,
    length: int = 2,
    max_value: int = 52,
) -> Iterator[int]:
    """Gets the combination corresponding to a particular index.

    The values in the combination will be in the range 1..max_value included.

    The index must be in the range 1..comb(12, len(combination)) included.

    Args:
        index (int): The index of the combination.
        length (int, optional): The length of the combination. Defaults to 2.
        max_value (int, optional): The maximum value for the combination. Defaults to 52.

    Raises:
        ValueError: If the length is lower than 1.
        ValueError: If the max_value is lower than 1.
        ValueError: If the index is lower than 1 or greater than the number of combinations.


    Yields:
        Iterator[int]: A number from the combination corresponding to the index.

    Examples:
    ```python
    from toolbox.math import get_combination_from_index

    # Get the combination for 3 numbers out of 8 from an index
    print(list(get_combination_from_index(5, 3, 8)))
    ```
    """
    if length < 1:
        raise ValueError("The combination length must not be lower than 1")

    if max_value < 1:
        raise ValueError("The max value must not be lower than 1")

    max_index = comb(max_value, length)

    if index < 1:
        raise ValueError("The index must not be lower than 1")

    if index > max_index:
        raise ValueError("The index must not be greater than the number of possible combinations")

    idx = max_index - index
    for pos in range(length, 0, -1):
        val_idx = 0
        value = 0
        while True:
            tmp_idx = comb(max_value - value, pos)
            if tmp_idx <= idx:
                val_idx = tmp_idx
                break
            value += 1

        idx -= val_idx
        yield value
