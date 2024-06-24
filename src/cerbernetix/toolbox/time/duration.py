"""Represents a nanosecond duration.

Examples:
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
"""

from __future__ import annotations

from cerbernetix.toolbox.math.utils import limit


class Duration:
    """Represents a nanosecond duration.

    Attributes:
        duration (int): A number of nanoseconds representing the duration.
        precision (int): The desired time precision when converting to string.
        This is the unit of time up to what express the duration. It must have a value from the
        constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS.
        upto (int): The larger unit to present. It must have a value from the constants NANOSECONDS,
        MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS.
        style (str): The string format to apply. Either COUNTER or FULL.

    Examples:
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
    """

    UNITS = (
        1000,  # nanoseconds
        1000,  # microseconds
        1000,  # milliseconds
        60,  # seconds
        60,  # minutes
        24,  # hours
        7,  # days
    )

    NANOSECONDS = 0
    MICROSECONDS = 1
    MILLISECONDS = 2
    SECONDS = 3
    MINUTES = 4
    HOURS = 5
    DAYS = 6
    WEEKS = 7

    TEMPLATE_COUNTER_SEP = ("", "", ".", ":", ":", ":", ":")
    TEMPLATE_COUNTER = (
        "{:03}",  # nanoseconds
        "{:03}",  # microseconds
        "{:03}",  # milliseconds
        "{:02}",  # seconds
        "{:02}",  # minutes
        "{:02}",  # hours
        "{}",  # days
        "{}",  # weeks
    )

    TEMPLATE_FULL_SEP = (" ", " ", " ", " ", " ", " ", " ")
    TEMPLATE_FULL = (
        "{}ns",  # nanoseconds
        "{}us",  # microseconds
        "{}ms",  # milliseconds
        "{}s",  # seconds
        "{}m",  # minutes
        "{}h",  # hours
        "{}d",  # days
        "{}w",  # weeks
    )

    COUNTER = "counter"
    FULL = "full"

    duration: int = 0
    precision: int = SECONDS
    upto: int = HOURS
    style: str = COUNTER

    def __init__(
        self,
        duration: int,
        precision: int = None,
        upto: int = None,
        style: str = None,
    ) -> None:
        """Creates a duration from a number of nanoseconds.

        Args:
            duration (int): A number of nanoseconds representing the duration.
            precision (int, optional): The desired time precision when converting to string.
            This is the unit of time up to what express the duration. It must have a value from the
            constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS.
            Defaults to SECONDS.
            upto (int, optional): The larger unit to present. It must have a value from the
            constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS.
            Defaults to HOURS when the style is COUNTER or WEEKS when the style is FULL.
            style (str, optional): The string format to apply. It must have a value from the
            constants COUNTER or FULL. Defaults to COUNTER.

        Examples:
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
        """
        self.duration = int(duration)

        if precision is not None:
            self.precision = int(precision)

        if style is not None:
            self.style = str(style)

        if upto is None:
            self.upto = self.HOURS if self.style == self.COUNTER else self.WEEKS
        else:
            self.upto = int(upto)

    def split(self, upto: int = None) -> list:
        """Splits the duration into a list containing time units.

        When `upto` is given, the extraction stops by the represented unit.

        Args:
            upto (int, optional): The larger unit to extract. If omitted, use the builtin value. It
            must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS,
            MINUTES, HOURS, DAYS, WEEKS. Defaults to None.

        Returns:
            list: A list containing time units of this form:
            (nanoseconds, microseconds, milliseconds, seconds, minutes, hours, days, weeks)

        Examples:
        ```python
        from cerbernetix.toolbox.time import Duration

        print(Duration(2191325008063004).split()) # (4, 63, 8, 5, 42, 608)
        print(Duration(2191325008063004).split(Duration.WEEKS)) # (4, 63, 8, 5, 42, 8, 4, 3)
        ```
        """
        if upto is None:
            upto = self.upto

        duration = self.duration

        units = []
        for i in range(limit(upto, 0, len(self.UNITS))):
            unit = self.UNITS[i]
            units.append(duration % unit)
            duration = duration // unit
        units.append(duration)

        return units

    def to_string(
        self,
        precision: int = None,
        upto: int = None,
        style: str = None,
    ) -> str:
        """Converts the duration to a string presenting a split by time units.

        Args:
            precision (int, optional): The desired time precision. This is the unit of time up to
            what express the duration. If omitted, use the builtin value. It must have a value from
            the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS,
            WEEKS. Defaults to None.
            upto (int, optional): The larger unit to present. If omitted, use the builtin value. It
            must have a value from the constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS,
            MINUTES, HOURS, DAYS, WEEKS. Defaults to None.
            style (str, optional): The string format to apply. If omitted, use the builtin value.
            It must have a value from the constants COUNTER or FULL. Defaults to None.

        Returns:
            str: A string representing the duration as hours, minutes, seconds...

        Examples:
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
        """
        if precision is None:
            precision = self.precision
        if upto is None:
            upto = self.upto
        if style is None:
            style = self.style

        units = self.split(upto)
        stop = len(units)
        maxi = stop - 1

        if style == self.FULL:
            template = self.TEMPLATE_FULL
            separators = self.TEMPLATE_FULL_SEP

            while maxi > precision and units[maxi] == 0:
                maxi -= 1

            stop = maxi + 1
            units = units[:stop]
        else:
            template = self.TEMPLATE_COUNTER
            separators = self.TEMPLATE_COUNTER_SEP

        placeholders = ""
        for i in range(limit(precision, 0, stop), stop):
            placeholders = template[i] + placeholders
            if i < maxi:
                placeholders = separators[i] + placeholders

        return placeholders.format(*units[::-1])

    def clone(
        self,
        duration: int = None,
        precision: int = None,
        upto: int = None,
        style: str = None,
    ) -> Duration:
        """Clones the instance, allowing to change a few properties.

        Args:
            duration (int, optional): A number of nanoseconds representing the duration. If omitted,
            use the builtin value. Defaults to None.
            precision (int, optional): The desired time precision when converting to string.
            This is the unit of time up to what express the duration. It must have a value from the
            constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS.
            If omitted, use the builtin value. Defaults to None.
            upto (int, optional): The larger unit to present. It must have a value from the
            constants NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS, WEEKS.
            If omitted, use the builtin value. Defaults to None.
            style (str, optional): The string format to apply. It must have a value from the
            constants COUNTER or FULL. If omitted, use the builtin value. Defaults to None.

        Returns:
            Duration: A copy of the current instance.

        Examples:
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
        """
        return Duration(
            self.duration if duration is None else duration,
            self.precision if precision is None else precision,
            self.upto if upto is None else upto,
            self.style if style is None else style,
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
        return self.to_string()

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
        return self.clone(self.duration + int(other))

    def __radd__(self, other) -> Duration:
        """Adds a value to the duration and returns with a new instance.

        Args:
            other (int | float | Duration): The value to add.

        Returns:
            Duration: A new instance containing the result of the addition.
        """
        return self.clone(int(other) + self.duration)

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
        return self.clone(self.duration - int(other))

    def __rsub__(self, other) -> Duration:
        """Subtracts a value from the duration and returns with a new instance.

        Args:
            other (int | float | Duration): The value to add.

        Returns:
            Duration: A new instance containing the result of the subtraction.
        """
        return self.clone(int(other) - self.duration)

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
