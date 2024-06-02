<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/system/module.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.system.module`
A set of helpers for loading properties dynamically. 



**Examples:**
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

<a href="../src/cerbernetix/toolbox/system/module.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `import_property`

```python
import_property(namespace: str) → Any | None
```

Imports a property from the given namespace. 



**Args:**
 
 - <b>`namespace`</b> (str):  The namespace of the property to import. 



**Returns:**
 
 - <b>`Any | None`</b>:  The imported property or None. 



**Raises:**
 
 - <b>`ImportError`</b>:  if an error occurs when importing. 



**Examples:**
 ```python
from cerbernetix.toolbox.system import import_property

try:
    update = import_property("lib.utils.update")
    update("foo")
except ImportError as e:
    print(f"An error occurred while importing the update helper: {e}")
``` 


---

<a href="../src/cerbernetix/toolbox/system/module.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `import_and_call`

```python
import_and_call(namespace: str, *args, **kwargs) → Any
```

Imports a callable from the given namespace, then call it with the given parameters. 



**Args:**
 
 - <b>`namespace`</b> (str):  The namespace of the property to import. 
 - <b>`*args`</b>:  positional parameters forwarded to the callable. 
 - <b>`**kwargs`</b>:  named parameters forwarded to the callable. 



**Returns:**
 
 - <b>`Any`</b>:  The return value of the callable. 



**Raises:**
 
 - <b>`ImportError`</b>:  if an error occurs when importing. 
 - <b>`TypeError`</b>:  if the given namespace does not target a callable. 



**Examples:**
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
