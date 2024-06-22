"""An iterator for returning elements from nested iterables.

Examples:
```python
from cerbernetix.toolbox.iterators import iter_deep

for v in iter_deep(1, 2, [[3], [4, [5]]], 6):
    print(v)
```
"""

from typing import Iterator


def iter_deep(*array) -> Iterator:
    """Creates an iterator that returns elements from each iterable including nested ones.

    The function accepts multiple iterables. If an iterable contains other iterables, they will
    also be consumed.

    Yields:
        Iterator: An iterator that returns elements from each iterable including nested ones.

    Examples:
    ```python
    from cerbernetix.toolbox.iterators import iter_deep

    for v in iter_deep(1, 2, [[3], [4, [5]]], 6):
        print(v)
    ```
    """
    for value in array:
        if isinstance(value, str):
            yield value
            continue
        try:
            values = iter(value)
        except TypeError:
            yield value
        else:
            for iterator in values:
                for val in iter_deep(iterator):
                    yield val
