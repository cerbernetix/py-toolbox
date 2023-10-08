"""A tool for getting the date of a weekday.

Examples:
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
"""
import datetime
from datetime import date

# Represent each weekday per position in the week
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# The number of days in a week
WEEK = 7


class Weekday:
    """Gets the date of a weekday given a particular date.

    Examples:
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
    """

    def __init__(self, day: int) -> None:
        """Binds a weekday so that we can get a date from it.

        Args:
            day (int): The weekday to bind.

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
        """
        self.day = day

    def next(self, weekday: int = None) -> int:
        """Gets the number of days before the next occurrence of the bound weekday.

        If the weekday is None, it uses the current date.

        Args:
            weekday (int, optional): The current weekday from which count the days.
            Defaults to None.

        Returns:
            int: The number of days before the next occurrence of the bound weekday.

        Examples:
        ```python
        from toolbox.time import Weekday, FRIDAY

        weekday = Weekday(FRIDAY)

        print(weekday.next(THURSDAY)) # 1
        print(weekday.next(SUNDAY)) # 5
        ```
        """
        if weekday is None:
            weekday = datetime.date.today().weekday()

        return (WEEK - weekday + self.day - 1) % WEEK + 1

    def previous(self, weekday: int = None) -> int:
        """Gets the number of days since the last occurrence of the bound weekday.

        If the weekday is None, it uses the current date.

        Args:
            weekday (int, optional): The current weekday from which count the days.
            Defaults to None.

        Returns:
            int: The number of days since the last occurrence of the bound weekday.

        Examples:
        ```python
        from toolbox.time import Weekday, FRIDAY

        weekday = Weekday(FRIDAY)

        print(weekday.previous(THURSDAY)) # 6
        print(weekday.previous(SUNDAY)) # 2
        ```
        """
        if weekday is None:
            weekday = datetime.date.today().weekday()

        return (weekday + WEEK - self.day - 1) % WEEK + 1

    def closest(self, weekday: int = None) -> int:
        """Gets the number of days from the closest occurrence of the bound weekday.

        If the weekday is None, it uses the current date.

        Args:
            weekday (int, optional): The current weekday from which count the days.
            Defaults to None.

        Returns:
            int: The number of days from the closest occurrence of the bound weekday.

        Examples:
        ```python
        from toolbox.time import Weekday, FRIDAY

        weekday = Weekday(FRIDAY)

        print(weekday.closest(THURSDAY)) # 1
        print(weekday.closest(SUNDAY)) # -2
        ```
        """
        if weekday is None:
            weekday = datetime.date.today().weekday()

        if weekday == self.day:
            return 0

        to_next = self.next(weekday)
        from_previous = self.previous(weekday)
        return -from_previous if to_next > from_previous else to_next

    def next_date(self, day: str | date = None, closest: bool = False) -> date:
        """Gets the date of the next occurrence of the weekday with respect to the given date.

        If the date is None, it uses the current date.

        Args:
            date (str | date, optional): The date for which get the next weekday.
            Defaults to None.
            closest (bool, optional): Whether the date should be the closest possible or not.
            If True and the given date is on the expected weekday it will be returned. Otherwise,
            the date of the next corresponding weekday will be returned. Defaults to False.

        Raises:
            TypeError: If the given date is not a date or a string.
            ValueError; If the string is not a valid date.

        Returns:
            date: The date of the next occurrence of the weekday.

        Examples:
        ```python
        from toolbox.time import Weekday, FRIDAY

        weekday = Weekday(FRIDAY)

        # Get the date of the next Friday
        print(weekday.next_date("2023-10-04")) # "2023-10-06"
        print(weekday.next_date("2023-10-06")) # "2023-10-13"

        # Get the date of the closest next Friday
        print(weekday.next_date("2023-10-06", True)) # "2023-10-06"
        ```
        """
        day = self._get_date(day)
        weekday = day.weekday()

        if closest and weekday == self.day:
            return day

        return day + datetime.timedelta(days=self.next(weekday))

    def previous_date(self, day: str | date = None, closest: bool = False) -> date:
        """Gets the date of the previous occurrence of the weekday with respect to the given date.

        If the date is None, it uses the current date.

        Args:
            date (str | date, optional): The date for which get the previous weekday.
            Defaults to None.
            closest (bool, optional): Whether the date should be the closest possible or not.
            If True and the given date is on the expected weekday it will be returned. Otherwise,
            the date of the previous corresponding weekday will be returned. Defaults to False.

        Raises:
            TypeError: If the given date is not a date or a string.
            ValueError; If the string is not a valid date.

        Returns:
            date: The date of the previous occurrence of the weekday.

        Examples:
        ```python
        from toolbox.time import Weekday, FRIDAY

        weekday = Weekday(FRIDAY)

        # Get the date of the previous Friday
        print(weekday.previous_date("2023-10-04")) # "2023-09-29"
        print(weekday.previous_date("2023-10-06")) # "2023-09-29"

        # Get the date of the closest previous Friday
        print(weekday.previous_date("2023-10-06", True)) # "2023-10-06"
        ```
        """
        day = self._get_date(day)
        weekday = day.weekday()

        if closest and weekday == self.day:
            return day

        return day - datetime.timedelta(days=self.previous(weekday))

    def closest_date(self, day: str | date = None) -> date:
        """Gets the date of the previous occurrence of the weekday with respect to the given date.

        If the date is None, it uses the current date.

        Args:
            day (str | date, optional): The date for which get the previous weekday.
            Defaults to None.

        Raises:
            TypeError: If the given date is not a date or a string.
            ValueError; If the string is not a valid date.

        Returns:
            date: The date of the previous occurrence of the weekday.

        Examples:
        ```python
        from toolbox.time import Weekday, FRIDAY

        weekday = Weekday(FRIDAY)

        # Get the date of the closest Friday
        print(weekday.closest_date("2023-10-01")) # "2023-09-29"
        print(weekday.closest_date("2023-10-04")) # "2023-10-06"
        print(weekday.closest_date("2023-10-06")) # "2023-10-06"
        ```
        """
        day = self._get_date(day)
        weekday = day.weekday()

        if weekday == self.day:
            return day

        return day + datetime.timedelta(self.closest(weekday))

    def _get_date(self, day: str | date = None) -> date:
        """Gets a valid date.

        If the date is None, returns the current date.

        Args:
            date (str | date, optional): The date to validate. Default to None.

        Raises:
            TypeError: If the given date is not a date or a string.
            ValueError; If the string is not a valid date.

        Returns:
            date: The date object.
        """
        if day is None:
            day = datetime.date.today()
        elif isinstance(day, str):
            day = datetime.date.fromisoformat(day)

        if not isinstance(day, date):
            raise TypeError("The date must be a date or a string")

        return day
