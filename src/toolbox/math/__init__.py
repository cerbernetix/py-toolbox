"""A collection of Math related tools.

It contains:
- `get_combination_index(combination, max_value)`: Gets the index of a combination.
- `get_combination_from_index(index, length, max_value)`: Gets the combination corresponding to a
particular index.

Examples:
```python
from toolbox.math import get_combination_index, get_combination_from_index

# Get the index of a combination
print(get_combination_index([1,3,5], 8))

# Get the combination from an index
print(list(get_combination_from_index(5, 8)))
```
"""
from toolbox.math.combination import get_combination_from_index, get_combination_index
