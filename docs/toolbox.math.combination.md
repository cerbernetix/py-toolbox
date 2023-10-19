<!-- markdownlint-disable -->

<a href="../src/toolbox/math/combination.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.math.combination`
A set of functions for working with combinations. 



**Examples:**
 ```python
from toolbox.math import get_combination_rank, get_combination_from_rank

# Get the rank of a combination of 3 numbers
print(get_combination_rank([1,3,5]))

# Get the combination of 3 numbers ranked at position 5
print(list(get_combination_from_rank(5, 3)))
``` 


---

<a href="../src/toolbox/math/combination.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
 
 - <b>`ValueError`</b>:  If the combination contains values lower than 0. 



**Returns:**
 
 - <b>`int`</b>:  The rank of the combination, starting at 0. 



**Examples:**
 ```python
from toolbox.math import get_combination_rank

# Get the rank of a combination of 3 numbers
print(get_combination_rank([1,3,5]))
``` 


---

<a href="../src/toolbox/math/combination.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
from toolbox.math import get_combination_from_rank

# Get the combination of 3 numbers ranked at position 5
print(list(get_combination_from_rank(5, 3)))
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
