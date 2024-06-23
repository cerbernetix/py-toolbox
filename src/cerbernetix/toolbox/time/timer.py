"""Captures the time spent.

Examples:
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
"""

from __future__ import annotations

import time

from cerbernetix.toolbox.time.duration import Duration


class Timer:
    """Capture the time spent.

    Attributes:
        started_at (int): The start timestamp.
        checked_at (int): The timestamp of the last checkpoint.
        stopped_at (int): The stop timestamp, or None if the timer is still running.
        stopped (bool): True if the timer is stopped, False otherwise.
        till_check (Duration): The time elapsed between the starting point and the last checkpoint.
        since_check (Duration): The time elapsed since the last checkpoint.
        since_stop (Duration): The time elapsed since the stopping point.
        duration (Duration): The time elapsed since the starting point.
        mean_duration (Duration): The average duration of all checkpoints.
        checkpoints (tuple[Duration]): The duration for each checkpoint.
        precision (int): The desired time precision when converting durations to string.
        upto (int): The larger unit to present when converting durations to string.
        style (sr): The string format to apply to the duration.

    Examples:
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
    """

    def __init__(
        self,
        precision: int = None,
        upto: int = None,
        style: str = None,
    ) -> None:
        """Creates a timer.

        Args:
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
        """
        self.precision = precision
        self.upto = upto
        self.style = style
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
    def till_check(self) -> Duration:
        """Gets the time elapsed between the starting point and the last checkpoint.

        Returns:
            Duration: The time elapsed between the starting point and the last checkpoint.
        """
        return self._to_duration(self._ts_last - self._ts_start)

    @property
    def since_check(self) -> Duration:
        """Gets the time elapsed since the last checkpoint.

        If the timer is stopped, gets the time elapsed between the last checkpoint and and the stop.

        Returns:
            Duration: The time elapsed since the last checkpoint.
        """
        return self._to_duration(self.current() - self._ts_last)

    @property
    def since_stop(self) -> Duration:
        """Gets the time elapsed since the stopping point.

        If the timer is still running, return 0.

        Returns:
            Duration: The time elapsed since the stopping point.
        """
        if self._ts_stop is None:
            return self._to_duration(0)
        return self._to_duration(self.timestamp() - self._ts_stop)

    @property
    def duration(self) -> Duration:
        """Gets the time elapsed since the starting point.

        If the timer is stopped, gets the total time elapsed between the start and stop points.

        Returns:
            Duration: The time elapsed since the starting point.
        """
        return self._to_duration(self.current() - self._ts_start)

    @property
    def mean_duration(self) -> Duration:
        """Gets the average duration of all checkpoints.

        The time elapsed between the stop point and the last checkpoint also counts.

        Returns:
            Duration: The average duration of all checkpoints.
        """
        return self._to_duration(sum(self._checkpoints) // len(self._checkpoints))

    @property
    def checkpoints(self) -> tuple[Duration]:
        """Gets the duration for each checkpoint.

        The time elapsed between the stop point and the last checkpoint also counts.

        Returns:
            tuple[Duration]: A tuple containing the time elapsed for each checkpoint.
        """
        return tuple([self._to_duration(duration) for duration in self._checkpoints])

    def check(self) -> Duration:
        """Capture a new checkpoint.

        Returns:
            Duration: The time elapsed since the last checkpoint.

        Examples:
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
        """
        if self.stopped:
            return self._to_duration(0)

        last = self._ts_last
        self._ts_last = self.timestamp()
        elapsed = self._ts_last - last
        self._checkpoints.append(elapsed)
        return self._to_duration(elapsed)

    def stop(self) -> Duration:
        """Stops the timer.

        Returns:
            Duration: The time elapsed since the starting point.

        Examples:
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
        """
        if self.stopped:
            return self._to_duration(0)

        self._ts_stop = self.timestamp()
        self._checkpoints.append(self._ts_stop - self._ts_last)
        return self._to_duration(self._ts_stop - self._ts_start)

    def reset(self) -> None:
        """Resets the timer.

        Examples:
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

    def _to_duration(self, duration: int) -> Duration:
        """Create a duration from the given value.

        Args:
            duration (int): The nanoseconds duration

        Returns:
            Duration: An instance of Duration with appropriate configuration.
        """
        return Duration(duration, precision=self.precision, upto=self.upto, style=self.style)

    _ts_start: int
    _ts_last: int
    _ts_stop: int
    _checkpoints: list[int]
