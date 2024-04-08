"""A set of helper functions related to math.

Examples
```python
from cerbernetix.toolbox.math import minmax

mini, maxi = minmax(3, 2, 6, 4, 5) # 2, 6
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
