<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/system/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.system`
The `system` package provides several utilities for low level management. 

It contains: 
- `full_type(value)`: Returns with the fully qualified type of the given value. 
- `import_property(ns)`: Imports a property from the given namespace. 
- `import_and_call(ns)`: Imports a function from the given namespace and call it with parameters. 



**Examples:**
 ```python
from cerbernetix.toolbox.system import full_type

print(full_type("foo")) # builtins.str
print(full_type(full_type)) # cerbernetix.toolbox.system.type.full_type
``` 

```python
from cerbernetix.toolbox.system import import_property

try:
     update = import_property("lib.utils.update")
     update("foo")
except ImportError as e:
     print(f"An error occurred while importing the update helper: {e}")
``` 

```python
from cerbernetix.toolbox.system import import_and_call

try:
     import_and_call("lib.utils.update", "foo")
except ImportError as e:
     print(f"An error occurred while importing the update helper: {e}")
except TypeError as e:
     print(f"Unable to call the update helper: {e}")
``` 





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
