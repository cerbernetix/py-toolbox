"""Test the class for handling a configuration."""
import unittest

from toolbox.config import Config, ConfigOption
from toolbox.data.mappers import passthrough
from toolbox.testing import test_cases


class TestConfig(unittest.TestCase):
    """Test suite for the class for handling a configuration."""

    @test_cases(
        [
            ["Empty", {}, []],
            [
                "List of values",
                {"config": {"foo": "bar", "value": 42}},
                [("foo", "bar"), ("value", 42)],
            ],
            [
                "List of option",
                {"options": [ConfigOption("a"), {"name": "b", "value": 1}, ["c", 2]]},
                [("a", None), ("b", 1), ("c", 2)],
            ],
            [
                "Values and options",
                {
                    "config": {"foo": "bar", "value": 42},
                    "options": [
                        ConfigOption("foo"),
                        {"name": "value", "value": 1},
                        ["date", "2023-09-12"],
                    ],
                },
                [("foo", "bar"), ("value", 42), ("date", "2023-09-12")],
            ],
        ]
    )
    def test_config(self, _, params, values):
        """Test the creation of a configuration."""
        config = Config(**params)

        self.assertEqual(list(config), values)

    def test_keys(self):
        """Test the list of option names is returned."""
        config = Config(
            options=[
                ConfigOption("a"),
                ConfigOption("b"),
                ConfigOption("c"),
            ]
        )

        self.assertEqual(list(config.keys()), ["a", "b", "c"])

    def test_has(self):
        """Test an option exists."""
        config = Config()

        self.assertFalse(config.has("foo"))

        config.set_option("foo")

        self.assertTrue(config.has("foo"))

    def test_get(self):
        """Test getting the value of an option."""
        config = Config()

        self.assertIsNone(config.get("foo"))

        self.assertEqual(config.get("foo", "default"), "default")

        config.set_option("foo", default="bar")

        self.assertEqual(config.get("foo"), "bar")

        config.set("foo", "baz")

        self.assertEqual(config.get("foo"), "baz")

    def test_set(self):
        """Test setting the value of an option."""
        config = Config()

        self.assertIsNone(config.get("foo"))
        self.assertFalse(config.has("foo"))

        self.assertEqual(config.set("foo", "bar"), "bar")

        self.assertEqual(config.get("foo"), "bar")
        self.assertTrue(config.has("foo"))

        config.set_option("bar", 100, 200, choices=[100, 200, 300])

        self.assertEqual(config.get("bar"), 100)

        config.set("bar", 200)

        self.assertEqual(config.get("bar"), 200)

        config.set("bar", None)

        self.assertEqual(config.get("bar"), 200)

        self.assertRaises(ValueError, lambda: config.set("bar", 400))

    def test_reset(self):
        """Test resetting the value of an option."""
        config = Config(
            options=[
                {"name": "foo", "value": "foo", "default": "bar"},
                {"name": "bar", "value": "foo"},
            ]
        )

        self.assertEqual(config.get("foo"), "foo")
        self.assertEqual(config.get("bar"), "foo")
        self.assertEqual(config.get("baz"), None)

        config.reset("foo")
        config.reset("bar")
        config.reset("baz")

        self.assertEqual(config.get("foo"), "bar")
        self.assertEqual(config.get("bar"), None)
        self.assertEqual(config.get("baz"), None)

    def test_drop(self):
        """Test dropping an option."""
        config = Config(options=["foo", "bar"])

        self.assertTrue(config.has("foo"))
        self.assertTrue(config.has("bar"))
        self.assertFalse(config.has("baz"))

        self.assertTrue(config.drop("foo"))
        self.assertFalse(config.drop("foo"))
        self.assertFalse(config.drop("baz"))

        self.assertFalse(config.has("foo"))
        self.assertTrue(config.has("bar"))
        self.assertFalse(config.has("baz"))

    def test_describe(self):
        """Test the description of an option can be retrieved."""
        config = Config(
            options=[
                ConfigOption("a", default="A", description="foo"),
                ConfigOption("b", default="B"),
            ]
        )

        self.assertEqual(config.describe("a"), "foo")
        self.assertEqual(config.describe("b"), "")

    def test_choices(self):
        """Test the choices of an option can be retrieved."""
        config = Config(
            options=[
                ConfigOption("a", default=10, choices=[10, 20]),
                ConfigOption("b", default=10),
            ]
        )

        self.assertEqual(config.choices("a"), (10, 20))
        self.assertEqual(config.choices("b"), ())
        self.assertEqual(config.choices("c"), ())

    def test_get_option(self):
        """Test the option is returned."""
        options = [
            ConfigOption("a"),
            ConfigOption("b"),
        ]
        config = Config(options=options)

        self.assertIsInstance(config.get_option("a"), ConfigOption)
        self.assertEqual(config.get_option("a"), options[0])

        self.assertIsInstance(config.get_option("b"), ConfigOption)
        self.assertEqual(config.get_option("b"), options[1])

        self.assertIsNone(config.get_option("c"))

    def test_set_option(self):
        """Test the creation of configuration options."""
        config = Config()

        self.assertFalse(config.has("a"))

        config.set_option("a", 10, "-1", "foo", int, [-1, 10])

        self.assertTrue(config.has("a"))
        self.assertEqual(config.get("a"), 10)
        self.assertEqual(config.describe("a"), "foo")
        self.assertRaises(ValueError, lambda: config.set("a", 20))

        config.reset("a")
        self.assertEqual(config.get("a"), -1)

    def test_get_options(self):
        """Test the options are exported."""
        config = Config(
            options=[
                ConfigOption("a", 1, 10, "A"),
                ConfigOption("b", default="B", choices=["b", "B"]),
                ConfigOption("c", 10, mapper=str),
            ]
        )

        self.assertEqual(
            config.get_options(),
            [
                {
                    "name": "a",
                    "value": 1,
                    "default": 10,
                    "description": "A",
                    "mapper": passthrough,
                    "choices": (),
                },
                {
                    "name": "b",
                    "value": None,
                    "default": "B",
                    "description": "",
                    "mapper": passthrough,
                    "choices": ("b", "B"),
                },
                {
                    "name": "c",
                    "value": "10",
                    "default": None,
                    "description": "",
                    "mapper": str,
                    "choices": (),
                },
            ],
        )

    def test_get_config(self):
        """Tests that the configuration options are exported."""
        config = Config(
            options=[
                ConfigOption("a", "A"),
                ConfigOption("b", default="B"),
                ConfigOption("v", 10, default=42),
            ]
        )
        export = config.get_config()
        expected = {
            "a": "A",
            "b": "B",
            "v": 10,
        }

        self.assertEqual(export, expected)

    def test_set_config(self):
        """Tests that the configuration options are imported."""
        config = Config(
            options=[
                ConfigOption("a"),
                ConfigOption("b"),
                ConfigOption("v", default=-1, mapper=int, choices=[-1, 10]),
            ]
        )
        export = {
            "a": "A",
            "b": "B",
            "c": "foo",
            "v": 10,
        }

        config.set_config(export)

        self.assertEqual(config.get("a"), export["a"])
        self.assertEqual(config.get("b"), export["b"])
        self.assertEqual(config.get("c"), export["c"])
        self.assertEqual(config.get("v"), export["v"])

        self.assertRaises(ValueError, lambda: config.set_config({"v": 20}))

    def test_reset_config(self):
        """Test the options are reset to their default value."""
        config = Config(
            options=[
                ConfigOption("a", "a", "A"),
                ConfigOption("b", "b", "B"),
            ]
        )

        self.assertEqual(config.get("a"), "a")
        self.assertEqual(config.get("b"), "b")

        config.reset_config()

        self.assertEqual(config.get("a"), "A")
        self.assertEqual(config.get("b"), "B")

    def test_array_access(self):
        """Test the access to a configuration option."""
        config = Config(
            options=[
                ConfigOption("a", default="A"),
                ConfigOption("b", default="B"),
                ConfigOption("v", default=42),
            ]
        )

        self.assertEqual(len(config), 3)

        self.assertIn("a", config)
        self.assertIn("b", config)
        self.assertNotIn("c", config)
        self.assertIn("v", config)

        self.assertEqual(config["a"], "A")
        self.assertEqual(config["b"], "B")
        self.assertRaises(IndexError, lambda: config["c"])
        self.assertEqual(config["v"], 42)

        config["a"] = "123"
        config["b"] = "456"
        config["c"] = "foo"
        config["v"] = 10

        self.assertEqual(config["a"], "123")
        self.assertEqual(config["b"], "456")
        self.assertEqual(config["c"], "foo")
        self.assertEqual(config["v"], 10)

        options = [
            ("a", "123"),
            ("b", "456"),
            ("v", 10),
            ("c", "foo"),
        ]
        self.assertEqual(list(config), options)

        del config["a"]
        self.assertNotIn("a", config)
        self.assertRaises(IndexError, lambda: config["a"])

    def test_direct_access(self):
        """Test the access to a configuration option."""
        config = Config(
            options=[
                ConfigOption("a", default="A"),
                ConfigOption("b", default="B"),
                ConfigOption("v", default=42),
            ]
        )

        self.assertEqual(config.a, "A")
        self.assertEqual(config.b, "B")
        self.assertRaises(AttributeError, lambda: config.c)
        self.assertEqual(config.v, 42)

    def test_str(self):
        """Test the access to a configuration option."""
        config = Config({"a": "A", "b": "B", "v": 42})

        string = "a=A\nb=B\nv=42"

        self.assertEqual(str(config), string)
