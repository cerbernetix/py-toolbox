"""Test the TestCase class with more assertions."""
from toolbox.testing import TestCase, test_cases


class TestAsserts(TestCase):
    """Test suite for the TestCase class with more assertions."""

    @test_cases(
        [
            {
                "_": "floats",
                "first": 12.3456778123,
                "second": 12.3456789546,
                "places": 5,
            },
            {
                "_": "lists",
                "first": [12.3456789123, 57.0987654323335],
                "second": [12.3456789546, 57.0987654563232],
                "places": 7,
            },
            {
                "_": "n-dim lists",
                "first": [
                    [12.3456789123, 57.0987654323335],
                    [3.4546565465, 4.434325286767, 5.343543543],
                ],
                "second": [
                    [12.3456789546, 57.0987654563232],
                    [3.4546565324, 4.434325276767, 5.343543522],
                ],
                "places": 7,
            },
            {
                "_": "tuples",
                "first": (12.3456779123, 57.0987644323335),
                "second": (12.3456789546, 57.0987654563232),
                "places": 5,
            },
            {
                "_": "sets",
                "first": {12.3456789123, 57.0987654323335},
                "second": {12.3456789546, 57.0987654563232},
                "places": 7,
            },
            {
                "_": "dicts",
                "first": {"a": 12.3456789123, "b": [57.0987654323335, 2.24343545354]},
                "second": {"a": 12.3456789546, "b": [57.0987654563232, 2.24343545764]},
                "places": 7,
            },
            {
                "_": "mix list and dict",
                "first": [12.3456789123, 57.0987654323335],
                "second": {"a": 12.3456789546, "b": 57.0987654563232},
                "places": 7,
            },
        ]
    )
    def test_lists_almost_equal(self, _, first, second, places):
        """Tests 2 lists of floats are almost equal"""
        self.assertListsAlmostEqual(first, second, places)

    @test_cases(
        [
            {
                "_": "first list is longer",
                "first": [12.3456789123, 57.0987654323335, 23.454662],
                "second": [12.3456789546, 57.0987654563232],
                "places": 7,
            },
            {
                "_": "second list is longer",
                "first": [12.3456789123, 57.0987654323335],
                "second": [12.3456789546, 57.0987654563232, 23.454662],
                "places": 7,
            },
            {
                "_": "lists mismatch",
                "first": [57.0987654323335, 12.3456789123],
                "second": [12.3456789546, 57.0987654563232],
                "places": 7,
            },
            {
                "_": "list and non iterable",
                "first": [57.0987654323335, 12.3456789123],
                "second": 12.3456789546,
                "places": 7,
            },
            {
                "_": "non iterable and list",
                "first": 57.0987654323335,
                "second": [12.3456789546, 57.0987654563232],
                "places": 7,
            },
            {
                "_": "n-dim lists",
                "first": [
                    [12.3456789123, 57.0987654323335],
                    [3.4546565465, 4.433325286767, 5.343543543],
                ],
                "second": [
                    [12.3456789546, 57.0987654563232],
                    [3.4546565324, 4.434325276767, 5.343543522],
                ],
                "places": 7,
            },
        ]
    )
    def test_lists_almost_equal_fail(self, _, first, second, places):
        """Tests 2 lists of floats are not almost equal"""
        try:
            self.assertListsAlmostEqual(first, second, places)
        except AssertionError:
            pass
        else:
            raise AssertionError("lists are not almost equal")  # pragma: no cover

    @test_cases(
        [
            {
                "_": "first list is longer",
                "first": [12.3456789123, 57.0987654323335, 23.454662],
                "second": [12.3456789546, 57.0987654563232],
                "places": 7,
            },
            {
                "_": "second list is longer",
                "first": [12.3456789123, 57.0987654323335],
                "second": [12.3456789546, 57.0987654563232, 23.454662],
                "places": 7,
            },
            {
                "_": "lists mismatch",
                "first": [57.0987654323335, 12.3456789123],
                "second": [12.3456789546, 57.0987654563232],
                "places": 7,
            },
        ]
    )
    def test_lists_not_almost_equal(self, _, first, second, places):
        """Tests 2 lists of floats are not almost equal"""
        self.assertListsNotAlmostEqual(first, second, places)

    @test_cases(
        [
            {
                "_": "floats",
                "first": 12.3456789123,
                "second": 12.3456789546,
                "places": 5,
            },
            {
                "_": "lists",
                "first": [12.3456789123, 57.0987654323335],
                "second": [12.3456789546, 57.0987654563232],
                "places": 7,
            },
            {
                "_": "n-dim lists",
                "first": [
                    [12.3456789123, 57.0987654323335],
                    [3.4546565465, 4.434325286767, 5.343543543],
                ],
                "second": [
                    [12.3456789546, 57.0987654563232],
                    [3.4546565324, 4.434325276767, 5.343543522],
                ],
                "places": 7,
            },
            {
                "_": "tuples",
                "first": (12.3456779123, 57.0987644323335),
                "second": (12.3456789546, 57.0987654563232),
                "places": 5,
            },
            {
                "_": "sets",
                "first": {12.3456789123, 57.0987654323335},
                "second": {12.3456789546, 57.0987654563232},
                "places": 7,
            },
            {
                "_": "dicts",
                "first": {"a": 12.3456789123, "b": [57.0987654323335, 2.24343545354]},
                "second": {"a": 12.3456789546, "b": [57.0987654563232, 2.24343545764]},
                "places": 7,
            },
            {
                "_": "mix list and dict",
                "first": [12.3456789123, 57.0987654323335],
                "second": {"a": 12.3456789546, "b": 57.0987654563232},
                "places": 7,
            },
        ]
    )
    def test_lists_not_almost_equal_fail(self, _, first, second, places):
        """Tests 2 lists of floats are almost equal"""
        try:
            self.assertListsNotAlmostEqual(first, second, places)
        except AssertionError:
            pass
        else:
            raise AssertionError("lists are not almost equal")  # pragma: no cover
