<!-- markdownlint-disable -->

<a href="../toolbox/data/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.data`
A collection of data utilities. 

It contains: 
- Value mappers: 
    - `passthrough(value)` - A passthrough mapper. It returns the value as it is. 
    - `boolean(value)` - Converts a value to a boolean value. 



**Examples:**
 ```python
from toolbox.data import mappers

# Passthrough a value
print(mappers.passthrough("foo")) # "foo"
print(mappers.passthrough(42)) # 42

# Gets a boolean value
print(mappers.boolean("True")) # True
print(mappers.boolean("On")) # True
print(mappers.boolean("1")) # True
print(mappers.boolean("False")) # False
print(mappers.boolean("Off")) # False
print(mappers.boolean("0")) # False
``` 

**Global Variables**
---------------
- **mappers**




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
