"""The `system` package provides several utilities for low level management.

It contains:
- `full_type(value)`: Return with the full qualified type of the given value.
- `import_prop(ns)`: Import a property from the given namespace.

Examples:
```python
from cerbernetix.toolbox.system import full_type

print(full_type("foo")) # builtins.str
print(full_type(full_type)) # cerbernetix.toolbox.system.type.full_type
```

```python
from cerbernetix.toolbox.system import import_prop

try:
    update = import_prop("lib.utils.update")
    update("foo")
except ImportError as e:
    print(f"An error occurred while importing the update helper: {e}")
```
"""

from cerbernetix.toolbox.system.module import import_prop
from cerbernetix.toolbox.system.type import full_type
