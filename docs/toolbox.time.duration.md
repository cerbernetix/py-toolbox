<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/time/duration.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.time.duration`
Represents a nanosecond duration. 



**Examples:**
 ```python
import time
from cerbernetix.toolbox.time import Duration

print(Duration(0))
# "00:00:00"

print(Duration(2191325008063004))
# "608:42:05"

print(Duration(2191325008063004, precision=Duration.NANOSECONDS, upto=Duration.WEEKS))
# "3:4:08:42:05.008063004"

print(Duration(2191325008063004, upto=Duration.WEEKS))
# "3:4:08:42:05"

print(Duration(2191325008063004, precision=Duration.SECONDS, upto=Duration.HOURS))
# "608:42:05"

print(Duration(
     2191325008063004, precision=Duration.NANOSECONDS, upto=Duration.WEEKS, style=Duration.FULL
))
# "3w 4d 8h 42m 5s 8ms 63us 4ns"

print(Duration(2191325008063004).duration)
# 2191325008063004

d = Duration(time.monotonic_ns())
d += 123456789

if d > time.monotonic_ns():
     print("not yet!)
``` 



---

<a href="../src/cerbernetix/toolbox/time/duration.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Duration`
Represents a nanosecond duration. 



**Attributes:**
 
 - <b>`duration`</b> (int):  A number of nanoseconds representing the duration. 
 - <b>`precision`</b> (int):  The desired time precision when converting to string. This is the unit of time up to what express the duration. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. 
 - <b>`upto`</b> (int):  The larger unit to present. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. 
 - <b>`style`</b> (str):  The string format to apply. Either COUNTER or FULL. 



**Examples:**
 ```python
import time
from cerbernetix.toolbox.time import Duration

print(Duration(2191325008063004))
# "608:42:05"

print(Duration(2191325008063004, upto=Duration.WEEKS))
# "3:4:08:42:05"

print(Duration(2191325008063004, style=Duration.FULL))
# "608h 42m 5s"

print(Duration(2191325008063004, precision=Duration.NANOSECONDS, style=Duration.FULL))
# "608h 42m 5s 8ms 63us 4ns"

print(Duration(2191325008063004).duration)
# 2191325008063004

d = Duration(time.monotonic_ns())
d += 123456789

if d > time.monotonic_ns():
    print("not yet!)
``` 

<a href="../src/cerbernetix/toolbox/time/duration.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    duration: 'int',
    precision: 'int' = None,
    upto: 'int' = None,
    style: 'str' = None
) → None
```

Creates a duration from a number of nanoseconds. 



**Args:**
 
 - <b>`duration`</b> (int):  A number of nanoseconds representing the duration. 
 - <b>`precision`</b> (int, optional):  The desired time precision when converting to string. This is the unit of time up to what express the duration. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. Defaults to SECONDS. 
 - <b>`upto`</b> (int, optional):  The larger unit to present. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. Defaults to HOURS when the style is COUNTER or WEEKS when the style is FULL. 
 - <b>`style`</b> (str, optional):  The string format to apply. It must have a value from the constants COUNTER or FULL. Defaults to COUNTER. 



**Examples:**
 ```python
import time
from cerbernetix.toolbox.time import Duration

print(Duration(0))
# "00:00:00"

print(Duration(2191325008063004))
# "608:42:05"

print(Duration(2191325008063004, precision=Duration.NANOSECONDS, upto=Duration.WEEKS))
# "3:4:08:42:05.008063004"

print(Duration(
    2191325008063004, precision=Duration.NANOSECONDS, style=Duration.FULL
))
# "608h 42m 5s 8ms 63us 4ns"

print(Duration(2191325008063004).duration)
# 2191325008063004
``` 




---

<a href="../src/cerbernetix/toolbox/time/duration.py#L299"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clone`

```python
clone(
    duration: 'int' = None,
    precision: 'int' = None,
    upto: 'int' = None,
    style: 'str' = None
) → Duration
```

Clones the instance, allowing to change a few properties. 



**Args:**
 
 - <b>`duration`</b> (int, optional):  A number of nanoseconds representing the duration. If omitted, use the builtin value. Defaults to None. 
 - <b>`precision`</b> (int, optional):  The desired time precision when converting to string. This is the unit of time up to what express the duration. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. If omitted, use the builtin value. Defaults to None. 
 - <b>`upto`</b> (int, optional):  The larger unit to present. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. If omitted, use the builtin value. Defaults to None. 
 - <b>`style`</b> (str, optional):  The string format to apply. It must have a value from the constants COUNTER or FULL. If omitted, use the builtin value. Defaults to None. 



**Returns:**
 
 - <b>`Duration`</b>:  A copy of the current instance. 



**Examples:**
 ```python
from cerbernetix.toolbox.time import Duration

duration1 = Duration(2191325008063004)
print(duration1.to_string())
# "608:42:05"

duration2 = duration1.clone()
print(duration2.to_string())
# "608:42:05"

duration3 = duration1.clone(precision=Duration.NANOSECONDS)
print(duration3.to_string())
# "608:42:05.008063004"
``` 

---

<a href="../src/cerbernetix/toolbox/time/duration.py#L192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `split`

```python
split(upto: 'int' = None) → list
```

Splits the duration into a list containing time units. 

When `upto` is given, the extraction stops by the represented unit. 



**Args:**
 
 - <b>`upto`</b> (int, optional):  The larger unit to extract. If omitted, use the builtin value. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. Defaults to None. 



**Returns:**
 
 - <b>`list`</b>:  A list containing time units of this form: (nanoseconds, microseconds, milliseconds, seconds, minutes, hours, days, weeks) 



**Examples:**
 ```python
from cerbernetix.toolbox.time import Duration

print(Duration(2191325008063004).split()) # (4, 63, 8, 5, 42, 608)
print(Duration(2191325008063004).split(Duration.WEEKS)) # (4, 63, 8, 5, 42, 8, 4, 3)
``` 

---

<a href="../src/cerbernetix/toolbox/time/duration.py#L228"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_string`

```python
to_string(
    precision: 'int' = None,
    upto: 'int' = None,
    style: 'str' = None
) → str
```

Converts the duration to a string presenting a split by time units. 



**Args:**
 
 - <b>`precision`</b> (int, optional):  The desired time precision. This is the unit of time up to what express the duration. If omitted, use the builtin value. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. Defaults to None. 
 - <b>`upto`</b> (int, optional):  The larger unit to present. If omitted, use the builtin value. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. Defaults to None. 
 - <b>`style`</b> (str, optional):  The string format to apply. If omitted, use the builtin value. It must have a value from the constants COUNTER or FULL. Defaults to None. 



**Returns:**
 
 - <b>`str`</b>:  A string representing the duration as hours, minutes, seconds... 



**Examples:**
 ```python
from cerbernetix.toolbox.time import Duration

print(Duration(2191325008063004).to_string())
# "608:42:05"

print(Duration(2191325008063004).to_string(Duration.NANOSECONDS))
# "608:42:05.008063004"

print(Duration(2191325008063004).to_string(upto=Duration.WEEKS))
# "3:4:08:42:05"

print(Duration(2191325008063004).to_string(style=Duration.FULL))
# "608h 42m 5s"
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
