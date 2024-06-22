"""Test the tool for capturing the time spent."""

import unittest
from unittest.mock import patch

from cerbernetix.toolbox.testing import test_cases
from cerbernetix.toolbox.time import Timer


class TestTimer(unittest.TestCase):
    """Test suite for the tool for capturing the time spent."""

    @patch("time.monotonic_ns")
    def test_construction(self, monotonic_ns):
        """Tests the construction of a Timer."""
        monotonic_ns.return_value = 123456789
        timer = Timer()
        self.assertEqual(timer.started_at, 123456789)
        self.assertEqual(timer.checked_at, 123456789)
        self.assertIsNone(timer.stopped_at)
        self.assertFalse(timer.stopped)
        self.assertEqual(timer.till_check, 0)
        self.assertEqual(timer.since_check, 0)
        self.assertEqual(timer.since_stop, 0)
        self.assertEqual(timer.duration, 0)
        self.assertEqual(timer.checkpoints, ())

    @patch("time.monotonic_ns")
    def test_check(self, monotonic_ns):
        """Tests the checkpoints for a Timer."""
        monotonic_ns.return_value = 0
        timer = Timer()
        self.assertEqual(timer.started_at, 0)
        self.assertEqual(timer.checked_at, 0)
        self.assertIsNone(timer.stopped_at)
        self.assertFalse(timer.stopped)

        monotonic_ns.return_value = 100
        self.assertEqual(timer.check(), 100)
        self.assertEqual(timer.started_at, 0)
        self.assertEqual(timer.checked_at, 100)
        self.assertIsNone(timer.stopped_at)
        self.assertFalse(timer.stopped)
        self.assertEqual(timer.till_check, 100)
        self.assertEqual(timer.since_check, 0)
        self.assertEqual(timer.since_stop, 0)
        self.assertEqual(timer.duration, 100)
        self.assertEqual(timer.checkpoints, (100,))

    @patch("time.monotonic_ns")
    def test_stop(self, monotonic_ns):
        """Tests a Timer can be stopped."""
        monotonic_ns.return_value = 0
        timer = Timer()
        self.assertEqual(timer.started_at, 0)
        self.assertEqual(timer.checked_at, 0)
        self.assertIsNone(timer.stopped_at)
        self.assertFalse(timer.stopped)

        monotonic_ns.return_value = 100
        self.assertEqual(timer.check(), 100)

        monotonic_ns.return_value = 200
        self.assertEqual(timer.stop(), 200)
        self.assertEqual(timer.started_at, 0)
        self.assertEqual(timer.checked_at, 100)
        self.assertEqual(timer.stopped_at, 200)
        self.assertTrue(timer.stopped)
        self.assertEqual(timer.till_check, 100)
        self.assertEqual(timer.since_check, 100)
        self.assertEqual(timer.since_stop, 0)
        self.assertEqual(timer.duration, 200)
        self.assertEqual(timer.checkpoints, (100, 100))

        monotonic_ns.return_value = 300
        self.assertEqual(timer.stop(), 0)
        self.assertEqual(timer.since_stop, 100)
        self.assertEqual(timer.duration, 200)

        self.assertEqual(timer.check(), 0)
        self.assertEqual(timer.started_at, 0)
        self.assertEqual(timer.checked_at, 100)
        self.assertEqual(timer.stopped_at, 200)
        self.assertTrue(timer.stopped)
        self.assertEqual(timer.till_check, 100)
        self.assertEqual(timer.since_check, 100)
        self.assertEqual(timer.since_stop, 100)
        self.assertEqual(timer.duration, 200)
        self.assertEqual(timer.checkpoints, (100, 100))

    @patch("time.monotonic_ns")
    def test_mean_duration(self, monotonic_ns):
        """Tests the average duration of checkpoints."""
        monotonic_ns.return_value = 0
        timer = Timer()
        self.assertEqual(timer.started_at, 0)
        self.assertEqual(timer.checked_at, 0)
        self.assertIsNone(timer.stopped_at)
        self.assertFalse(timer.stopped)

        monotonic_ns.return_value = 100
        self.assertEqual(timer.check(), 100)
        self.assertEqual(timer.checkpoints, (100,))
        self.assertEqual(timer.mean_duration, 100)

        monotonic_ns.return_value = 200
        self.assertEqual(timer.check(), 100)
        self.assertEqual(timer.checkpoints, (100, 100))
        self.assertEqual(timer.mean_duration, 100)

        monotonic_ns.return_value = 250
        self.assertEqual(timer.check(), 50)
        self.assertEqual(timer.checkpoints, (100, 100, 50))
        self.assertEqual(timer.mean_duration, 83)

        monotonic_ns.return_value = 300
        self.assertEqual(timer.stop(), 300)
        self.assertEqual(timer.checkpoints, (100, 100, 50, 50))
        self.assertEqual(timer.mean_duration, 75)

    @patch("time.monotonic_ns")
    def test_reset(self, monotonic_ns):
        """Tests a Timer can be reset."""
        monotonic_ns.return_value = 0
        timer = Timer()
        self.assertEqual(timer.started_at, 0)
        self.assertEqual(timer.checked_at, 0)
        self.assertIsNone(timer.stopped_at)
        self.assertFalse(timer.stopped)

        monotonic_ns.return_value = 100
        self.assertEqual(timer.check(), 100)

        monotonic_ns.return_value = 200
        self.assertEqual(timer.stop(), 200)

        self.assertEqual(timer.started_at, 0)
        self.assertEqual(timer.checked_at, 100)
        self.assertEqual(timer.stopped_at, 200)
        self.assertTrue(timer.stopped)
        self.assertEqual(timer.till_check, 100)
        self.assertEqual(timer.since_check, 100)
        self.assertEqual(timer.since_stop, 0)
        self.assertEqual(timer.duration, 200)
        self.assertEqual(timer.checkpoints, (100, 100))

        monotonic_ns.return_value = 300
        timer.reset()
        self.assertEqual(timer.started_at, 300)
        self.assertEqual(timer.checked_at, 300)
        self.assertIsNone(timer.stopped_at)
        self.assertFalse(timer.stopped)
        self.assertEqual(timer.till_check, 0)
        self.assertEqual(timer.since_check, 0)
        self.assertEqual(timer.since_stop, 0)
        self.assertEqual(timer.duration, 0)
        self.assertEqual(timer.checkpoints, ())

    @test_cases(
        [
            [0, (0, 0, 0, 0, 0)],
            [123456789, (0, 2, 3, 456, 789)],
            [123123123123, (34, 12, 3, 123, 123)],
        ]
    )
    def test_split_duration(self, duration, split):
        """Tests a duration can be splitted."""
        self.assertEqual(Timer.split_duration(duration), split)

    @test_cases(
        [
            [0, Timer.PRECISION_HOURS, "0"],
            [0, Timer.PRECISION_MINUTES, "0:00"],
            [0, Timer.PRECISION_SECONDS, "0:00:00"],
            [0, Timer.PRECISION_MICROSECONDS, "0:00:00:000"],
            [0, Timer.PRECISION_NANOSECONDS, "0:00:00:000:000"],
            [123456789, Timer.PRECISION_HOURS, "0"],
            [123456789, Timer.PRECISION_MINUTES, "0:02"],
            [123456789, Timer.PRECISION_SECONDS, "0:02:03"],
            [123456789, Timer.PRECISION_MICROSECONDS, "0:02:03:456"],
            [123456789, Timer.PRECISION_NANOSECONDS, "0:02:03:456:789"],
            [123123003023, Timer.PRECISION_HOURS, "34"],
            [123123003023, Timer.PRECISION_MINUTES, "34:12"],
            [123123003023, Timer.PRECISION_SECONDS, "34:12:03"],
            [123123003023, Timer.PRECISION_MICROSECONDS, "34:12:03:003"],
            [123123003023, Timer.PRECISION_NANOSECONDS, "34:12:03:003:023"],
        ]
    )
    def test_duration_to_string(self, duration, precision, result):
        """Tests a duration can be splitted."""
        self.assertEqual(Timer.duration_to_string(duration, precision), result)
