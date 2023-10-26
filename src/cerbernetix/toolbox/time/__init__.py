"""A collection of time related utilities.

It contains:
- `Weekday(day)` - Gets the date of a weekday given a particular date.

Examples:
```python
from cerbernetix.toolbox.time import Weekday, FRIDAY

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
"""
from cerbernetix.toolbox.time.weekday import (
    FRIDAY,
    MONDAY,
    SATURDAY,
    SUNDAY,
    THURSDAY,
    TUESDAY,
    WEDNESDAY,
    Weekday,
)
