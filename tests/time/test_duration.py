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
        self.assertEqual(duration.precision, Duration.PRECISION_SECONDS)

        duration = Duration("456", str(Duration.PRECISION_NANOSECONDS))
        self.assertEqual(duration.duration, 456)
        self.assertEqual(duration.precision, Duration.PRECISION_NANOSECONDS)

    @test_cases(
        [
            [0, (0, 0, 0, 0, 0)],
            [123456789, (0, 2, 3, 456, 789)],
            [123123123123, (34, 12, 3, 123, 123)],
        ]
    )
    def test_split(self, duration, split):
        """Tests a duration can be splitted."""
        self.assertEqual(Duration(duration).split(), split)

    @test_cases(
        [
            [0, Duration.PRECISION_HOURS, "0"],
            [0, Duration.PRECISION_MINUTES, "0:00"],
            [0, Duration.PRECISION_SECONDS, "0:00:00"],
            [0, Duration.PRECISION_MICROSECONDS, "0:00:00:000"],
            [0, Duration.PRECISION_NANOSECONDS, "0:00:00:000:000"],
            [123456789, Duration.PRECISION_HOURS, "0"],
            [123456789, Duration.PRECISION_MINUTES, "0:02"],
            [123456789, Duration.PRECISION_SECONDS, "0:02:03"],
            [123456789, Duration.PRECISION_MICROSECONDS, "0:02:03:456"],
            [123456789, Duration.PRECISION_NANOSECONDS, "0:02:03:456:789"],
            [123123003023, Duration.PRECISION_HOURS, "34"],
            [123123003023, Duration.PRECISION_MINUTES, "34:12"],
            [123123003023, Duration.PRECISION_SECONDS, "34:12:03"],
            [123123003023, Duration.PRECISION_MICROSECONDS, "34:12:03:003"],
            [123123003023, Duration.PRECISION_NANOSECONDS, "34:12:03:003:023"],
        ]
    )
    def test_to_string(self, duration, precision, result):
        """Tests a duration can be converted to string."""
        self.assertEqual(Duration(duration).to_string(precision), result)

    @test_cases(
        [
            [0, Duration.PRECISION_HOURS, "0"],
            [0, Duration.PRECISION_MINUTES, "0:00"],
            [0, Duration.PRECISION_SECONDS, "0:00:00"],
            [0, Duration.PRECISION_MICROSECONDS, "0:00:00:000"],
            [0, Duration.PRECISION_NANOSECONDS, "0:00:00:000:000"],
            [123456789, Duration.PRECISION_HOURS, "0"],
            [123456789, Duration.PRECISION_MINUTES, "0:02"],
            [123456789, Duration.PRECISION_SECONDS, "0:02:03"],
            [123456789, Duration.PRECISION_MICROSECONDS, "0:02:03:456"],
            [123456789, Duration.PRECISION_NANOSECONDS, "0:02:03:456:789"],
            [123123003023, Duration.PRECISION_HOURS, "34"],
            [123123003023, Duration.PRECISION_MINUTES, "34:12"],
            [123123003023, Duration.PRECISION_SECONDS, "34:12:03"],
            [123123003023, Duration.PRECISION_MICROSECONDS, "34:12:03:003"],
            [123123003023, Duration.PRECISION_NANOSECONDS, "34:12:03:003:023"],
        ]
    )
    def test_str(self, duration, precision, result):
        """Tests a duration can be converted to string."""
        self.assertEqual(str(Duration(duration, precision)), result)

    def test_repr(self):
        """Tests a duration can be converted to string."""
        duration = Duration(1234, 4)
        self.assertEqual(duration.__repr__(), "Duration(1234, 4)")

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
