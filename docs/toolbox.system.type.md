<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/system/type.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.system.type`
A set of helpers for types management. 



**Examples:**
 ```python
from cerbernetix.toolbox.system import full_type

print(full_type("foo")) # builtins.str
print(full_type(full_type)) # cerbernetix.toolbox.system.type.full_type
``` 


---

<a href="../src/cerbernetix/toolbox/system/type.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `full_type`

```python
full_type(value) → str
```

Gets the fully qualified type of a value. 



**Args:**
 
 - <b>`value`</b> (Any):  The value from to get the fully qualified type. 



**Returns:**
 
 - <b>`str`</b>:  The fully qualified type of the value. 



**Examples:**
 ```python
from cerbernetix.toolbox.system import full_type

print(full_type("foo")) # builtins.str
print(full_type(full_type)) # cerbernetix.toolbox.system.type.full_type
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
