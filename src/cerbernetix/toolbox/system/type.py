"""A set of helpers for types management.

Examples:
```python
from cerbernetix.toolbox.system import full_type

print(full_type("foo")) # builtins.str
print(full_type(full_type)) # cerbernetix.toolbox.system.type.full_type
```
"""


def full_type(value) -> str:
    """Gets the fully qualified type of a value.

    Args:
        value (Any): The value from to get the fully qualified type.

    Returns:
        str: The fully qualified type of the value.

    Examples:
    ```python
    from cerbernetix.toolbox.system import full_type

    print(full_type("foo")) # builtins.str
    print(full_type(full_type)) # cerbernetix.toolbox.system.type.full_type
    ```
    """
    if value is None:
        return "None"

    if not hasattr(value, "__name__") or not hasattr(value, "__module__"):
        value = value.__class__

    return f"{value.__module__}.{value.__name__}"
