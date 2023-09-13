<!-- markdownlint-disable -->

<a href="../toolbox/data/mappers.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.data.mappers`
A collection of data mappers. 



**Examples:**
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


---

<a href="../toolbox/data/mappers.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `passthrough`

```python
passthrough(value: Any) → Any
```

A passthrough mapper. It returns the value as it is. 



**Args:**
 
 - <b>`value`</b> (Any):  The value to map. 



**Returns:**
 
 - <b>`Any`</b>:  The mapped value. 



**Examples:**
 ```python
from toolbox.data import passthrough

print(passthrough("foo")) # "foo"
print(passthrough(42)) # 42
print(passthrough([])) # []
print(passthrough({})) # {}
``` 


---

<a href="../toolbox/data/mappers.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `boolean`

```python
boolean(value: Any) → bool
```

Converts a value to a boolean value. 



**Args:**
 
 - <b>`value`</b> (Any):  A value to cast to boolean. 



**Returns:**
 
 - <b>`bool`</b>:  The value casted to boolean. 



**Examples:**
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


---

<a href="../toolbox/data/mappers.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ValueMapper`
The interface for a value mapper. 

Such an object is responsible for formatting a value in the expected type and format. 

A mapper respecting this interface will be used as follows: 

```python
value = mapper(raw_value)
``` 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
