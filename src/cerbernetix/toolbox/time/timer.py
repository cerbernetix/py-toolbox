"""Capture the time spent.

Examples:
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
"""

from __future__ import annotations

import time

from cerbernetix.toolbox.math.utils import limit


class Timer:
    """Capture the time spent.

    Attributes:
        started_at (int): The start timestamp.
        checked_at (int): The timestamp of the last checkpoint.
        stopped_at (int): The stop timestamp, or None if the timer is still running.
        stopped (bool): True if the timer is stopped, False otherwise.
        till_check (int): The time elapsed between the starting point and the last checkpoint.
        since_check (int): The time elapsed since the last checkpoint.
        since_stop (int): The time elapsed since the stopping point.
        duration (int): The time elapsed since the starting point.

    Examples:
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
    """

    _ts_start: int
    _ts_last: int
    _ts_stop: int
    _checkpoints: list[int]

    def __init__(self) -> None:
        """Creates a timer.

        Examples:
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
        """
        self.reset()

    @property
    def started_at(self) -> int:
        """Gets the timestamp of the starting point.

        Returns:
            int: The start timestamp.
        """
        return self._ts_start

    @property
    def checked_at(self) -> int:
        """Gets the timestamp of the last checkpoint.

        Returns:
            int: The last checkpoint timestamp.
        """
        return self._ts_last

    @property
    def stopped_at(self) -> int:
        """Gets the timestamp of the stopping point.

        Returns:
            int: The stop timestamp, or None if the timer is still running.
        """
        return self._ts_stop

    @property
    def stopped(self) -> bool:
        """Tells if the timer was stopped.

        Returns:
            bool: True if the timer is stopped, False otherwise.
        """
        return self._ts_stop is not None

    @property
    def till_check(self) -> int:
        """Gets the time elapsed between the starting point and the last checkpoint.

        Returns:
            int: The time elapsed between the starting point and the last checkpoint.
        """
        return self._ts_last - self._ts_start

    @property
    def since_check(self) -> int:
        """Gets the time elapsed since the last checkpoint.

        If the timer is stopped, gets the time elapsed between the last checkpoint and and the stop.

        Returns:
            int: The time elapsed since the last checkpoint.
        """
        return self.current() - self._ts_last

    @property
    def since_stop(self) -> int:
        """Gets the time elapsed since the stopping point.

        If the timer is still running, return 0.

        Returns:
            int: The time elapsed since the stopping point.
        """
        if self._ts_stop is None:
            return 0
        return self.timestamp() - self._ts_stop

    @property
    def duration(self) -> int:
        """Gets the time elapsed since the starting point.

        If the timer is stopped, gets the total time elapsed between the start and stop points.

        Returns:
            int: The time elapsed since the starting point.
        """
        return self.current() - self._ts_start

    @property
    def mean_duration(self) -> int:
        """Gets the average duration of all checkpoints.

        The time elapsed between the stop point and the last checkpoint also counts.

        Returns:
            int: The average duration of all checkpoints.
        """
        return sum(self._checkpoints) // len(self._checkpoints)

    @property
    def checkpoints(self) -> tuple[int]:
        """Gets the duration for each checkpoint.

        The time elapsed between the stop point and the last checkpoint also counts.

        Returns:
            tuple[int]: A tuple containing the time elapsed for each checkpoint.
        """
        return tuple(self._checkpoints)

    def check(self) -> int:
        """Capture a new checkpoint.

        Returns:
            int: The time elapsed since the last checkpoint.

        Examples:
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
        """
        if self.stopped:
            return 0

        last = self._ts_last
        self._ts_last = self.timestamp()
        elapsed = self._ts_last - last
        self._checkpoints.append(elapsed)
        return elapsed

    def stop(self) -> int:
        """Stops the timer.

        Returns:
            int: The time elapsed since the starting point.

        Examples:
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
        """
        if self.stopped:
            return 0

        self._ts_stop = self.timestamp()
        self._checkpoints.append(self._ts_stop - self._ts_last)
        return self._ts_stop - self._ts_start

    def reset(self) -> None:
        """Resets the timer.

        Examples:
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
        """
        self._ts_start = self.timestamp()
        self._ts_last = self._ts_start
        self._ts_stop = None
        self._checkpoints = []

    def timestamp(self) -> int:
        """Gets the current timestamp.

        Returns:
            int: The current timestamp.

        Examples:
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
        """
        return time.monotonic_ns()

    def current(self) -> int:
        """Gets the current timestamp or the stop timestamp depending if the timer is still running.

        Returns:
            int: The current timestamp if the timer is still running, otherwise the stop timestamp.

        Examples:
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
        """
        return self.timestamp() if self._ts_stop is None else self._ts_stop

    @staticmethod
    def split_duration(duration: int) -> tuple:
        """Splits a duration in nanoseconds to a tuple containing time units.

        Args:
            duration (int): A duration expressed in nanoseconds.

        Returns:
            tuple: A tuple containing time units of this form:
            (hours, minutes, seconds, microseconds, nanoseconds)

        Examples:
        ```python
        from cerbernetix.toolbox.time import Timer

        print(Timer.split_duration(123456789)) # (0, 2, 3, 456, 789)
        ```
        """
        ns, duration = duration % 1000, duration // 1000
        ms, duration = duration % 1000, duration // 1000
        s, duration = duration % 60, duration // 60
        m, h = duration % 60, duration // 60
        return (h, m, s, ms, ns)

    PRECISION_NANOSECONDS = 5
    PRECISION_MICROSECONDS = 4
    PRECISION_SECONDS = 3
    PRECISION_MINUTES = 2
    PRECISION_HOURS = 1

    @classmethod
    def duration_to_string(cls, duration: int, precision: int = PRECISION_SECONDS) -> str:
        """Converts a duration in nanoseconds to a string presenting a split by time units.

        Args:
            duration (int): A duration expressed in nanoseconds.
            precision (int, optional): The desired time precision. This is the unit of time up to
            what express the duration. Defaults to PRECISION_SECONDS.

        Returns:
            str: A string representing the duration as hours, minutes, and seconds.

        Examples:
        ```python
        from cerbernetix.toolbox.time import Timer

        print(Timer.duration_to_string(123456789)) # "0:02:03"
        print(Timer.duration_to_string(123456789, Timer.PRECISION_NANOSECONDS)) # "0:02:03:456:789"
        ```
        """
        units = cls.split_duration(duration)
        precision = limit(precision, 1, len(units))
        return ":".join(
            [str(unit).rjust((i + 1) // 2 + 1, "0") for i, unit in enumerate(units[:precision])]
        )
