"""Test the class for handling config options."""
import unittest

from toolbox.config import ConfigOption, create_options
from toolbox.data import boolean, passthrough
from toolbox.testing import test_cases


class TestConfigOption(unittest.TestCase):
    """Test suite for the class for handling a config option."""

    @test_cases(
        [
            [
                "Name",
                {"name": "foo"},
                "foo",
                None,
                None,
                "",
                passthrough,
                (),
            ],
            [
                "Value",
                {"name": "foo", "value": "bar"},
                "foo",
                "bar",
                None,
                "",
                passthrough,
                (),
            ],
            [
                "Default",
                {"name": "foo", "default": "bar"},
                "foo",
                None,
                "bar",
                "",
                passthrough,
                (),
            ],
            [
                "Description",
                {"name": "foo", "description": "bar"},
                "foo",
                None,
                None,
                "bar",
                passthrough,
                (),
            ],
            [
                "Mapper",
                {"name": "foo", "mapper": str},
                "foo",
                None,
                None,
                "",
                str,
                (),
            ],
            [
                "Choices with value",
                {"name": "foo", "value": "bar", "choices": ["foo", "bar"]},
                "foo",
                "bar",
                None,
                "",
                passthrough,
                ("foo", "bar"),
            ],
            [
                "Choices with default",
                {"name": "foo", "default": "bar", "choices": ["foo", "bar"]},
                "foo",
                None,
                "bar",
                "",
                passthrough,
                ("foo", "bar"),
            ],
        ]
    )
    def test_create_option(
        self, _, params, name, value, default, description, mapper, choices
    ):
        """Test the creation of an option."""

        option = ConfigOption(**params)
        self.assertEqual(option.name, name)
        self.assertEqual(option.value, value)
        self.assertEqual(option.default, default)
        self.assertEqual(option.description, description)
        self.assertEqual(option.mapper, mapper)
        self.assertEqual(option.choices, choices)

    def test_create_option_fail(self):
        """Test the creation of an option raises an error."""
        self.assertRaises(ValueError, lambda: ConfigOption(""))
        self.assertRaises(ValueError, lambda: ConfigOption("foo", mapper=True))
        self.assertRaises(ValueError, lambda: ConfigOption("foo", choices=["bar"]))
        self.assertRaises(
            ValueError, lambda: ConfigOption("foo", value="baz", choices=["bar"])
        )
        self.assertRaises(
            ValueError, lambda: ConfigOption("foo", default="baz", choices=["bar"])
        )

    def test_copy_option(self):
        """Test the copy of an option."""
        name = "foo"
        value = "bar"
        default = "baz"
        description = "Foo bar"
        mapper = str
        choices = ("foo", "bar", "baz")

        option = ConfigOption(
            name=name,
            value=value,
            default=default,
            description=description,
            mapper=mapper,
            choices=choices,
        )
        option2 = option.copy()

        self.assertEqual(option2, option)
        self.assertIsNot(option2, option)

        self.assertEqual(option2.name, name)
        self.assertEqual(option2.value, value)
        self.assertEqual(option2.default, default)
        self.assertEqual(option2.description, description)
        self.assertEqual(option2.mapper, mapper)
        self.assertEqual(option2.choices, choices)

        option.set("foo")
        self.assertEqual(option.get(), "foo")
        self.assertEqual(option2.get(), "bar")

    @test_cases(
        [
            [
                "No value",
                {"name": "foo"},
                {
                    "name": "foo",
                    "value": None,
                    "default": None,
                    "description": "",
                    "mapper": passthrough,
                    "choices": (),
                },
            ],
            [
                "No value with mapper",
                {"name": "foo", "mapper": str},
                {
                    "name": "foo",
                    "value": None,
                    "default": None,
                    "description": "",
                    "mapper": str,
                    "choices": (),
                },
            ],
            [
                "Default value",
                {"name": "foo", "default": "bar"},
                {
                    "name": "foo",
                    "value": None,
                    "default": "bar",
                    "description": "",
                    "mapper": passthrough,
                    "choices": (),
                },
            ],
            [
                "Mapped value",
                {"name": "foo", "value": 10, "mapper": str},
                {
                    "name": "foo",
                    "value": "10",
                    "default": None,
                    "description": "",
                    "mapper": str,
                    "choices": (),
                },
            ],
            [
                "Mapped default",
                {"name": "foo", "default": 10, "mapper": str},
                {
                    "name": "foo",
                    "value": None,
                    "default": "10",
                    "description": "",
                    "mapper": str,
                    "choices": (),
                },
            ],
            [
                "Description",
                {"name": "foo", "value": 0, "default": 10, "description": "FooBar"},
                {
                    "name": "foo",
                    "value": 0,
                    "default": 10,
                    "description": "FooBar",
                    "mapper": passthrough,
                    "choices": (),
                },
            ],
            [
                "Choices",
                {"name": "foo", "value": 0, "default": 10, "choices": [0, 1, 10]},
                {
                    "name": "foo",
                    "value": 0,
                    "default": 10,
                    "description": "",
                    "mapper": passthrough,
                    "choices": (0, 1, 10),
                },
            ],
        ]
    )
    def test_get_dict(self, _, params, value):
        """Test the option is returned as a dictionary."""
        option = ConfigOption(**params)
        self.assertEqual(option.get_dict(), value)

    @test_cases(
        [
            ["No value", {"name": "foo"}, None],
            ["No value with mapper", {"name": "foo", "mapper": str}, None],
            ["Default value", {"name": "foo", "default": "bar"}, "bar"],
            ["Mapped value", {"name": "foo", "value": 10, "mapper": str}, "10"],
            ["Mapped default", {"name": "foo", "default": 10, "mapper": str}, "10"],
        ]
    )
    def test_get(self, _, params, value):
        """Test the access to the value."""
        option = ConfigOption(**params)
        self.assertEqual(option.get(), value)

    @test_cases(
        [
            ["No value", {"name": "foo"}, None, None, None],
            ["No value with mapper", {"name": "foo", "mapper": str}, None, None, None],
            ["Default value", {"name": "foo", "default": "bar"}, "foo", "foo", "foo"],
            ["Mapped value", {"name": "foo", "mapper": str}, 10, "10", "10"],
            [
                "Mapped default",
                {"name": "foo", "default": 10, "mapper": str},
                20,
                "20",
                "20",
            ],
            ["Reset value", {"name": "foo", "value": 10}, None, None, None],
            [
                "Reset default",
                {"name": "foo", "value": 10, "default": 20},
                None,
                None,
                20,
            ],
            ["Choice", {"name": "foo", "value": 10, "choices": [10, 20]}, 20, 20, 20],
        ]
    )
    def test_set(self, _, params, value_set, value_return, value_get):
        """Test the modification of the value."""
        option = ConfigOption(**params)
        self.assertEqual(option.set(value_set), value_return)
        self.assertEqual(option.get(), value_get)

    @test_cases(
        [
            [
                "No value and no default",
                {"name": "foo", "value": 1, "choices": [1, 2]},
                None,
            ],
            [
                "Value out of choices",
                {"name": "foo", "default": 1, "choices": [1, 2]},
                3,
            ],
        ]
    )
    def test_set_fail(self, _, params, value):
        """Test the modification of the value raises an error."""
        option = ConfigOption(**params)
        self.assertRaises(ValueError, lambda: option.set(value))

    @test_cases(
        [
            ["No value and no default", {"name": "foo"}, None, None],
            ["Value", {"name": "foo", "value": 10}, None, None],
            ["Default", {"name": "foo", "default": 10}, None, 10],
            ["Value and default", {"name": "foo", "value": 0, "default": 10}, None, 10],
        ]
    )
    def test_reset_value(self, _, params, raw_value, value):
        """Test the reset to the default value."""
        option = ConfigOption(**params)

        option.reset()

        self.assertEqual(option.value, raw_value)
        self.assertEqual(option.get(), value)

    def test_reset_value_fail(self):
        """Test the reset to the default value raises an error."""
        option = ConfigOption("foo", value=10, choices=[10])

        self.assertRaises(ValueError, option.reset)

    @test_cases(
        [
            ["No value", {"name": "foo"}, None, None, None],
            ["No value with mapper", {"name": "foo", "mapper": str}, None, None, None],
            ["Default value", {"name": "foo", "default": "bar"}, "foo", "foo", "foo"],
            ["Mapped value", {"name": "foo", "mapper": str}, 10, "10", "10"],
            [
                "Mapped default",
                {"name": "foo", "default": 10, "mapper": str},
                20,
                "20",
                "20",
            ],
            ["Remove default", {"name": "foo", "value": 10}, None, None, None],
            ["Choice", {"name": "foo", "value": 10, "choices": [10, 20]}, 20, 20, 20],
        ]
    )
    def test_set_default(self, _, params, value_set, value_return, value_get):
        """Test the modification of the default value."""
        option = ConfigOption(**params)
        self.assertEqual(option.set_default(value_set), value_return)
        self.assertEqual(option.default, value_get)

    @test_cases(
        [
            [
                "No value and no default",
                {"name": "foo", "default": 1, "choices": [1, 2]},
                None,
            ],
            [
                "Value out of choices",
                {"name": "foo", "default": 1, "choices": [1, 2]},
                3,
            ],
        ]
    )
    def test_set_default_fail(self, _, params, value):
        """Test the modification of the default value raises an error."""
        option = ConfigOption(**params)
        self.assertRaises(ValueError, lambda: option.set_default(value))

    @test_cases(
        [
            ["No description", {"name": "foo"}, None, ""],
            ["Set description", {"name": "foo"}, "foo", "foo"],
        ]
    )
    def test_set_description(self, _, params, description_set, description_get):
        """Test the modification of the description."""
        option = ConfigOption(**params)
        option.set_description(description_set)
        self.assertEqual(option.description, description_get)

    @test_cases(
        [
            ["Passthrough of None", passthrough, None, None],
            ["Passthrough of value", passthrough, "foo", "foo"],
            ["Int to string", str, 123, "123"],
            ["Float to string", str, 12.3, "12.3"],
            ["True to string", str, True, "True"],
            ["False to string", str, False, "False"],
            ["String to int", int, "123", 123],
            ["String to float", float, "12.3", 12.3],
            ["String to True", boolean, "true", True],
            ["String to False", boolean, "false", False],
        ]
    )
    def test_cast(self, _, mapper, value_set, value_get):
        """Test the conversion of the value."""
        option = ConfigOption("foo", mapper=mapper)

        self.assertEqual(option.cast(value_set), value_get)

    @test_cases(
        [
            ["No value", "foo", None, "foo=None"],
            ["String value", "foo_s", "bar", "foo_s=bar"],
            ["Int value", "foo_i", 42, "foo_i=42"],
            ["Float value", "foo_f", 4.2, "foo_f=4.2"],
            ["Bool value", "foo_b", True, "foo_b=True"],
            ["List value", "foo_l", [1, 2, 3], "foo_l=[1, 2, 3]"],
        ]
    )
    def test_str(self, _, name, value, string):
        """Test the string representation of the option."""
        option = ConfigOption(name, value)

        self.assertEqual(str(option), string)

    def test_eq(self):
        """Test the equality of options."""
        foo10 = ConfigOption("foo", 10)
        foo20 = ConfigOption("foo", 20)
        bar10 = ConfigOption("bar", 10)

        self.assertEqual(foo10, foo10)
        self.assertEqual(foo10, foo10.copy())
        self.assertNotEqual(foo10, foo20)
        self.assertNotEqual(foo10, bar10)
        self.assertNotEqual(foo10, "foo10")


class TestCreateOptions(unittest.TestCase):
    """Test suite for the helper create_options()."""

    def test_create_options(self):
        """Test that options are created from a list."""
        source = [
            ConfigOption("foo", "bar", "baz"),
            {"name": "foo", "value": "bar", "default": "baz"},
            ["foo", "bar", "baz"],
            "foo",
        ]

        options = iter(create_options(source))

        for idx in range(3):
            option = next(options)
            self.assertIsNot(option, source[idx])
            self.assertEqual(option.name, "foo")
            self.assertEqual(option.value, "bar")
            self.assertEqual(option.default, "baz")

        option = next(options)
        self.assertEqual(option.name, "foo")
        self.assertEqual(option.value, None)
        self.assertEqual(option.default, None)
