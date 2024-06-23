<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/time/timer.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.time.timer`
Captures the time spent. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 00:00:02
sleep(3)

print(timer.stop())    # 00:00:05
sleep(1)

print(timer.duration)  # 00:00:05
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
 - <b>`till_check`</b> (Duration):  The time elapsed between the starting point and the last checkpoint. 
 - <b>`since_check`</b> (Duration):  The time elapsed since the last checkpoint. 
 - <b>`since_stop`</b> (Duration):  The time elapsed since the stopping point. 
 - <b>`duration`</b> (Duration):  The time elapsed since the starting point. 
 - <b>`mean_duration`</b> (Duration):  The average duration of all checkpoints. 
 - <b>`checkpoints`</b> (tuple[Duration]):  The duration for each checkpoint. 
 - <b>`precision`</b> (int):  The desired time precision when converting durations to string. 
 - <b>`upto`</b> (int):  The larger unit to present when converting durations to string. 
 - <b>`style`</b> (sr):  The string format to apply to the duration. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 00:00:02
sleep(3)

print(timer.stop())    # 00:00:05
sleep(1)

print(timer.duration)  # 00:00:05
``` 

<a href="../src/cerbernetix/toolbox/time/timer.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    precision: 'int' = None,
    upto: 'int' = None,
    style: 'str' = None
) → None
```

Creates a timer. 



**Args:**
 
 - <b>`precision`</b> (int, optional):  The desired time precision when converting to string. This is the unit of time up to what express the duration. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. Defaults to SECONDS. 
 - <b>`upto`</b> (int, optional):  The larger unit to present. It must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS. Defaults to HOURS when the style is COUNTER or WEEKS when the style is FULL. 
 - <b>`style`</b> (str, optional):  The string format to apply. It must have a value from the constants COUNTER or FULL. Defaults to COUNTER. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 00:00:02
sleep(3)

print(timer.stop())    # 00:00:05
sleep(1)

print(timer.duration)  # 00:00:05
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
 
 - <b>`tuple[Duration]`</b>:  A tuple containing the time elapsed for each checkpoint. 

---

#### <kbd>property</kbd> duration

Gets the time elapsed since the starting point. 

If the timer is stopped, gets the total time elapsed between the start and stop points. 



**Returns:**
 
 - <b>`Duration`</b>:  The time elapsed since the starting point. 

---

#### <kbd>property</kbd> mean_duration

Gets the average duration of all checkpoints. 

The time elapsed between the stop point and the last checkpoint also counts. 



**Returns:**
 
 - <b>`Duration`</b>:  The average duration of all checkpoints. 

---

#### <kbd>property</kbd> since_check

Gets the time elapsed since the last checkpoint. 

If the timer is stopped, gets the time elapsed between the last checkpoint and and the stop. 



**Returns:**
 
 - <b>`Duration`</b>:  The time elapsed since the last checkpoint. 

---

#### <kbd>property</kbd> since_stop

Gets the time elapsed since the stopping point. 

If the timer is still running, return 0. 



**Returns:**
 
 - <b>`Duration`</b>:  The time elapsed since the stopping point. 

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
 
 - <b>`Duration`</b>:  The time elapsed between the starting point and the last checkpoint. 



---

<a href="../src/cerbernetix/toolbox/time/timer.py#L207"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check`

```python
check() → Duration
```

Capture a new checkpoint. 



**Returns:**
 
 - <b>`Duration`</b>:  The time elapsed since the last checkpoint. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 00:00:02
sleep(3)

print(timer.stop())    # 00:00:05
sleep(1)

print(timer.duration)  # 00:00:05
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L321"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../src/cerbernetix/toolbox/time/timer.py#L269"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

print(timer.stop())    # 00:00:03
sleep(2)

timer.reset()
sleep(1)

print(timer.duration)  # 00:00:01
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stop`

```python
stop() → Duration
```

Stops the timer. 



**Returns:**
 
 - <b>`Duration`</b>:  The time elapsed since the starting point. 



**Examples:**
 ```python
from time import sleep
from cerbernetix.toolbox.time import Timer

timer = Timer()
sleep(2)

print(timer.check())   # 00:00:02
sleep(3)

print(timer.stop())    # 00:00:05
sleep(1)

print(timer.duration)  # 00:00:05
``` 

---

<a href="../src/cerbernetix/toolbox/time/timer.py#L294"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
