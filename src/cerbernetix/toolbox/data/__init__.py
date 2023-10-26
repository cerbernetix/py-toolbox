"""A collection of data utilities.

It contains:
- Value mappers:
    - `passthrough(value)` - A passthrough mapper. It returns the value as it is.
    - `boolean(value)` - Converts a value to a boolean value.
    - `decimal(separator, thousands)` - Creates a mapper for casting decimal values to floats.
- `ValueExtractor(entries, mapper)` - A tool for extracting values from a set of possible entries.

Examples:
```python
from cerbernetix.toolbox.data import mappers
from cerbernetix.toolbox.data import ValueExtractor

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

# Extracts a date from various possible entries
extractor = ValueExtractor(["date", "time", "day"])
data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]

# Extracts a number from various possible entries, casting it to an integer
extractor = ValueExtractor(["value", "val", "number"], int)
data = [{"val": "42"}, {"value": 12, {"number": 100}]
print([extractor.extract(row) for row in data]) # [42, 12, 100]

# Build full names from multiple entries
extractor = ValueExtractor(["firstname", "lastname"], " ".join)
data = [
    {"firstname": "John", "lastname": "Smith"},
    {"firstname": "Jane", "lastname": "Doe"},
]
print([extractor.aggregate(row) for row in data]) # ["John Smith", "Jane Doe"]
```
"""
from cerbernetix.toolbox.data.mappers import ValueMapper, boolean, decimal, passthrough
from cerbernetix.toolbox.data.value_extractor import ValueExtractor
