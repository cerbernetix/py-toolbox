<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/math/utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.math.utils`
A set of helper functions related to math. 

Examples ```python
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

<a href="../src/cerbernetix/toolbox/math/utils.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `minmax`

```python
minmax(*args) → tuple
```

Returns with the min and the max value from the arguments. 



**Args:**
 
 - <b>`*args`</b>:  Arguments from which extract the min and the max. 



**Returns:**
 
 - <b>`tuple`</b>:  A tuple with first the min value, then the max value. 

Examples ```python
from cerbernetix.toolbox.math import minmax

mini, maxi = minmax(3, 2, 6, 4, 5) # 2, 6
``` 


---

<a href="../src/cerbernetix/toolbox/math/utils.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `quantity`

```python
quantity(quota: int | float, total: int) → int
```

Gets a quantity with respect to a quota applied to a total. 



**Args:**
 
 - <b>`quota`</b> (int | float):  The expected quota from the total. It can be either a percentage or an absolute value. The percentage is represented by a number between 0 and 1. An absolute value is represented by a number between 1 and the total included. 
 - <b>`total`</b> (int):  The total number. 



**Returns:**
 
 - <b>`int`</b>:  The quantity computed from the quota applied to the total. It cannot exceeds the total, and it cannot be negative. 

Examples ```python
from cerbernetix.toolbox.math import quantity

# Gets a size from a percentage
size = quantity(.2, 10) # 2

# Gets a size from an absolute value
size = quantity(6, 10)  # 6
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
