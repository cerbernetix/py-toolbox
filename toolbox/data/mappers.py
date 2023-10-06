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

# Gets a float
mapper = mappers.decimal(",")
print(mapper("3,14")) # 3.14

mapper = mappers.decimal(",", ".")
print(mapper("3.753.323,184")) # 3753323.184
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


def decimal(separator: str = None, thousands: str = None) -> ValueMapper:
    """Creates a mapper for casting decimal values to floats.

    Args:
        separator (str, optional): The decimal separator. Defaults to None.
        thousands (str, optional): An optional thousands separator. Defaults to None.

    Returns:
        ValueMapper: Returns a mapper function that can be used for casting a decimal
        value into a float.

    Examples:
    ```python
    from toolbox.data import decimal

    mapper = decimal(",")
    print(mapper("3,14")) # 3.14

    mapper = decimal(",", ".")
    print(mapper("3.753.323,184")) # 3753323.184
    ```
    """

    def mapper(value: str) -> float:
        value = str(value)

        if thousands is not None:
            value = value.replace(thousands, "")

        if separator is not None:
            value = value.replace(separator, ".")

        return float(value)

    return mapper
