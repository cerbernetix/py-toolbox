"""A set of helpers for loading properties dynamically.

Examples:
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
"""

import importlib
from typing import Any


def import_property(namespace: str) -> Any | None:
    """Imports a property from the given namespace.

    Args:
        namespace (str): The namespace of the property to import.

    Returns:
        Any | None: The imported property or None.

    Raises:
        ImportError: if an error occurs when importing.

    Examples:
    ```python
    from cerbernetix.toolbox.system import import_property

    try:
        update = import_property("lib.utils.update")
        update("foo")
    except ImportError as e:
        print(f"An error occurred while importing the update helper: {e}")
    ```
    """
    if namespace and ("." in namespace):
        module_name, type_name = namespace.rsplit(".", 1)
        return getattr(importlib.import_module(module_name), type_name, None)

    return None


def import_and_call(namespace: str, *args, **kwargs) -> Any:
    """Imports a callable from the given namespace, then call it with the given parameters.

    Args:
        namespace (str): The namespace of the property to import.
        *args: positional parameters forwarded to the callable.
        **kwargs: named parameters forwarded to the callable.

    Returns:
        Any: The return value of the callable.

    Raises:
        ImportError: if an error occurs when importing.
        TypeError: if the given namespace does not target a callable.

    Examples:
    ```python
    from cerbernetix.toolbox.system import import_and_call

    try:
        import_and_call("lib.utils.update", "foo")
    except ImportError as e:
        print(f"An error occurred while importing the update helper: {e}")
    except TypeError as e:
        print(f"Unable to call the update helper: {e}")
    ```
    """
    function = import_property(namespace)

    if not callable(function):
        raise TypeError(f"{namespace} is not callable!")

    return function(*args, **kwargs)
