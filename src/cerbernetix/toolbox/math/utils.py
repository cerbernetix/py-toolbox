"""A set of helper functions related to math.

Examples
```python
from cerbernetix.toolbox.math import minmax

mini, maxi = minmax(3, 2, 6, 4, 5) # 2, 6
```

```python
from cerbernetix.toolbox.math import quantity

# Gets a size from a percentage
size = quantity(.2, 10) # 2

# Gets a size from an absolute value
size = quantity(6, 10)  # 6
```
"""


def minmax(*args) -> tuple:
    """Returns with the min and the max value from the arguments.

    Args:
        *args: Arguments from which extract the min and the max.

    Returns:
        tuple: A tuple with first the min value, then the max value.

    Examples
    ```python
    from cerbernetix.toolbox.math import minmax

    mini, maxi = minmax(3, 2, 6, 4, 5) # 2, 6
    ```
    """
    return min(*args), max(*args)


def quantity(quota: int | float, total: int) -> int:
    """Gets a quantity with respect to a quota applied to a total.

    Args:
        quota (int | float): The expected quota from the total. It can be either a percentage or an
        absolute value. The percentage is represented by a number between 0 and 1. An absolute
        value is represented by a number between 1 and the total included.
        total (int): The total number.

    Returns:
        int: The quantity computed from the quota applied to the total. It cannot exceeds the total,
        and it cannot be negative.

    Examples
    ```python
    from cerbernetix.toolbox.math import quantity

    # Gets a size from a percentage
    size = quantity(.2, 10) # 2

    # Gets a size from an absolute value
    size = quantity(6, 10)  # 6
    ```
    """
    if 0 < quota < 1:
        return int(total * quota)

    return min(abs(int(quota)), total)
