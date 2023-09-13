"""A collection of data mappers.

Examples:
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
"""
from typing import Any, Protocol


class ValueMapper(Protocol):
    """The interface for a value mapper.

    Such an object is responsible for formatting a value in the expected type and format.

    A mapper respecting this interface will be used as follows:

    ```python
    value = mapper(raw_value)
    ```
    """

    def __call__(self, value: Any) -> Any:
        return value  # pragma: no cover


def passthrough(value: Any) -> Any:
    """A passthrough mapper. It returns the value as it is.

    Args:
        value (Any): The value to map.

    Returns:
        Any: The mapped value.

    Examples:
    ```python
    from toolbox.data import passthrough

    print(passthrough("foo")) # "foo"
    print(passthrough(42)) # 42
    print(passthrough([])) # []
    print(passthrough({})) # {}
    ```
    """
    return value


def boolean(value: Any) -> bool:
    """Converts a value to a boolean value.

    Args:
        value (Any): A value to cast to boolean.

    Returns:
        bool: The value casted to boolean.

    Examples:
    ```python
    from toolbox.data import boolean

    print(boolean(True)) # True
    print(boolean("True")) # True
    print(boolean("On")) # True
    print(boolean("1")) # True
    print(boolean("foo")) # True
    print(boolean(42)) # True
    print(boolean("000")) # True

    print(boolean(False)) # False
    print(boolean("False")) # False
    print(boolean("Off")) # False
    print(boolean("0")) # False
    print(boolean(())) # False
    print(boolean([])) # False
    print(boolean({})) # False
    ```
    """
    if isinstance(value, str) and value.lower() in ("false", "off", "0"):
        return False

    return bool(value)
