"""Test the tool for capturing the time spent."""

import unittest
from unittest.mock import patch

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
