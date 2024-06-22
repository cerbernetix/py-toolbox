<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/iterators/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.iterators`
A collection of iterators. 

It contains: 
- `iter_deep(*iterables)` - Iterator that returns elements from each iterable including nested ones. 



**Examples:**
 ```python
from cerbernetix.toolbox.iterators import iter_deep

for v in iter_deep(1, 2, [[3], [4, [5]]], 6):
     print(v)
``` 





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
