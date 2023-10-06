"""Test the tool for extracting values from a set of possible entries."""
import unittest

from toolbox.data import ValueExtractor, passthrough
from toolbox.testing import test_cases


class TestValueExtractor(unittest.TestCase):
    """Test suite for the value extractor."""

    def test_construction(self):
        """Tests the construction of a value extractor."""
        extractor = ValueExtractor(["foo"])
        self.assertEqual(extractor.entries, ("foo",))
        self.assertEqual(extractor.mapper, passthrough)

        extractor = ValueExtractor("foo")
        self.assertEqual(extractor.entries, ("foo",))
        self.assertEqual(extractor.mapper, passthrough)

        extractor = ValueExtractor(["foo", "bar"], int)
        self.assertEqual(extractor.entries, ("foo", "bar"))
        self.assertEqual(extractor.mapper, int)

        self.assertRaises(ValueError, lambda: ValueExtractor([], True))

    @test_cases(
        [
            [
                ["date", "time", "day"],
                None,
                [
                    ({"date": "2023-10-06"}, "2023-10-06"),
                    ({"day": "2023-02-20"}, "2023-02-20"),
                    ({"time": "2023-06-12"}, "2023-06-12"),
                    ({"foo": "2023-06-12"}, None),
                ],
            ],
            [
                ["value", "val", "number"],
                int,
                [
                    ({"val": "42"}, 42),
                    ({"value": 12}, 12),
                    ({"number": 100}, 100),
                    ({"foo": 18}, None),
                ],
            ],
        ]
    )
    def test_extract(self, entries, mapper, data):
        """Tests a value can be extracted."""
        extractor = ValueExtractor(entries, mapper)
        for row, value in data:
            self.assertEqual(extractor.extract(row), value)
