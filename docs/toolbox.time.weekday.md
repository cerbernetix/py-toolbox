<!-- markdownlint-disable -->

<a href="../toolbox/time/weekday.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.time.weekday`
A tool for getting the date of a weekday. 



**Examples:**
 ```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

# Get the date of the closest Friday
print(weekday.closest_date("2023-10-01")) # "2023-09-29"
print(weekday.closest_date("2023-10-04")) # "2023-10-06"
print(weekday.closest_date("2023-10-06")) # "2023-10-06"

# Get the date of the next Friday
print(weekday.next_date("2023-10-04")) # "2023-10-06"
print(weekday.next_date("2023-10-06")) # "2023-10-13"

# Get the date of the closest next Friday
print(weekday.next_date("2023-10-06", True)) # "2023-10-06"

# Get the date of the previous Friday
print(weekday.previous_date("2023-10-04")) # "2023-09-29"
print(weekday.previous_date("2023-10-06")) # "2023-09-29"

# Get the date of the closest previous Friday
print(weekday.previous_date("2023-10-06", True)) # "2023-10-06"
``` 

**Global Variables**
---------------
- **MONDAY**
- **TUESDAY**
- **WEDNESDAY**
- **THURSDAY**
- **FRIDAY**
- **SATURDAY**
- **SUNDAY**
- **WEEK**


---

<a href="../toolbox/time/weekday.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Weekday`
Gets the date of a weekday given a particular date. 



**Examples:**
 ```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

# Get the date of the closest Friday
print(weekday.closest_date("2023-10-01")) # "2023-09-29"
print(weekday.closest_date("2023-10-04")) # "2023-10-06"
print(weekday.closest_date("2023-10-06")) # "2023-10-06"

# Get the date of the next Friday
print(weekday.next_date("2023-10-04")) # "2023-10-06"
print(weekday.next_date("2023-10-06")) # "2023-10-13"

# Get the date of the closest next Friday
print(weekday.next_date("2023-10-06", True)) # "2023-10-06"

# Get the date of the previous Friday
print(weekday.previous_date("2023-10-04")) # "2023-09-29"
print(weekday.previous_date("2023-10-06")) # "2023-09-29"

# Get the date of the closest previous Friday
print(weekday.previous_date("2023-10-06", True)) # "2023-10-06"
``` 

<a href="../toolbox/time/weekday.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(day: int) → None
```

Binds a weekday so that we can get a date from it. 



**Args:**
 
 - <b>`day`</b> (int):  The weekday to bind. 

```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

# Get the date of the closest Friday
print(weekday.closest_date("2023-10-01")) # "2023-09-29"
print(weekday.closest_date("2023-10-04")) # "2023-10-06"
print(weekday.closest_date("2023-10-06")) # "2023-10-06"

# Get the date of the next Friday
print(weekday.next_date("2023-10-04")) # "2023-10-06"
print(weekday.next_date("2023-10-06")) # "2023-10-13"

# Get the date of the closest next Friday
print(weekday.next_date("2023-10-06", True)) # "2023-10-06"

# Get the date of the previous Friday
print(weekday.previous_date("2023-10-04")) # "2023-09-29"
print(weekday.previous_date("2023-10-06")) # "2023-09-29"

# Get the date of the closest previous Friday
print(weekday.previous_date("2023-10-06", True)) # "2023-10-06"
``` 




---

<a href="../toolbox/time/weekday.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `closest`

```python
closest(weekday: int = None) → int
```

Gets the number of days from the closest occurrence of the bound weekday. 

If the weekday is None, it uses the current date. 



**Args:**
 
 - <b>`weekday`</b> (int, optional):  The current weekday from which count the days. Defaults to None. 



**Returns:**
 
 - <b>`int`</b>:  The number of days from the closest occurrence of the bound weekday. 



**Examples:**
 ```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

