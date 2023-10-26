<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/math/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.math`
A collection of Math related tools. 

It contains: 
- `get_combination_rank(combination, offset)`: Gets the rank of a combination. 
- `get_combination_from_rank(rank, length, offset)`: Gets the combination corresponding to a particular rank. 



**Examples:**
 ```python
from cerbernetix.toolbox.math import get_combination_rank, get_combination_from_rank

# Get the rank of a combination of 3 numbers
print(get_combination_rank([1, 3, 5]))

# Get the combination of 3 numbers ranked at position 5
print(list(get_combination_from_rank(5, 3)))
``` 





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
