"""A collection of iterators.

It contains:
- `iter_deep(*iterables)` - Iterator that returns elements from each iterable including nested ones.

Examples:
```python
from cerbernetix.toolbox.iterators import iter_deep

for v in iter_deep(1, 2, [[3], [4, [5]]], 6):
    print(v)
```
"""

from cerbernetix.toolbox.iterators.iter_deep import iter_deep