print(weekday.closest(THURSDAY)) # 1
print(weekday.closest(SUNDAY)) # -2
``` 

---

<a href="../toolbox/time/weekday.py#L276"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `closest_date`

```python
closest_date(day: str | date = None) → date
```

Gets the date of the previous occurrence of the weekday with respect to the given date. 

If the date is None, it uses the current date. 



**Args:**
 
 - <b>`day`</b> (str | date, optional):  The date for which get the previous weekday. Defaults to None. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the given date is not a date or a string. ValueError; If the string is not a valid date. 



**Returns:**
 
 - <b>`date`</b>:  The date of the previous occurrence of the weekday. 



**Examples:**
 ```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

# Get the date of the closest Friday
print(weekday.closest_date("2023-10-01")) # "2023-09-29"
print(weekday.closest_date("2023-10-04")) # "2023-10-06"
print(weekday.closest_date("2023-10-06")) # "2023-10-06"
``` 

---

<a href="../toolbox/time/weekday.py#L108"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `next`

```python
next(weekday: int = None) → int
```

Gets the number of days before the next occurrence of the bound weekday. 

If the weekday is None, it uses the current date. 



**Args:**
 
 - <b>`weekday`</b> (int, optional):  The current weekday from which count the days. Defaults to None. 



**Returns:**
 
 - <b>`int`</b>:  The number of days before the next occurrence of the bound weekday. 



**Examples:**
 ```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

print(weekday.next(THURSDAY)) # 1
print(weekday.next(SUNDAY)) # 5
``` 

---

<a href="../toolbox/time/weekday.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `next_date`

```python
next_date(day: str | date = None, closest: bool = False) → date
```

Gets the date of the next occurrence of the weekday with respect to the given date. 

If the date is None, it uses the current date. 



**Args:**
 
 - <b>`date`</b> (str | date, optional):  The date for which get the next weekday. Defaults to None. 
 - <b>`closest`</b> (bool, optional):  Whether the date should be the closest possible or not. If True and the given date is on the expected weekday it will be returned. Otherwise, the date of the next corresponding weekday will be returned. Defaults to False. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the given date is not a date or a string. ValueError; If the string is not a valid date. 



**Returns:**
 
 - <b>`date`</b>:  The date of the next occurrence of the weekday. 



**Examples:**
 ```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

# Get the date of the next Friday
print(weekday.next_date("2023-10-04")) # "2023-10-06"
print(weekday.next_date("2023-10-06")) # "2023-10-13"

# Get the date of the closest next Friday
print(weekday.next_date("2023-10-06", True)) # "2023-10-06"
``` 

---

<a href="../toolbox/time/weekday.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `previous`

```python
previous(weekday: int = None) → int
```

Gets the number of days since the last occurrence of the bound weekday. 

If the weekday is None, it uses the current date. 



**Args:**
 
 - <b>`weekday`</b> (int, optional):  The current weekday from which count the days. Defaults to None. 



**Returns:**
 
 - <b>`int`</b>:  The number of days since the last occurrence of the bound weekday. 



**Examples:**
 ```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

print(weekday.previous(THURSDAY)) # 6
print(weekday.previous(SUNDAY)) # 2
``` 

---

<a href="../toolbox/time/weekday.py#L235"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `previous_date`

```python
previous_date(day: str | date = None, closest: bool = False) → date
```

Gets the date of the previous occurrence of the weekday with respect to the given date. 

If the date is None, it uses the current date. 



**Args:**
 
 - <b>`date`</b> (str | date, optional):  The date for which get the previous weekday. Defaults to None. 
 - <b>`closest`</b> (bool, optional):  Whether the date should be the closest possible or not. If True and the given date is on the expected weekday it will be returned. Otherwise, the date of the previous corresponding weekday will be returned. Defaults to False. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the given date is not a date or a string. ValueError; If the string is not a valid date. 



**Returns:**
 
 - <b>`date`</b>:  The date of the previous occurrence of the weekday. 



**Examples:**
 ```python
from toolbox.time import Weekday, FRIDAY

weekday = Weekday(FRIDAY)

# Get the date of the previous Friday
print(weekday.previous_date("2023-10-04")) # "2023-09-29"
print(weekday.previous_date("2023-10-06")) # "2023-09-29"

# Get the date of the closest previous Friday
print(weekday.previous_date("2023-10-06", True)) # "2023-10-06"
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
