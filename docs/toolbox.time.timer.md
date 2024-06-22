<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/time/timer.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.time.timer`
Capture the time spent. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 0:0:2
sleep(3)

print(timer.stop())    # 0:0:5
sleep(1)

print(timer.duration)  # 0:0:5
``` 



---

<a href="../src/cerbernetix/toolbox/time/timer.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Timer`
Capture the time spent. 



**Attributes:**
 
 - <b>`started_at`</b> (int):  The start timestamp. 
 - <b>`checked_at`</b> (int):  The timestamp of the last checkpoint. 
 - <b>`stopped_at`</b> (int):  The stop timestamp, or None if the timer is still running. 
 - <b>`stopped`</b> (bool):  True if the timer is stopped, False otherwise. 
 - <b>`till_check`</b> (int):  The time elapsed between the starting point and the last checkpoint. 
 - <b>`since_check`</b> (int):  The time elapsed since the last checkpoint. 
 - <b>`since_stop`</b> (int):  The time elapsed since the stopping point. 
 - <b>`duration`</b> (int):  The time elapsed since the starting point. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 0:0:2
sleep(3)

print(timer.stop())    # 0:0:5
sleep(1)

print(timer.duration)  # 0:0:5
``` 

<a href="../src/cerbernetix/toolbox/time/timer.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__() → None
```

Creates a timer. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 0:0:2
sleep(3)

print(timer.stop())    # 0:0:5
sleep(1)

print(timer.duration)  # 0:0:5
``` 


---

#### <kbd>property</kbd> checked_at

Gets the timestamp of the last checkpoint. 



**Returns:**
 
 - <b>`int`</b>:  The last checkpoint timestamp. 

---

#### <kbd>property</kbd> checkpoints

Gets the duration for each checkpoint. 

The time elapsed between the stop point and the last checkpoint also counts. 



**Returns:**
 
 - <b>`tuple[int]`</b>:  A tuple containing the time elapsed for each checkpoint. 

---

#### <kbd>property</kbd> duration

Gets the time elapsed since the starting point. 

If the timer is stopped, gets the total time elapsed between the start and stop points. 



**Returns:**
 
 - <b>`int`</b>:  The time elapsed since the starting point. 

---

#### <kbd>property</kbd> mean_duration

Gets the average duration of all checkpoints. 

The time elapsed between the stop point and the last checkpoint also counts. 



**Returns:**
 
 - <b>`int`</b>:  The average duration of all checkpoints. 

---

#### <kbd>property</kbd> since_check

Gets the time elapsed since the last checkpoint. 

If the timer is stopped, gets the time elapsed between the last checkpoint and and the stop. 



**Returns:**
 
 - <b>`int`</b>:  The time elapsed since the last checkpoint. 

---

#### <kbd>property</kbd> since_stop

Gets the time elapsed since the stopping point. 

If the timer is still running, return 0. 



**Returns:**
 
 - <b>`int`</b>:  The time elapsed since the stopping point. 

---

#### <kbd>property</kbd> started_at

Gets the timestamp of the starting point. 



**Returns:**
 
 - <b>`int`</b>:  The start timestamp. 

---

#### <kbd>property</kbd> stopped

Tells if the timer was stopped. 



**Returns:**
 
 - <b>`bool`</b>:  True if the timer is stopped, False otherwise. 

---

#### <kbd>property</kbd> stopped_at

Gets the timestamp of the stopping point. 



**Returns:**
 
 - <b>`int`</b>:  The stop timestamp, or None if the timer is still running. 

---

#### <kbd>property</kbd> till_check

Gets the time elapsed between the starting point and the last checkpoint. 



**Returns:**
 
 - <b>`int`</b>:  The time elapsed between the starting point and the last checkpoint. 



---

<a href="../src/cerbernetix/toolbox/time/timer.py#L188"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check`

```python
check() → int
```

Capture a new checkpoint. 



**Returns:**
 
 - <b>`int`</b>:  The time elapsed since the last checkpoint. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 0:0:2
sleep(3)

print(timer.stop())    # 0:0:5
sleep(1)

print(timer.duration)  # 0:0:5
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L302"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `current`

```python
current() → int
```

Gets the current timestamp or the stop timestamp depending if the timer is still running. 



**Returns:**
 
 - <b>`int`</b>:  The current timestamp if the timer is still running, otherwise the stop timestamp. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

# print a new timestamp
print(time.current())
sleep(3)

time.stop()
sleep(1)

# print a the stop timestamp
print(time.current())
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L359"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `duration_to_string`

```python
duration_to_string(duration: 'int', precision: 'int' = 3) → str
```

Converts a duration in nanoseconds to a string presenting a split by time units. 



**Args:**
 
 - <b>`duration`</b> (int):  A duration expressed in nanoseconds. 
 - <b>`precision`</b> (int, optional):  The desired time precision. This is the unit of time up to what express the duration. Defaults to PRECISION_SECONDS. 



**Returns:**
 
 - <b>`str`</b>:  A string representing the duration as hours, minutes, and seconds. 



**Examples:**
 ```python
from cerbernetix.toolbox.time import Timer

print(Timer.duration_to_string(123456789)) # "0:02:03"
print(Timer.duration_to_string(123456789, Timer.PRECISION_NANOSECONDS)) # "0:02:03:456:789"
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L250"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset`

```python
reset() → None
```

Resets the timer. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(3)

print(timer.stop())    # 0:0:3
sleep(2)

timer.reset()
sleep(1)

print(timer.duration)  # 0:0:1
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L329"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `split_duration`

```python
split_duration(duration: 'int') → tuple
```

Splits a duration in nanoseconds to a tuple containing time units. 



**Args:**
 
 - <b>`duration`</b> (int):  A duration expressed in nanoseconds. 



**Returns:**
 
 - <b>`tuple`</b>:  A tuple containing time units of this form: (hours, minutes, seconds, microseconds, nanoseconds) 



**Examples:**
 ```python
from cerbernetix.toolbox.time import Timer

print(Timer.split_duration(123456789)) # (0, 2, 3, 456, 789)
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stop`

```python
stop() → int
```

Stops the timer. 



**Returns:**
 
 - <b>`int`</b>:  The time elapsed since the starting point. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 0:0:2
sleep(3)

print(timer.stop())    # 0:0:5
sleep(1)

print(timer.duration)  # 0:0:5
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L275"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `timestamp`

```python
timestamp() → int
```

Gets the current timestamp. 



**Returns:**
 
 - <b>`int`</b>:  The current timestamp. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

# print a new timestamp
print(time.timestamp())
sleep(3)

time.stop()
sleep(1)

# print a new timestamp
print(time.timestamp())
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
