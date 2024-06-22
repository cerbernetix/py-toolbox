"""Represents a nanosecond duration.

Examples:
```python
import time
from cerbernetix.toolbox.time import Duration

print(Duration(123123456789)) # "0:02:03"
print(Duration(123123456789).duration) # 123123456789

d = Duration(time.monotonic_ns())
d += 123456789

if d > time.monotonic_ns():
    print("not yet!)
```
"""

from __future__ import annotations

from cerbernetix.toolbox.math.utils import limit


class Duration:
    """Represents a nanosecond duration.

    Attributes:
        duration (int): A number of nanoseconds representing the duration.
        precision (int): The desired time precision when converting to string.
        This is the unit of time up to what express the duration.

    Examples:
    ```python
    import time
    from cerbernetix.toolbox.time import Duration

    print(Duration(123123456789)) # "0:02:03"
    print(Duration(123123456789).duration) # 123123456789

    d = Duration(time.monotonic_ns())
    d += 123456789

    if d > time.monotonic_ns():
        print("not yet!)
    ```
    """

    PRECISION_NANOSECONDS = 6
    PRECISION_MICROSECONDS = 5
    PRECISION_MILLISECONDS = 4
    PRECISION_SECONDS = 3
    PRECISION_MINUTES = 2
    PRECISION_HOURS = 1

    duration: int = 0
    precision: int = PRECISION_SECONDS

    def __init__(self, duration: int, precision: int = PRECISION_SECONDS) -> None:
        """Creates a duration from a number of nanoseconds.

        Args:
            duration (int): A number of nanoseconds representing the duration.
            precision (int, optional): The desired time precision when converting to string.
            This is the unit of time up to what express the duration. Defaults to PRECISION_SECONDS.

        Examples:
        ```python
        import time
        from cerbernetix.toolbox.time import Duration

        print(Duration(123123456789)) # "0:02:03"
        print(Duration(123123456789).duration) # 123123456789

        d = Duration(time.monotonic_ns())
        d += 123456789

        if d > time.monotonic_ns():
            print("not yet!)
        ```
        """
        self.duration = int(duration)
        self.precision = int(precision)

    def split(self) -> tuple:
        """Splits the duration into a tuple containing time units.

        Returns:
            tuple: A tuple containing time units of this form:
            (hours, minutes, seconds, microseconds, nanoseconds)

        Examples:
        ```python
        from cerbernetix.toolbox.time import Duration

        print(Duration(123123456789).split()) # (0, 2, 3, 123, 456, 789)
        ```
        """
        duration = self.duration
        ns, duration = duration % 1000, duration // 1000
        mi, duration = duration % 1000, duration // 1000
        ms, duration = duration % 1000, duration // 1000
        s, duration = duration % 60, duration // 60
        m, h = duration % 60, duration // 60
        return (h, m, s, ms, mi, ns)

    def to_string(self, precision: int = None) -> str:
        """Converts the duration to a string presenting a split by time units.

        Args:
            precision (int, optional): The desired time precision. This is the unit of time up to
            what express the duration. If omitted, use the builtin value.  Defaults to None.

        Returns:
            str: A string representing the duration as hours, minutes, and seconds...

        Examples:
        ```python
        from cerbernetix.toolbox.time import Duration

        print(Duration(123123456789).to_string()) # "0:02:03"
        print(Duration(123123456789).to_string(Timer.PRECISION_NANOSECONDS)) # "0:02:03:123:456:789"
        ```
        """
        if precision is None:
            precision = self.precision

        units = self.split()
        precision = limit(precision, 1, len(units))
        return ":".join(
            [
                str(unit).rjust(min((i + 1) // 2 + 1, 3), "0")
                for i, unit in enumerate(units[:precision])
            ]
        )

    def __str__(self) -> str:
        """Converts the duration to a string presenting a split by time units.

        Returns:
            str: A string representing the duration as hours, minutes, and seconds...
        """
        return self.to_string()

    def __repr__(self) -> str:
        """Returns with a string representation of the duration.

        Returns:
            str: The string representation of the duration.
        """
        return f"Duration({self.duration}, {self.precision})"

    def __index__(self) -> int:
        """Converts to a numeric value.

        Returns:
            int: The duration.
        """
        return self.duration

    def __add__(self, other: int | float | Duration) -> Duration:
        """Adds a value to the duration and returns with a new instance.

        Args:
            other (int | float | Duration): The value to add.

        Returns:
            Duration: A new instance containing the result of the addition.
        """
        return Duration(self.duration + int(other), self.precision)

    def __radd__(self, other) -> Duration:
        """Adds a value to the duration and returns with a new instance.

        Args:
            other (int | float | Duration): The value to add.

        Returns:
            Duration: A new instance containing the result of the addition.
        """
        return Duration(int(other) + self.duration, self.precision)

    def __iadd__(self, other) -> Duration:
        """Adds a value to the duration inplace.

        Args:
            other (int | float | Duration): The value to add.

        Returns:
            Duration: The instance containing the result of the addition.
        """
        self.duration += int(other)
        return self

    def __sub__(self, other) -> Duration:
        """Subtracts a value from the duration and returns with a new instance.

        Args:
            other (int | float | Duration): The value to add.

        Returns:
            Duration: A new instance containing the result of the subtraction.
        """
        return Duration(self.duration - int(other), self.precision)

    def __rsub__(self, other) -> Duration:
        """Subtracts a value from the duration and returns with a new instance.

        Args:
            other (int | float | Duration): The value to add.

        Returns:
            Duration: A new instance containing the result of the subtraction.
        """
        return Duration(int(other) - self.duration, self.precision)

    def __isub__(self, other) -> Duration:
        """Subtracts a value from the duration inplace.

        Args:
            other (int | float | Duration): The value to add.

        Returns:
            Duration: The instance containing the result of the subtraction.
        """
        self.duration -= int(other)
        return self

    def __eq__(self, value: object) -> bool:
        """Compares the duration with another compatible value.

        Args:
            value (object): The other value to compare with

        Returns:
            bool: True if the values are equal.
        """
        return self.duration == int(value)

    def __ne__(self, value: object) -> bool:
        """Compares the duration with another compatible value.

        Args:
            value (object): The other value to compare with

        Returns:
            bool: True if the values are not equal.
        """
        return self.duration != int(value)

    def __lt__(self, value: object) -> bool:
        """Compares the duration with another compatible value.

        Args:
            value (object): The other value to compare with

        Returns:
            bool: True if the duration is lower than the value.
        """
        return self.duration < int(value)

    def __le__(self, value: object) -> bool:
        """Compares the duration with another compatible value.

        Args:
            value (object): The other value to compare with

        Returns:
            bool: True if the duration is lower than or equal the value.
        """
        return self.duration <= int(value)

    def __gt__(self, value: object) -> bool:
        """Compares the duration with another compatible value.

        Args:
            value (object): The other value to compare with

        Returns:
            bool: True if the duration is greater than the value.
        """
        return self.duration > int(value)

    def __ge__(self, value: object) -> bool:
        """Compares the duration with another compatible value.

        Args:
            value (object): The other value to compare with

        Returns:
            bool: True if the duration is greater than or equal the value.
        """
        return self.duration >= int(value)
