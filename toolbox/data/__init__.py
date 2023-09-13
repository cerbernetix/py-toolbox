"""A collection of data utilities.

It contains:
- Value mappers:
    - `passthrough(value)` - A passthrough mapper. It returns the value as it is.
    - `boolean(value)` - Converts a value to a boolean value.

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
from toolbox.data.mappers import ValueMapper, boolean, passthrough
