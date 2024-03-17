"""A set of functions for working with combinations.

Examples:
```python
from cerbernetix.toolbox.math import (
    get_combination_rank,
    get_combination_from_rank,
    get_combinations,
)

# Get the rank of a combination of 3 numbers
print(get_combination_rank([1, 3, 5]))

# Get the combination of 3 numbers ranked at position 5
print(get_combination_from_rank(5, 3))

# Get the combinations of 3 numbers from the list
values = [1, 2, 4, 8, 16]
print(list(get_combinations(values, 3)))
```
"""

from math import comb
from typing import Iterable, Iterator


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
    from cerbernetix.toolbox.math import get_combination_rank

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
    from cerbernetix.toolbox.math import get_combination_from_rank

    # Get the combination of 3 numbers ranked at position 5
    print(get_combination_from_rank(5, 3))
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


def get_combinations(
    values: int | list | tuple | dict,
    length: int = 2,
    offset: int = 0,
    columns: list | tuple = None,
) -> Iterator[list]:
    """Yields lists of combined values according to the combinations defined by the lengths.

    Taking a list of values and the length of a combination, it yields each combination of length
    elements taken from the values.

    Note: Beware, the number of possible combinations grows fast with the lengths.
    For example, 3 out of 5 gives 10 possible combinations, but 3 out of 50 gives 19600...

    Args:
        values (int | list | tuple | dict): The list of values from which build the list of
        combinations. It can be either the length of a range of integers from 0, or a list of
        sparse values.
        length (int, optional): The length of each combination. Defaults to 2.
        offset (int, optional): An offset to add to the values if they must not start at 0.
        Defaults to 0.
        columns (list | tuple, optional): A mapping list for retrieving the values in order from
        the values. Defaults to None.

    Yields:
        Iterator[list]: A list of combined values by the given length.

    Examples:
    ```python
    from cerbernetix.toolbox.math import get_combinations

    # Get the combinations of 3 numbers from the list
    values = [1, 2, 4, 8, 16]
    print(list(get_combinations(values, 3)))
    # [[1, 2, 4],
    #  [1, 2, 8],
    #  [1, 4, 8],
    #  [2, 4, 8],
    #  [1, 2, 16],
    #  [1, 4, 16],
    #  [2, 4, 16],
    #  [1, 8, 16],
    #  [2, 8, 16],
    #  [4, 8, 16]]
    ```
    """
    if isinstance(values, int):
        nb_values = values
        values = [*range(values)]
    else:
        nb_values = len(values)
    nb_comb = comb(nb_values, length)

    if columns is None:
        columns = [*range(nb_values)]

    for rank in range(nb_comb):
        combination = get_combination_from_rank(rank, length)
        yield [values[columns[index]] + offset for index in combination]
