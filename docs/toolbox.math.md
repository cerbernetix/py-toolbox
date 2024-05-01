<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/math/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.math`
A collection of Math related tools. 

It contains: 
- `get_combination_rank(combination, offset)`: Gets the rank of a combination. 
- `get_combination_from_rank(rank, length, offset)`: Gets the combination corresponding to a particular rank. 
- `get_combinations(values, length, start, stop, step, offset, indexes)`: Yields lists of combined values according to the combinations defined by the lengths. 
- `minmax(*args)`: Returns with the min and the max value from the given arguments. 
- `quantity(quota, total)`: Gets a quantity with respect to a quota applied to a total. 



**Examples:**
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





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
