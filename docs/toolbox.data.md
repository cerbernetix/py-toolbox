<!-- markdownlint-disable -->

<a href="../toolbox/data/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.data`
A collection of data utilities. 

It contains: 
- Value mappers: 
    - `passthrough(value)` - A passthrough mapper. It returns the value as it is. 
    - `boolean(value)` - Converts a value to a boolean value. 
- `ValueExtractor()` - A tool for extracting values from a set of possible entries. 



**Examples:**
 ```python
from toolbox.data import mappers
from toolbox.data import ValueExtractor

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

# Extracts a date from various possible entries
extractor = ValueExtractor(["date", "time", "day"])
data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]

# Extracts a number from various possible entries, casting it to an integer
extractor = ValueExtractor(["value", "val", "number"], int)
data = [{"val": "42"}, {"value": 12, {"number": 100}]
print([extractor.extract(row) for row in data]) # [42, 12, 100]
``` 

**Global Variables**
---------------
- **mappers**
- **value_extractor**




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
