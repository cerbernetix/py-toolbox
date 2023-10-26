<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/data/value_extractor.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.data.value_extractor`
A tool for extracting values from a set of possible entries. 



**Examples:**
 ```python
from cerbernetix.toolbox.data import ValueExtractor

# Extracts a date from various possible entries
extractor = ValueExtractor(["date", "time", "day"])
data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]

# Build full names from multiple entries
extractor = ValueExtractor(["firstname", "lastname"], " ".join)
data = [
     {"firstname": "John", "lastname": "Smith"},
     {"firstname": "Jane", "lastname": "Doe"},
]
print([extractor.aggregate(row) for row in data]) # ["John Smith", "Jane Doe"]
``` 



---

<a href="../src/cerbernetix/toolbox/data/value_extractor.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ValueExtractor`
Extracts a value from a set of possible entries. 



**Attributes:**
 
 - <b>`entries`</b> (tuple[str], readonly):  The list of possible entries to look at from the structure on which the extractor will be applied. 
 - <b>`mapper`</b> (ValueMapper, readonly):  A mapper for casting the extracted value. 



**Examples:**
 ```python
from cerbernetix.toolbox.data import ValueExtractor

extractor = ValueExtractor(["date", "time", "day"])
data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]
``` 

<a href="../src/cerbernetix/toolbox/data/value_extractor.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(entries: Union[Iterable[str], str], mapper: ValueMapper = None) → None
```

Creates a value extractor. 



**Args:**
 
 - <b>`entries`</b> (Iterable[str] | str):  The list of possible entries to look at from the structure on which the extractor will be applied. 
 - <b>`mapper`</b> (ValueMapper, optional):  A mapper for casting the extracted value. Defaults to None. 



**Raises:**
 
 - <b>`ValueError`</b>:  If an invalid mapper is given. 



**Examples:**
 ```python
from cerbernetix.toolbox.data import ValueExtractor

extractor = ValueExtractor(["date", "time", "day"])
data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]
``` 


---

#### <kbd>property</kbd> entries

The list of possible entries to look at from the structure on which apply the extractor. 



**Returns:**
 
 - <b>`tuple[str]`</b>:  The list of possible entries to look at from the structure on which the extractor will be applied. 

---

#### <kbd>property</kbd> mapper

The mapper applied to cast and format the extracted value. 



**Returns:**
 
 - <b>`ValueMapper`</b>:  The mapper applied to cast and format the extracted value. 



---

<a href="../src/cerbernetix/toolbox/data/value_extractor.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `aggregate`

```python
aggregate(structure: dict) → Any
```

Aggregates a value from the specified structure. 



**Args:**
 
 - <b>`structure`</b> (dict):  The structure from which aggregate the value. 



**Returns:**
 
 - <b>`Any`</b>:  The value aggregated from the structure. 



**Examples:**
 ```python
from cerbernetix.toolbox.data import ValueExtractor

# Build full names from multiple entries
extractor = ValueExtractor(["firstname", "lastname"], " ".join)
data = [
    {"firstname": "John", "lastname": "Smith"},
    {"firstname": "Jane", "lastname": "Doe"},
]
print([extractor.aggregate(row) for row in data]) # ["John Smith", "Jane Doe"]

# Build a list from multiple entries
extractor = ValueExtractor(["value_1", "value_2", "value_3"])
data = [
    {"value_1": 42, "value_2": 12, "value_3": 100},
    {"value_1": 10, "value_2": 20, "value_3": 30},
]
print([extractor.aggregate(row) for row in data]) # [[42, 12, 100], [10, 20, 30]]
``` 

---

<a href="../src/cerbernetix/toolbox/data/value_extractor.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `extract`

```python
extract(structure: dict) → Any
```

Extracts the value from the specified structure. 

It checks successively each entry configured till one exists in the structure, and it returns the first that match. If none of the entries exists in the structure, it returns None. 



**Args:**
 
 - <b>`structure`</b> (dict):  The structure from which extract the value. 



**Returns:**
 
 - <b>`Any`</b>:  The value extracted from the structure. It returns None if no entry is found. 



**Examples:**
 ```python
from cerbernetix.toolbox.data import ValueExtractor

# Extracts a date from various possible entries
extractor = ValueExtractor(["date", "time", "day"])
data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]

# Extracts a number from various possible entries, casting it to an integer
extractor = ValueExtractor(["value", "val", "number"], int)
data = [{"val": "42"}, {"value": 12, {"number": 100}]
print([extractor.extract(row) for row in data]) # [42, 12, 100]
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
