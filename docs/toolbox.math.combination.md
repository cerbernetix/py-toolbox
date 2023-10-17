<!-- markdownlint-disable -->

<a href="../src/toolbox/math/combination.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.math.combination`
A set of functions for working with combinations. 



**Examples:**
 ```python
from toolbox.math import get_combination_index, get_combination_from_index

# Get the index of a combination
print(get_combination_index([1,3,5], 8))

# Get the combination from an index
print(list(get_combination_from_index(5, 8)))
``` 


---

<a href="../src/toolbox/math/combination.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_combination_index`

```python
get_combination_index(combination: Iterable[int], max_value: int = 52) → int
```

Gets the index of a combination. 

The values in the combination must be in the range 1..max_value included. 

The first index is 1. The last index if equal to `comb(12, len(combination))` 

The combination is sorted before computing the index. 



**Args:**
 
 - <b>`combination`</b> (Iterable[int]):  The combination to index. 
 - <b>`max_value`</b> (int, optional):  The maximum value for the combination. Defaults to 52. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the max_value is lower than 1. 
 - <b>`ValueError`</b>:  If the combination is empty. 
 - <b>`ValueError`</b>:  If the combination contains values lower than 1. 



**Returns:**
 
 - <b>`int`</b>:  The index of the combination. 



**Examples:**
 ```python
from toolbox.math import get_combination_index

# Get the index of a combination for 3 numbers out of 8
print(get_combination_index([1,3,5], 8))
``` 


---

<a href="../src/toolbox/math/combination.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_combination_from_index`

```python
get_combination_from_index(
    index: int,
    length: int = 2,
    max_value: int = 52
) → Iterator[int]
```

Gets the combination corresponding to a particular index. 

The values in the combination will be in the range 1..max_value included. 

The index must be in the range 1..comb(12, len(combination)) included. 



**Args:**
 
 - <b>`index`</b> (int):  The index of the combination. 
 - <b>`length`</b> (int, optional):  The length of the combination. Defaults to 2. 
 - <b>`max_value`</b> (int, optional):  The maximum value for the combination. Defaults to 52. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the length is lower than 1. 
 - <b>`ValueError`</b>:  If the max_value is lower than 1. 
 - <b>`ValueError`</b>:  If the index is lower than 1 or greater than the number of combinations. 





**Yields:**
 
 - <b>`Iterator[int]`</b>:  A number from the combination corresponding to the index. 



**Examples:**
 ```python
from toolbox.math import get_combination_from_index

# Get the combination for 3 numbers out of 8 from an index
print(list(get_combination_from_index(5, 3, 8)))
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
