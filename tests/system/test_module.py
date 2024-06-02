"""Test the set of helpers for loading properties dynamically."""

import unittest
from unittest.mock import patch

from cerbernetix.toolbox.system import import_and_call, import_property


class TestModule(unittest.TestCase):
    """Test suite for the set of helpers for loading properties dynamically."""

    @patch("importlib.import_module")
    def test_import_property(self, import_module):
        """Test import_property."""

        class _Module:
            prop = "foo"

        module_name = "foo.bar"
        prop_name = "prop"
        import_module.return_value = _Module()
        self.assertIs(import_property(f"{module_name}.{prop_name}"), _Module.prop)
        self.assertIs(import_property("foo"), None)
        self.assertIs(import_property(None), None)

        import_module.assert_called_with(module_name)

    @patch("importlib.import_module")
    def test_import_and_call(self, import_module):
        """Test import_and_call."""

        class _Module:
            prop = "foo"

            def fn(self, prm="default"):
                """mock function"""
                return prm

        module_name = "foo.bar"
        import_module.return_value = _Module()
        self.assertEqual(import_and_call(f"{module_name}.fn"), "default")
        self.assertEqual(import_and_call(f"{module_name}.fn", "foo"), "foo")
        self.assertRaises(TypeError, lambda: import_and_call(f"{module_name}.foo"))

        import_module.assert_called_with(module_name)
