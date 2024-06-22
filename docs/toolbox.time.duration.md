<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/time/duration.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.time.duration`
Represents a nanosecond duration. 



**Examples:**
 ```python
import time
from cerbernetix.toolbox.time import Duration

print(Duration(123456789)) # "0:02:03"
print(Duration(123456789).duration) # 123456789

d = Duration(time.monotonic_ns())
d += 123456789

if d > time.monotonic_ns():
     print("not yet!)
``` 



---

<a href="../src/cerbernetix/toolbox/time/duration.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Duration`
Represents a nanosecond duration. 



**Attributes:**
 
 - <b>`duration`</b> (int):  A number of nanoseconds representing the duration. 
 - <b>`precision`</b> (int):  The desired time precision when converting to string. This is the unit of time up to what express the duration. 



**Examples:**
 ```python
import time
from cerbernetix.toolbox.time import Duration

print(Duration(123456789)) # "0:02:03"
print(Duration(123456789).duration) # 123456789

d = Duration(time.monotonic_ns())
d += 123456789

if d > time.monotonic_ns():
    print("not yet!)
``` 

<a href="../src/cerbernetix/toolbox/time/duration.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(duration: 'int', precision: 'int' = 3) → None
```

Creates a duration from a number of nanoseconds. 



**Args:**
 
 - <b>`duration`</b> (int):  A number of nanoseconds representing the duration. 
 - <b>`precision`</b> (int, optional):  The desired time precision when converting to string. This is the unit of time up to what express the duration. Defaults to PRECISION_SECONDS. 



**Examples:**
 ```python
import time
from cerbernetix.toolbox.time import Duration

print(Duration(123456789)) # "0:02:03"
print(Duration(123456789).duration) # 123456789

d = Duration(time.monotonic_ns())
d += 123456789

if d > time.monotonic_ns():
    print("not yet!)
``` 




---

<a href="../src/cerbernetix/toolbox/time/duration.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `split`

```python
split() → tuple
```

Splits the duration into a tuple containing time units. 



**Returns:**
 
 - <b>`tuple`</b>:  A tuple containing time units of this form: (hours, minutes, seconds, microseconds, nanoseconds) 



**Examples:**
 ```python
from cerbernetix.toolbox.time import Duration

print(Duration(123456789).split()) # (0, 2, 3, 456, 789)
``` 

---

<a href="../src/cerbernetix/toolbox/time/duration.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_string`

```python
to_string(precision: 'int' = None) → str
```

Converts the duration to a string presenting a split by time units. 



**Args:**
 
 - <b>`precision`</b> (int, optional):  The desired time precision. This is the unit of time up to what express the duration. If omitted, use the builtin value.  Defaults to None. 



**Returns:**
 
 - <b>`str`</b>:  A string representing the duration as hours, minutes, and seconds... 



**Examples:**
 ```python
from cerbernetix.toolbox.time import Duration

print(Duration(123456789).to_string()) # "0:02:03"
print(Duration(123456789).to_string(Timer.PRECISION_NANOSECONDS)) # "0:02:03:456:789"
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
