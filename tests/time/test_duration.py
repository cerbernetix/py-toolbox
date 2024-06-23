"""Test the duration representation."""

import unittest

from cerbernetix.toolbox.testing import test_cases
from cerbernetix.toolbox.time import Duration


class TestDuration(unittest.TestCase):
    """Test suite for the duration representation."""

    def test_construction(self):
        """Tests the construction of a Duration."""
        duration = Duration(123)
        self.assertEqual(duration.duration, 123)
        self.assertEqual(duration.precision, Duration.SECONDS)
        self.assertEqual(duration.upto, Duration.HOURS)
        self.assertEqual(duration.style, Duration.COUNTER)

        duration = Duration(
            duration="456",
            precision=str(Duration.NANOSECONDS),
            upto=Duration.WEEKS,
            style=Duration.FULL,
        )
        self.assertEqual(duration.duration, 456)
        self.assertEqual(duration.precision, Duration.NANOSECONDS)
        self.assertEqual(duration.upto, Duration.WEEKS)
        self.assertEqual(duration.style, Duration.FULL)

    CASES_SPLIT = [
        [0, None, [0, 0, 0, 0, 0, 0]],
        [2191325008063004, None, [4, 63, 8, 5, 42, 608]],
        [2191325008063004, Duration.WEEKS, [4, 63, 8, 5, 42, 8, 4, 3]],
        [2191325008063004, Duration.DAYS, [4, 63, 8, 5, 42, 8, 25]],
        [2191325008063004, Duration.HOURS, [4, 63, 8, 5, 42, 608]],
        [2191325008063004, Duration.MINUTES, [4, 63, 8, 5, 36522]],
        [2191325008063004, Duration.SECONDS, [4, 63, 8, 2191325]],
        [2191325008063004, Duration.MILLISECONDS, [4, 63, 2191325008]],
        [2191325008063004, Duration.MICROSECONDS, [4, 2191325008063]],
        [2191325008063004, Duration.NANOSECONDS, [2191325008063004]],
    ]

    @test_cases(CASES_SPLIT)
    def test_split(self, duration, upto, split):
        """Tests a duration can be splitted."""
        duration = Duration(duration)
        self.assertEqual(duration.split(upto), split)

    CASES_STRING = [
        [0, None, None, None, "00:00:00"],
        [0, None, Duration.NANOSECONDS, None, "00:00:00.000000000"],
        [0, Duration.WEEKS, Duration.HOURS, Duration.COUNTER, "0:0:00"],
        [0, Duration.WEEKS, Duration.MINUTES, Duration.COUNTER, "0:0:00:00"],
        [0, Duration.WEEKS, Duration.SECONDS, Duration.COUNTER, "0:0:00:00:00"],
        [0, Duration.DAYS, Duration.HOURS, Duration.COUNTER, "0:00"],
        [0, Duration.DAYS, Duration.MINUTES, Duration.COUNTER, "0:00:00"],
        [0, Duration.DAYS, Duration.SECONDS, Duration.COUNTER, "0:00:00:00"],
        [0, Duration.HOURS, Duration.MINUTES, Duration.COUNTER, "00:00"],
        [0, Duration.HOURS, Duration.SECONDS, Duration.COUNTER, "00:00:00"],
        [0, Duration.HOURS, Duration.MILLISECONDS, Duration.COUNTER, "00:00:00.000"],
        [0, Duration.HOURS, Duration.MICROSECONDS, Duration.COUNTER, "00:00:00.000000"],
        [0, Duration.HOURS, Duration.NANOSECONDS, Duration.COUNTER, "00:00:00.000000000"],
        [2191325008063004, None, None, None, "608:42:05"],
        [2191325008063004, Duration.DAYS, Duration.HOURS, Duration.COUNTER, "25:08"],
        [2191325008063004, Duration.DAYS, Duration.MINUTES, Duration.COUNTER, "25:08:42"],
        [2191325008063004, Duration.DAYS, Duration.SECONDS, Duration.COUNTER, "25:08:42:05"],
        [2191325008063004, Duration.DAYS, Duration.MILLISECONDS, None, "25:08:42:05.008"],
        [2191325008063004, Duration.DAYS, Duration.MICROSECONDS, None, "25:08:42:05.008063"],
        [2191325008063004, Duration.DAYS, Duration.NANOSECONDS, None, "25:08:42:05.008063004"],
        [123123023003023, Duration.HOURS, Duration.HOURS, Duration.COUNTER, "34"],
        [123123023003023, Duration.HOURS, Duration.MINUTES, Duration.COUNTER, "34:12"],
        [123123023003023, Duration.HOURS, Duration.SECONDS, Duration.COUNTER, "34:12:03"],
        [123123023003023, Duration.HOURS, Duration.MILLISECONDS, Duration.COUNTER, "34:12:03.023"],
        [123123023003023, Duration.HOURS, Duration.MICROSECONDS, None, "34:12:03.023003"],
        [123123023003023, Duration.HOURS, Duration.NANOSECONDS, None, "34:12:03.023003023"],
        [0, None, None, Duration.FULL, "0s"],
        [0, None, Duration.NANOSECONDS, Duration.FULL, "0ns"],
        [0, Duration.DAYS, Duration.HOURS, Duration.FULL, "0h"],
        [0, Duration.HOURS, Duration.MINUTES, Duration.FULL, "0m"],
        [0, Duration.HOURS, Duration.SECONDS, Duration.FULL, "0s"],
        [0, Duration.HOURS, Duration.MILLISECONDS, Duration.FULL, "0ms"],
        [0, Duration.HOURS, Duration.MICROSECONDS, Duration.FULL, "0us"],
        [0, Duration.HOURS, Duration.NANOSECONDS, Duration.FULL, "0ns"],
        [2191325008063004, Duration.HOURS, None, Duration.FULL, "608h 42m 5s"],
        [2191325008063004, None, None, Duration.FULL, "3w 4d 8h 42m 5s"],
        [2525008063004, None, None, Duration.FULL, "42m 5s"],
        [
            2191325008063004,
            Duration.WEEKS,
            Duration.NANOSECONDS,
            Duration.FULL,
            "3w 4d 8h 42m 5s 8ms 63us 4ns",
        ],
        [2191325008063004, Duration.DAYS, Duration.HOURS, Duration.FULL, "25d 8h"],
        [2191325008063004, Duration.DAYS, Duration.MINUTES, Duration.FULL, "25d 8h 42m"],
        [2191325008063004, Duration.DAYS, Duration.SECONDS, Duration.FULL, "25d 8h 42m 5s"],
        [
            2191325008063004,
            Duration.DAYS,
            Duration.MILLISECONDS,
            Duration.FULL,
            "25d 8h 42m 5s 8ms",
        ],
        [
            2191325008063004,
            Duration.DAYS,
            Duration.MICROSECONDS,
            Duration.FULL,
            "25d 8h 42m 5s 8ms 63us",
        ],
        [
            2191325008063004,
            Duration.DAYS,
            Duration.NANOSECONDS,
            Duration.FULL,
            "25d 8h 42m 5s 8ms 63us 4ns",
        ],
        [123123023003023, Duration.HOURS, Duration.HOURS, Duration.FULL, "34h"],
        [123123023003023, Duration.HOURS, Duration.MINUTES, Duration.FULL, "34h 12m"],
        [123123023003023, Duration.HOURS, Duration.SECONDS, Duration.FULL, "34h 12m 3s"],
        [123123023003023, Duration.HOURS, Duration.MILLISECONDS, Duration.FULL, "34h 12m 3s 23ms"],
        [
            123123023003023,
            Duration.HOURS,
            Duration.MICROSECONDS,
            Duration.FULL,
            "34h 12m 3s 23ms 3us",
        ],
        [
            123123023003023,
            Duration.HOURS,
            Duration.NANOSECONDS,
            Duration.FULL,
            "34h 12m 3s 23ms 3us 23ns",
        ],
    ]

    @test_cases(CASES_STRING)
    def test_to_string(self, duration, upto, precision, style, result):
        """Tests a duration can be converted to string."""
        duration = Duration(duration, style=style)
        self.assertEqual(duration.to_string(precision=precision, upto=upto, style=style), result)

    def test_clone(self):
        """Test a duraction can be cloned."""
        duration1 = Duration(2191325008063004)

        duration2 = duration1.clone()
        self.assertEqual(duration2.duration, duration1.duration)
        self.assertEqual(duration2.precision, duration1.precision)
        self.assertEqual(duration2.upto, duration1.upto)
        self.assertEqual(duration2.style, duration1.style)

        duration3 = duration1.clone(
            precision=Duration.NANOSECONDS, upto=Duration.DAYS, style=Duration.FULL
        )
        self.assertEqual(duration3.duration, duration1.duration)
        self.assertEqual(duration3.precision, Duration.NANOSECONDS)
        self.assertEqual(duration3.upto, Duration.DAYS)
        self.assertEqual(duration3.style, Duration.FULL)

    @test_cases(CASES_STRING)
    def test_str(self, duration, upto, precision, style, result):
        """Tests a duration can be converted to string."""
        kwargs = {}
        if precision is not None:
            kwargs["precision"] = precision
        if upto is not None:
            kwargs["upto"] = upto
        if style is not None:
            kwargs["style"] = style
        duration = Duration(duration, **kwargs)
        self.assertEqual(str(duration), result)

    def test_repr(self):
        """Tests a duration can be converted to string."""
        self.assertEqual(
            repr(Duration(1234)),
            "Duration(1234, precision=3, upto=5, style='counter')",
        )
        self.assertEqual(
            repr(Duration(1234, 4, 7, "full")),
            "Duration(1234, precision=4, upto=7, style='full')",
        )

    def test_numeric(self):
        """Tests a duration can be converted to number."""
        duration = Duration(123456789)
        self.assertEqual(int(duration), 123456789)
        self.assertEqual(float(duration), 123456789.0)

    def test_addition(self):
        """Tests a duration can be added."""
        duration1 = Duration(10)
        duration2 = Duration(20)

        duration3 = duration1 + duration2

        self.assertEqual(duration1.duration, 10)
        self.assertEqual(duration2.duration, 20)
        self.assertEqual(duration3.duration, 30)

        duration3 = duration1 + 3
        self.assertEqual(duration1.duration, 10)
        self.assertEqual(duration3.duration, 13)

        duration3 = 2 + duration1
        self.assertEqual(duration1.duration, 10)
        self.assertEqual(duration3.duration, 12)

        duration1 += 5
        self.assertEqual(duration1.duration, 15)

    def test_subtraction(self):
        """Tests a duration can be subtracted."""
        duration1 = Duration(30)
        duration2 = Duration(20)

        duration3 = duration1 - duration2

        self.assertEqual(duration1.duration, 30)
        self.assertEqual(duration2.duration, 20)
        self.assertEqual(duration3.duration, 10)

        duration3 = duration1 - 3
        self.assertEqual(duration1.duration, 30)
        self.assertEqual(duration3.duration, 27)

        duration3 = 50 - duration1
        self.assertEqual(duration1.duration, 30)
        self.assertEqual(duration3.duration, 20)

        duration1 -= 5
        self.assertEqual(duration1.duration, 25)

    def test_comparisons(self):
        """Tests a duration can be compared."""
        duration1 = Duration(10)
        duration2 = Duration(20)
        duration3 = Duration(20)

        self.assertNotEqual(duration1, duration2)
        self.assertNotEqual(duration1, 20)
        self.assertNotEqual(duration1, "20")

        self.assertEqual(duration2, duration3)
        self.assertEqual(duration2, 20)
        self.assertEqual(duration2, "20")

        self.assertLess(duration1, duration2)
        self.assertLess(duration1, 20)
        self.assertLess(duration1, "20")

        self.assertLessEqual(duration2, duration3)
        self.assertLessEqual(duration2, 20)
        self.assertLessEqual(duration2, "20")

        self.assertGreater(duration2, duration1)
        self.assertGreater(duration2, 10)
        self.assertGreater(duration2, "10")

        self.assertGreaterEqual(duration3, duration2)
        self.assertGreaterEqual(duration3, 20)
        self.assertGreaterEqual(duration3, "20")
