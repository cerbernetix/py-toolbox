"""The `system` package provides several utilities for low level management.

It contains:
- `full_type(value)`: Return with the full qualified type of the given value.

Examples:
```python
from cerbernetix.toolbox.system import full_type

print(full_type("foo")) # builtins.str
print(full_type(full_type)) # cerbernetix.toolbox.system.type.full_type
```
"""

from cerbernetix.toolbox.system.type import full_type
