<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/iterators/iter_deep.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.iterators.iter_deep`
An iterator for returning elements from nested iterables. 



**Examples:**
 ```python
from cerbernetix.toolbox.iterators import iter_deep

for v in iter_deep(1, 2, [[3], [4, [5]]], 6):
     print(v)
``` 


---

<a href="../src/cerbernetix/toolbox/iterators/iter_deep.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `iter_deep`

```python
iter_deep(*array) → Iterator
```

Creates an iterator that returns elements from each iterable including nested ones. 

The function accepts multiple iterables. If an iterable contains other iterables, they will also be consumed. 



**Yields:**
 
 - <b>`Iterator`</b>:  An iterator that returns elements from each iterable including nested ones. 



**Examples:**
 ```python
from cerbernetix.toolbox.iterators import iter_deep

for v in iter_deep(1, 2, [[3], [4, [5]]], 6):
    print(v)
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
