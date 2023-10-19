"""A collection of Math related tools.

It contains:
- `get_combination_rank(combination, offset)`: Gets the rank of a combination.
- `get_combination_from_rank(rank, length, offset)`: Gets the combination corresponding to a
particular rank.

Examples:
```python
from toolbox.math import get_combination_rank, get_combination_from_rank

# Get the rank of a combination of 3 numbers
print(get_combination_rank([1, 3, 5]))

# Get the combination of 3 numbers ranked at position 5
print(list(get_combination_from_rank(5, 3)))
```
"""
from toolbox.math.combination import get_combination_from_rank, get_combination_rank
