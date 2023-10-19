"""A collection of Math related tools.

It contains:
- `get_combination_rank(combination, max_value)`: Gets the rank of a combination.
- `get_combination_from_rank(rank, length, max_value)`: Gets the combination corresponding to a
particular rank.

Examples:
```python
from toolbox.math import get_combination_rank, get_combination_from_rank

# Get the rank of a combination
print(get_combination_rank([1,3,5], 8))

# Get the combination from an rank
print(list(get_combination_from_rank(5, 8)))
```
"""
from toolbox.math.combination import get_combination_from_rank, get_combination_rank
