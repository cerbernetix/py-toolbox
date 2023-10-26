"""Test the tool for getting the date of a weekday."""
import unittest
from datetime import date
from unittest.mock import patch

from cerbernetix.toolbox.testing import test_cases
from cerbernetix.toolbox.time import (
    FRIDAY,
    MONDAY,
    SATURDAY,
    SUNDAY,
    THURSDAY,
    TUESDAY,
    WEDNESDAY,
    Weekday,
)


class TestWeekday(unittest.TestCase):
    """Test suite for the tool for getting the date of a weekday."""

    def test_construction(self):
        """Tests the construction of a Weekday."""
        weekday = Weekday(FRIDAY)
        self.assertEqual(weekday.day, FRIDAY)

    @test_cases(
        [
            # Monday
            ["Monday from Monday", MONDAY, MONDAY, 7],
            ["Monday from Tuesday", MONDAY, TUESDAY, 6],
            ["Monday from Wednesday", MONDAY, WEDNESDAY, 5],
            ["Monday from Thursday", MONDAY, THURSDAY, 4],
            ["Monday from Friday", MONDAY, FRIDAY, 3],
            ["Monday from Saturday", MONDAY, SATURDAY, 2],
            ["Monday from Sunday", MONDAY, SUNDAY, 1],
            # Tuesday
            ["Tuesday from Monday", TUESDAY, MONDAY, 1],
            ["Tuesday from Tuesday", TUESDAY, TUESDAY, 7],
            ["Tuesday from Wednesday", TUESDAY, WEDNESDAY, 6],
            ["Tuesday from Thursday", TUESDAY, THURSDAY, 5],
            ["Tuesday from Friday", TUESDAY, FRIDAY, 4],
            ["Tuesday from Saturday", TUESDAY, SATURDAY, 3],
            ["Tuesday from Sunday", TUESDAY, SUNDAY, 2],
            # Wednesday
            ["Wednesday from Monday", WEDNESDAY, MONDAY, 2],
            ["Wednesday from Tuesday", WEDNESDAY, TUESDAY, 1],
            ["Wednesday from Wednesday", WEDNESDAY, WEDNESDAY, 7],
            ["Wednesday from Thursday", WEDNESDAY, THURSDAY, 6],
            ["Wednesday from Friday", WEDNESDAY, FRIDAY, 5],
            ["Wednesday from Saturday", WEDNESDAY, SATURDAY, 4],
            ["Wednesday from Sunday", WEDNESDAY, SUNDAY, 3],
            # Thursday
            ["Thursday from Monday", THURSDAY, MONDAY, 3],
            ["Thursday from Tuesday", THURSDAY, TUESDAY, 2],
            ["Thursday from Wednesday", THURSDAY, WEDNESDAY, 1],
            ["Thursday from Thursday", THURSDAY, THURSDAY, 7],
            ["Thursday from Friday", THURSDAY, FRIDAY, 6],
            ["Thursday from Saturday", THURSDAY, SATURDAY, 5],
            ["Thursday from Sunday", THURSDAY, SUNDAY, 4],
            # Friday
            ["Friday from Monday", FRIDAY, MONDAY, 4],
            ["Friday from Tuesday", FRIDAY, TUESDAY, 3],
            ["Friday from Wednesday", FRIDAY, WEDNESDAY, 2],
            ["Friday from Thursday", FRIDAY, THURSDAY, 1],
            ["Friday from Friday", FRIDAY, FRIDAY, 7],
            ["Friday from Saturday", FRIDAY, SATURDAY, 6],
            ["Friday from Sunday", FRIDAY, SUNDAY, 5],
            # Saturday
            ["Saturday from Monday", SATURDAY, MONDAY, 5],
            ["Saturday from Tuesday", SATURDAY, TUESDAY, 4],
            ["Saturday from Wednesday", SATURDAY, WEDNESDAY, 3],
            ["Saturday from Thursday", SATURDAY, THURSDAY, 2],
            ["Saturday from Friday", SATURDAY, FRIDAY, 1],
            ["Saturday from Saturday", SATURDAY, SATURDAY, 7],
            ["Saturday from Sunday", SATURDAY, SUNDAY, 6],
            # Sunday
            ["Sunday from Monday", SUNDAY, MONDAY, 6],
            ["Sunday from Tuesday", SUNDAY, TUESDAY, 5],
            ["Sunday from Wednesday", SUNDAY, WEDNESDAY, 4],
            ["Sunday from Thursday", SUNDAY, THURSDAY, 3],
            ["Sunday from Friday", SUNDAY, FRIDAY, 2],
            ["Sunday from Saturday", SUNDAY, SATURDAY, 1],
            ["Sunday from Sunday", SUNDAY, SUNDAY, 7],
        ]
    )
    def test_next(self, _, day, current, number):
        """Test the number of days to the next occurrence is returned."""
        weekday = Weekday(day)
        self.assertEqual(weekday.next(current), number)

        with patch("datetime.date") as mock:
            mock.today.return_value.weekday.return_value = current
            self.assertEqual(weekday.next(), number)

    @test_cases(
        [
            # Monday
            ["Monday from Monday", MONDAY, MONDAY, 7],
            ["Monday from Tuesday", MONDAY, TUESDAY, 1],
            ["Monday from Wednesday", MONDAY, WEDNESDAY, 2],
            ["Monday from Thursday", MONDAY, THURSDAY, 3],
            ["Monday from Friday", MONDAY, FRIDAY, 4],
            ["Monday from Saturday", MONDAY, SATURDAY, 5],
            ["Monday from Sunday", MONDAY, SUNDAY, 6],
            # Tuesday
            ["Tuesday from Monday", TUESDAY, MONDAY, 6],
            ["Tuesday from Tuesday", TUESDAY, TUESDAY, 7],
            ["Tuesday from Wednesday", TUESDAY, WEDNESDAY, 1],
            ["Tuesday from Thursday", TUESDAY, THURSDAY, 2],
            ["Tuesday from Friday", TUESDAY, FRIDAY, 3],
            ["Tuesday from Saturday", TUESDAY, SATURDAY, 4],
            ["Tuesday from Sunday", TUESDAY, SUNDAY, 5],
            # Wednesday
            ["Wednesday from Monday", WEDNESDAY, MONDAY, 5],
            ["Wednesday from Tuesday", WEDNESDAY, TUESDAY, 6],
            ["Wednesday from Wednesday", WEDNESDAY, WEDNESDAY, 7],
            ["Wednesday from Thursday", WEDNESDAY, THURSDAY, 1],
            ["Wednesday from Friday", WEDNESDAY, FRIDAY, 2],
            ["Wednesday from Saturday", WEDNESDAY, SATURDAY, 3],
            ["Wednesday from Sunday", WEDNESDAY, SUNDAY, 4],
            # Thursday
            ["Thursday from Monday", THURSDAY, MONDAY, 4],
            ["Thursday from Tuesday", THURSDAY, TUESDAY, 5],
            ["Thursday from Wednesday", THURSDAY, WEDNESDAY, 6],
            ["Thursday from Thursday", THURSDAY, THURSDAY, 7],
            ["Thursday from Friday", THURSDAY, FRIDAY, 1],
            ["Thursday from Saturday", THURSDAY, SATURDAY, 2],
            ["Thursday from Sunday", THURSDAY, SUNDAY, 3],
            # Friday
            ["Friday from Monday", FRIDAY, MONDAY, 3],
            ["Friday from Tuesday", FRIDAY, TUESDAY, 4],
            ["Friday from Wednesday", FRIDAY, WEDNESDAY, 5],
            ["Friday from Thursday", FRIDAY, THURSDAY, 6],
            ["Friday from Friday", FRIDAY, FRIDAY, 7],
            ["Friday from Saturday", FRIDAY, SATURDAY, 1],
            ["Friday from Sunday", FRIDAY, SUNDAY, 2],
            # Saturday
            ["Saturday from Monday", SATURDAY, MONDAY, 2],
            ["Saturday from Tuesday", SATURDAY, TUESDAY, 3],
            ["Saturday from Wednesday", SATURDAY, WEDNESDAY, 4],
            ["Saturday from Thursday", SATURDAY, THURSDAY, 5],
            ["Saturday from Friday", SATURDAY, FRIDAY, 6],
            ["Saturday from Saturday", SATURDAY, SATURDAY, 7],
            ["Saturday from Sunday", SATURDAY, SUNDAY, 1],
            # Sunday
            ["Sunday from Monday", SUNDAY, MONDAY, 1],
            ["Sunday from Tuesday", SUNDAY, TUESDAY, 2],
            ["Sunday from Wednesday", SUNDAY, WEDNESDAY, 3],
            ["Sunday from Thursday", SUNDAY, THURSDAY, 4],
            ["Sunday from Friday", SUNDAY, FRIDAY, 5],
            ["Sunday from Saturday", SUNDAY, SATURDAY, 6],
            ["Sunday from Sunday", SUNDAY, SUNDAY, 7],
        ]
    )
    def test_previous(self, _, day, current, number):
        """Test the number of days to the previous occurrence is returned."""
        weekday = Weekday(day)
        self.assertEqual(weekday.previous(current), number)

        with patch("datetime.date") as mock:
            mock.today.return_value.weekday.return_value = current
            self.assertEqual(weekday.previous(), number)

    @test_cases(
        [
            # Monday
            ["Monday from Monday", MONDAY, MONDAY, 0],
            ["Monday from Tuesday", MONDAY, TUESDAY, -1],
            ["Monday from Wednesday", MONDAY, WEDNESDAY, -2],
            ["Monday from Thursday", MONDAY, THURSDAY, -3],
            ["Monday from Friday", MONDAY, FRIDAY, 3],
            ["Monday from Saturday", MONDAY, SATURDAY, 2],
            ["Monday from Sunday", MONDAY, SUNDAY, 1],
            # Tuesday
            ["Tuesday from Monday", TUESDAY, MONDAY, 1],
            ["Tuesday from Tuesday", TUESDAY, TUESDAY, 0],
            ["Tuesday from Wednesday", TUESDAY, WEDNESDAY, -1],
            ["Tuesday from Thursday", TUESDAY, THURSDAY, -2],
            ["Tuesday from Friday", TUESDAY, FRIDAY, -3],
            ["Tuesday from Saturday", TUESDAY, SATURDAY, 3],
            ["Tuesday from Sunday", TUESDAY, SUNDAY, 2],
            # Wednesday
            ["Wednesday from Monday", WEDNESDAY, MONDAY, 2],
            ["Wednesday from Tuesday", WEDNESDAY, TUESDAY, 1],
            ["Wednesday from Wednesday", WEDNESDAY, WEDNESDAY, 0],
            ["Wednesday from Thursday", WEDNESDAY, THURSDAY, -1],
            ["Wednesday from Friday", WEDNESDAY, FRIDAY, -2],
            ["Wednesday from Saturday", WEDNESDAY, SATURDAY, -3],
            ["Wednesday from Sunday", WEDNESDAY, SUNDAY, 3],
            # Thursday
            ["Thursday from Monday", THURSDAY, MONDAY, 3],
            ["Thursday from Tuesday", THURSDAY, TUESDAY, 2],
            ["Thursday from Wednesday", THURSDAY, WEDNESDAY, 1],
            ["Thursday from Thursday", THURSDAY, THURSDAY, 0],
            ["Thursday from Friday", THURSDAY, FRIDAY, -1],
            ["Thursday from Saturday", THURSDAY, SATURDAY, -2],
            ["Thursday from Sunday", THURSDAY, SUNDAY, -3],
            # Friday
            ["Friday from Monday", FRIDAY, MONDAY, -3],
            ["Friday from Tuesday", FRIDAY, TUESDAY, 3],
            ["Friday from Wednesday", FRIDAY, WEDNESDAY, 2],
            ["Friday from Thursday", FRIDAY, THURSDAY, 1],
            ["Friday from Friday", FRIDAY, FRIDAY, 0],
            ["Friday from Saturday", FRIDAY, SATURDAY, -1],
            ["Friday from Sunday", FRIDAY, SUNDAY, -2],
            # Saturday
            ["Saturday from Monday", SATURDAY, MONDAY, -2],
            ["Saturday from Tuesday", SATURDAY, TUESDAY, -3],
            ["Saturday from Wednesday", SATURDAY, WEDNESDAY, 3],
            ["Saturday from Thursday", SATURDAY, THURSDAY, 2],
            ["Saturday from Friday", SATURDAY, FRIDAY, 1],
            ["Saturday from Saturday", SATURDAY, SATURDAY, 0],
            ["Saturday from Sunday", SATURDAY, SUNDAY, -1],
            # Sunday
            ["Sunday from Monday", SUNDAY, MONDAY, -1],
            ["Sunday from Tuesday", SUNDAY, TUESDAY, -2],
            ["Sunday from Wednesday", SUNDAY, WEDNESDAY, -3],
            ["Sunday from Thursday", SUNDAY, THURSDAY, 3],
            ["Sunday from Friday", SUNDAY, FRIDAY, 2],
            ["Sunday from Saturday", SUNDAY, SATURDAY, 1],
            ["Sunday from Sunday", SUNDAY, SUNDAY, 0],
        ]
    )
    def test_closest(self, _, day, current, number):
        """Test the number of days to the closest occurrence is returned."""
        weekday = Weekday(day)
        self.assertEqual(weekday.closest(current), number)

        with patch("datetime.date") as mock:
            mock.today.return_value.weekday.return_value = current
            self.assertEqual(weekday.closest(), number)

    @test_cases(
        [
            # Monday to Monday
            [
                "Next Monday from Monday, using string",
                MONDAY,
                False,
                "2023-10-02",
                date.fromisoformat("2023-10-09"),
            ],
            [
                "Next Monday from Monday, using date",
                MONDAY,
                False,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-10-09"),
            ],
            [
                "Closest Monday from Monday",
                MONDAY,
                True,
                "2023-10-02",
                date.fromisoformat("2023-10-02"),
            ],
            # Wednesday to Monday
            [
                "Next Monday from Wednesday, using string",
                MONDAY,
                False,
                "2023-10-04",
                date.fromisoformat("2023-10-09"),
            ],
            [
                "Next Monday from Wednesday, using date",
                MONDAY,
                False,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-10-09"),
            ],
            [
                "Closest Monday from Wednesday",
                MONDAY,
                True,
                "2023-10-04",
                date.fromisoformat("2023-10-09"),
            ],
            # Sunday to Monday
            [
                "Next Monday from Sunday, using string",
                MONDAY,
                False,
                "2023-10-08",
                date.fromisoformat("2023-10-09"),
            ],
            [
                "Next Monday from Sunday, using date",
                MONDAY,
                False,
                date.fromisoformat("2023-10-08"),
                date.fromisoformat("2023-10-09"),
            ],
            [
                "Closest Monday from Sunday",
                MONDAY,
                True,
                "2023-10-08",
                date.fromisoformat("2023-10-09"),
            ],
            # Monday to Wednesday
            [
                "Next Wednesday from Monday, using string",
                WEDNESDAY,
                False,
                "2023-10-02",
                date.fromisoformat("2023-10-04"),
            ],
            [
                "Next Wednesday from Monday, using date",
                WEDNESDAY,
                False,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-10-04"),
            ],
            [
                "Closest Wednesday from Monday",
                WEDNESDAY,
                True,
                "2023-10-02",
                date.fromisoformat("2023-10-04"),
            ],
            # Wednesday to Wednesday
            [
                "Next Wednesday from Wednesday, using string",
                WEDNESDAY,
                False,
                "2023-10-04",
                date.fromisoformat("2023-10-11"),
            ],
            [
                "Next Wednesday from Wednesday, using date",
                WEDNESDAY,
                False,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-10-11"),
            ],
            [
                "Closest Wednesday from Wednesday",
                WEDNESDAY,
                True,
                "2023-10-04",
                date.fromisoformat("2023-10-04"),
            ],
            # Sunday to Wednesday
            [
                "Next Wednesday from Sunday, using string",
                WEDNESDAY,
                False,
                "2023-10-08",
                date.fromisoformat("2023-10-11"),
            ],
            [
                "Next Wednesday from Sunday, using date",
                WEDNESDAY,
                False,
                date.fromisoformat("2023-10-08"),
                date.fromisoformat("2023-10-11"),
            ],
            [
                "Closest Wednesday from Sunday",
                WEDNESDAY,
                True,
                "2023-10-08",
                date.fromisoformat("2023-10-11"),
            ],
            # Monday to Sunday
            [
                "Next Sunday from Monday, using string",
                SUNDAY,
                False,
                "2023-10-02",
                date.fromisoformat("2023-10-08"),
            ],
            [
                "Next Sunday from Monday, using date",
                SUNDAY,
                False,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-10-08"),
            ],
            [
                "Closest Sunday from Monday",
                SUNDAY,
                True,
                "2023-10-02",
                date.fromisoformat("2023-10-08"),
            ],
            # Wednesday to Sunday
            [
                "Next Sunday from Wednesday, using string",
                SUNDAY,
                False,
                "2023-10-04",
                date.fromisoformat("2023-10-08"),
            ],
            [
                "Next Sunday from Wednesday, using date",
                SUNDAY,
                False,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-10-08"),
            ],
            [
                "Closest Sunday from Wednesday",
                SUNDAY,
                True,
                "2023-10-04",
                date.fromisoformat("2023-10-08"),
            ],
            # Sunday to Sunday
            [
                "Next Sunday from Sunday, using string",
                SUNDAY,
                False,
                "2023-10-08",
                date.fromisoformat("2023-10-15"),
            ],
            [
                "Next Sunday from Sunday, using date",
                SUNDAY,
                False,
                date.fromisoformat("2023-10-08"),
                date.fromisoformat("2023-10-15"),
            ],
            [
                "Closest Sunday from Sunday",
                SUNDAY,
                True,
                "2023-10-08",
                date.fromisoformat("2023-10-08"),
            ],
        ],
    )
    def test_next_date(self, _, day, closest, current, result):
        """Test the date of the next occurrence is returned."""
        weekday = Weekday(day)
        self.assertEqual(weekday.next_date(current, closest), result)

        with patch("datetime.date", spec=date) as mock:
            mock.today.return_value = (
                current if isinstance(current, date) else date.fromisoformat(current)
            )
            self.assertEqual(weekday.next_date(closest=closest), result)

        self.assertRaises(ValueError, lambda: weekday.next_date(""))
        self.assertRaises(TypeError, lambda: weekday.next_date(True))

    @test_cases(
        [
            # Monday to Monday
            [
                "Previous Monday from Monday, using string",
                MONDAY,
                False,
                "2023-10-02",
                date.fromisoformat("2023-09-25"),
            ],
            [
                "Previous Monday from Monday, using date",
                MONDAY,
                False,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-09-25"),
            ],
            [
                "Closest Monday from Monday",
                MONDAY,
                True,
                "2023-10-02",
                date.fromisoformat("2023-10-02"),
            ],
            # Wednesday to Monday
            [
                "Previous Monday from Wednesday, using string",
                MONDAY,
                False,
                "2023-10-04",
                date.fromisoformat("2023-10-02"),
            ],
            [
                "Previous Monday from Wednesday, using date",
                MONDAY,
                False,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-10-02"),
            ],
            [
                "Closest Monday from Wednesday",
                MONDAY,
                True,
                "2023-10-04",
                date.fromisoformat("2023-10-02"),
            ],
            # Sunday to Monday
            [
                "Previous Monday from Sunday, using string",
                MONDAY,
                False,
                "2023-10-08",
                date.fromisoformat("2023-10-02"),
            ],
            [
                "Previous Monday from Sunday, using date",
                MONDAY,
                False,
                date.fromisoformat("2023-10-08"),
                date.fromisoformat("2023-10-02"),
            ],
            [
                "Closest Monday from Sunday",
                MONDAY,
                True,
                "2023-10-08",
                date.fromisoformat("2023-10-02"),
            ],
            # Monday to Wednesday
            [
                "Previous Wednesday from Monday, using string",
                WEDNESDAY,
                False,
                "2023-10-02",
                date.fromisoformat("2023-09-27"),
            ],
            [
                "Previous Wednesday from Monday, using date",
                WEDNESDAY,
                False,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-09-27"),
            ],
            [
                "Closest Wednesday from Monday",
                WEDNESDAY,
                True,
                "2023-10-02",
                date.fromisoformat("2023-09-27"),
            ],
            # Wednesday to Wednesday
            [
                "Previous Wednesday from Wednesday, using string",
                WEDNESDAY,
                False,
                "2023-10-04",
                date.fromisoformat("2023-09-27"),
            ],
            [
                "Previous Wednesday from Wednesday, using date",
                WEDNESDAY,
                False,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-09-27"),
            ],
            [
                "Closest Wednesday from Wednesday",
                WEDNESDAY,
                True,
                "2023-10-04",
                date.fromisoformat("2023-10-04"),
            ],
            # Sunday to Wednesday
            [
                "Previous Wednesday from Sunday, using string",
                WEDNESDAY,
                False,
                "2023-10-08",
                date.fromisoformat("2023-10-04"),
            ],
            [
                "Previous Wednesday from Sunday, using date",
                WEDNESDAY,
                False,
                date.fromisoformat("2023-10-08"),
                date.fromisoformat("2023-10-04"),
            ],
            [
                "Closest Wednesday from Sunday",
                WEDNESDAY,
                True,
                "2023-10-08",
                date.fromisoformat("2023-10-04"),
            ],
            # Monday to Sunday
            [
                "Previous Sunday from Monday, using string",
                SUNDAY,
                False,
                "2023-10-02",
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Previous Sunday from Monday, using date",
                SUNDAY,
                False,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Closest Sunday from Monday",
                SUNDAY,
                True,
                "2023-10-02",
                date.fromisoformat("2023-10-01"),
            ],
            # Wednesday to Sunday
            [
                "Previous Sunday from Wednesday, using string",
                SUNDAY,
                False,
                "2023-10-04",
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Previous Sunday from Wednesday, using date",
                SUNDAY,
                False,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Closest Sunday from Wednesday",
                SUNDAY,
                True,
                "2023-10-04",
                date.fromisoformat("2023-10-01"),
            ],
            # Sunday to Sunday
            [
                "Previous Sunday from Sunday, using string",
                SUNDAY,
                False,
                "2023-10-08",
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Previous Sunday from Sunday, using date",
                SUNDAY,
                False,
                date.fromisoformat("2023-10-08"),
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Closest Sunday from Sunday",
                SUNDAY,
                True,
                "2023-10-08",
                date.fromisoformat("2023-10-08"),
            ],
        ],
    )
    def test_previous_date(self, _, day, closest, current, result):
        """Test the date of the previous occurrence is returned."""
        weekday = Weekday(day)
        self.assertEqual(weekday.previous_date(current, closest), result)

        with patch("datetime.date", spec=date) as mock:
            mock.today.return_value = (
                current if isinstance(current, date) else date.fromisoformat(current)
            )
            self.assertEqual(weekday.previous_date(closest=closest), result)

        self.assertRaises(ValueError, lambda: weekday.previous_date(""))
        self.assertRaises(TypeError, lambda: weekday.previous_date(True))

    @test_cases(
        [
            # Monday to Monday
            [
                "Closest Monday from Monday, using string",
                MONDAY,
                "2023-10-02",
                date.fromisoformat("2023-10-02"),
            ],
            [
                "Closest Monday from Monday, using date",
                MONDAY,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-10-02"),
            ],
            # Wednesday to Monday
            [
                "Closest Monday from Wednesday, using string",
                MONDAY,
                "2023-10-04",
                date.fromisoformat("2023-10-02"),
            ],
            [
                "Closest Monday from Wednesday, using date",
                MONDAY,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-10-02"),
            ],
            # Sunday to Monday
            [
                "Closest Monday from Sunday, using string",
                MONDAY,
                "2023-10-01",
                date.fromisoformat("2023-10-02"),
            ],
            [
                "Closest Monday from Sunday, using date",
                MONDAY,
                date.fromisoformat("2023-10-01"),
                date.fromisoformat("2023-10-02"),
            ],
            # Monday to Wednesday
            [
                "Closest Wednesday from Monday, using string",
                WEDNESDAY,
                "2023-10-02",
                date.fromisoformat("2023-10-04"),
            ],
            [
                "Closest Wednesday from Monday, using date",
                WEDNESDAY,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-10-04"),
            ],
            # Wednesday to Wednesday
            [
                "Closest Wednesday from Wednesday, using string",
                WEDNESDAY,
                "2023-10-04",
                date.fromisoformat("2023-10-04"),
            ],
            [
                "Closest Wednesday from Wednesday, using date",
                WEDNESDAY,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-10-04"),
            ],
            # Sunday to Wednesday
            [
                "Closest Wednesday from Sunday, using string",
                WEDNESDAY,
                "2023-10-08",
                date.fromisoformat("2023-10-11"),
            ],
            [
                "Closest Wednesday from Sunday, using date",
                WEDNESDAY,
                date.fromisoformat("2023-10-08"),
                date.fromisoformat("2023-10-11"),
            ],
            # Monday to Sunday
            [
                "Closest Sunday from Monday, using string",
                SUNDAY,
                "2023-10-02",
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Closest Sunday from Monday, using date",
                SUNDAY,
                date.fromisoformat("2023-10-02"),
                date.fromisoformat("2023-10-01"),
            ],
            # Wednesday to Sunday
            [
                "Closest Sunday from Wednesday, using string",
                SUNDAY,
                "2023-10-04",
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Closest Sunday from Wednesday, using date",
                SUNDAY,
                date.fromisoformat("2023-10-04"),
                date.fromisoformat("2023-10-01"),
            ],
            # Sunday to Sunday
            [
                "Closest Sunday from Sunday, using string",
                SUNDAY,
                "2023-10-01",
                date.fromisoformat("2023-10-01"),
            ],
            [
                "Closest Sunday from Sunday, using date",
                SUNDAY,
                date.fromisoformat("2023-10-01"),
                date.fromisoformat("2023-10-01"),
            ],
        ],
    )
    def test_closest_date(self, _, day, current, result):
        """Test the date of the closest occurrence is returned."""
        weekday = Weekday(day)
        self.assertEqual(weekday.closest_date(current), result)

        with patch("datetime.date", spec=date) as mock:
            mock.today.return_value = (
                current if isinstance(current, date) else date.fromisoformat(current)
            )
            self.assertEqual(weekday.closest_date(), result)

        self.assertRaises(ValueError, lambda: weekday.closest_date(""))
        self.assertRaises(TypeError, lambda: weekday.closest_date(True))
