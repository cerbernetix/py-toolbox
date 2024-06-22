"""Captures the time spent.

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
        This is the unit of time up to what express the duration.

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

    def __init__(self, precision: int = Duration.PRECISION_SECONDS) -> None:
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
        self.precision = precision
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
        return Duration(self._ts_last - self._ts_start, self.precision)

    @property
    def since_check(self) -> Duration:
        """Gets the time elapsed since the last checkpoint.

        If the timer is stopped, gets the time elapsed between the last checkpoint and and the stop.

        Returns:
            Duration: The time elapsed since the last checkpoint.
        """
        return Duration(self.current() - self._ts_last, self.precision)

    @property
    def since_stop(self) -> Duration:
        """Gets the time elapsed since the stopping point.

        If the timer is still running, return 0.

        Returns:
            Duration: The time elapsed since the stopping point.
        """
        if self._ts_stop is None:
            return Duration(0, self.precision)
        return Duration(self.timestamp() - self._ts_stop, self.precision)

    @property
    def duration(self) -> Duration:
        """Gets the time elapsed since the starting point.

        If the timer is stopped, gets the total time elapsed between the start and stop points.

        Returns:
            Duration: The time elapsed since the starting point.
        """
        return Duration(self.current() - self._ts_start, self.precision)

    @property
    def mean_duration(self) -> Duration:
        """Gets the average duration of all checkpoints.

        The time elapsed between the stop point and the last checkpoint also counts.

        Returns:
            Duration: The average duration of all checkpoints.
        """
        return Duration(sum(self._checkpoints) // len(self._checkpoints), self.precision)

    @property
    def checkpoints(self) -> tuple[Duration]:
        """Gets the duration for each checkpoint.

        The time elapsed between the stop point and the last checkpoint also counts.

        Returns:
            tuple[Duration]: A tuple containing the time elapsed for each checkpoint.
        """
        return tuple([Duration(duration, self.precision) for duration in self._checkpoints])

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

        print(timer.check())   # 0:0:2
        sleep(3)

        print(timer.stop())    # 0:0:5
        sleep(1)

        print(timer.duration)  # 0:0:5
        ```
        """
        if self.stopped:
            return Duration(0, self.precision)

        last = self._ts_last
        self._ts_last = self.timestamp()
        elapsed = self._ts_last - last
        self._checkpoints.append(elapsed)
        return Duration(elapsed, self.precision)

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

        print(timer.check())   # 0:0:2
        sleep(3)

        print(timer.stop())    # 0:0:5
        sleep(1)

        print(timer.duration)  # 0:0:5
        ```
        """
        if self.stopped:
            return Duration(0, self.precision)

        self._ts_stop = self.timestamp()
        self._checkpoints.append(self._ts_stop - self._ts_last)
        return Duration(self._ts_stop - self._ts_start, self.precision)

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
