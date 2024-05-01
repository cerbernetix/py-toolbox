<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/math/combination.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.math.combination`
A set of functions for working with combinations. 



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


---

<a href="../src/cerbernetix/toolbox/math/combination.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_combination_rank`

```python
get_combination_rank(combination: Iterable[int], offset: int = 0) → int
```

Gets the rank of a combination. 

The combination is sorted before computing the rank. 

The rank starts at 0. The values in the combination must start at 0. Negative numbers will raise an error. 



**Args:**
 
 - <b>`combination`</b> (Iterable[int]):  The combination to rank. 
 - <b>`offset`</b> (int, optional):  An offset to remove from the values if they don't start at 0. Defaults to 0. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the combination contains negative values. 



**Returns:**
 
 - <b>`int`</b>:  The rank of the combination, starting at 0. 



**Examples:**
 ```python
from cerbernetix.toolbox.math import get_combination_rank

# Get the rank of a combination of 3 numbers
print(get_combination_rank([1, 3, 5]))
``` 


---

<a href="../src/cerbernetix/toolbox/math/combination.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_combination_from_rank`

```python
get_combination_from_rank(
    rank: int,
    length: int = 2,
    offset: int = 0
) → list[int]
```

Gets the combination corresponding to a particular rank. 

The rank must start at 0. 



**Args:**
 
 - <b>`rank`</b> (int):  The rank of the combination. 
 - <b>`length`</b> (int, optional):  The length of the combination. Defaults to 2. 
 - <b>`offset`</b> (int, optional):  An offset to add to the values if they must not start at 0. Defaults to 0. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the rank is negative. 
 - <b>`ValueError`</b>:  If the length is negative 



**Returns:**
 
 - <b>`list[int]`</b>:  The combination corresponding to the rank, sorted by ascending values. 



**Examples:**
 ```python
from cerbernetix.toolbox.math import get_combination_from_rank

# Get the combination of 3 numbers ranked at position 5
print(get_combination_from_rank(5, 3))
``` 


---

<a href="../src/cerbernetix/toolbox/math/combination.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_combinations`

```python
get_combinations(
    values: int | list | tuple | dict,
    length: int = 2,
    start: int = 0,
    stop: int = None,
    step: int = 1,
    offset: int = 0,
    indexes: list | tuple = None
) → Iterator[list]
```

Yields lists of combined values according to the combinations defined by the lengths. 

Taking a list of values and the length of a combination, it yields each combination of length elements taken from the values. 

Note: Beware, the number of possible combinations grows fast with the lengths. For example, 3 out of 5 gives 10 possible combinations, but 3 out of 50 gives 19600... 



**Args:**
 
 - <b>`values`</b> (int | list | tuple | dict):  The list of values from which build the list of combinations. It can be either the length of a range of integers from 0, or a list of sparse values. 
 - <b>`length`</b> (int, optional):  The length of each combination. Defaults to 2. 
 - <b>`start`</b> (int, optional):  The rank of the first combination to generate. Defaults to 0. 
 - <b>`stop`</b> (int, optional):  The rank of the last combination before what stop the generation. If omitted, the maximum number of combination is taken. Defaults to None. 
 - <b>`step`</b> (int, optional):  The step between ranks. If start is higher than stop, the step is set to a negative value. Defaults to 1. 
 - <b>`offset`</b> (int, optional):  An offset to add to the values if they must not start at 0. Defaults to 0. 
 - <b>`indexes`</b> (list | tuple, optional):  A list of indexes for retrieving the values by position. Useful if the values are not indexed by sequential numbers or with a contiguous set like a dictionary or a spare array. Defaults to None. 



**Yields:**
 
 - <b>`Iterator[list]`</b>:  A list of combined values by the given length. 



**Examples:**
 ```python
from cerbernetix.toolbox.math import get_combinations

# Get the combinations of 3 numbers from the list
values = [1, 2, 4, 8, 16]
print(list(get_combinations(values, 3)))
# [[1, 2, 4],
#  [1, 2, 8],
#  [1, 4, 8],
#  [2, 4, 8],
#  [1, 2, 16],
#  [1, 4, 16],
#  [2, 4, 16],
#  [1, 8, 16],
#  [2, 8, 16],
#  [4, 8, 16]]

# Get the combinations of 3 numbers from the list from rank 4 to 8
values = {"1": 1, "2": 2, "4": 4, "8": 8, "16": 16}
indexes = ["1", "2", "4", "8", "16"]
print(list(get_combinations(values, 3, indexes=indexes, start=4, stop=8)))
# [[1, 2, 16],
#  [1, 4, 16],
#  [2, 4, 16],
#  [1, 8, 16]]

# Get combinations from a number of values
print(list(get_combinations(5, 3, offset=1)))
# [[1, 2, 3],
#  [1, 2, 4],
#  [1, 3, 4],
#  [2, 3, 4],
#  [1, 2, 5],
#  [1, 3, 5],
#  [2, 3, 5],
#  [1, 4, 5],
#  [2, 4, 5],
#  [3, 4, 5]]
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
