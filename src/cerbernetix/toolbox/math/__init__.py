"""A collection of Math related tools.

It contains:
- `get_combination_rank(combination, offset)`: Gets the rank of a combination.
- `get_combination_from_rank(rank, length, offset)`: Gets the combination corresponding to a
particular rank.
- `get_combinations(values, length, offset, indexes, start, stop, step)`: Yields lists of combined
values according to the combinations defined by the lengths.

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

# Get the combinations of 3 numbers out of 50 from rank 200 to 500
values = [1, 2, 4, 8, 16]
print(list(get_combinations(50, 3, start=200, stop=300)))
```
"""

from cerbernetix.toolbox.math.combination import (
    get_combination_from_rank,
    get_combination_rank,
    get_combinations,
)
