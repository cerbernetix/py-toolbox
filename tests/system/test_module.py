"""Test the set of helpers for loading properties dynamically."""

import unittest
from unittest.mock import patch

from cerbernetix.toolbox.system import import_callable, import_prop


class TestModule(unittest.TestCase):
    """Test suite for the set of helpers for loading properties dynamically."""

    @patch("importlib.import_module")
    def test_import_prop(self, import_module):
        """Test import_prop."""

        class _Module:
            prop = "foo"

        module_name = "foo.bar"
        prop_name = "prop"
        import_module.return_value = _Module()
        self.assertIs(import_prop(f"{module_name}.{prop_name}"), _Module.prop)
        self.assertIs(import_prop("foo"), None)
        self.assertIs(import_prop(None), None)

        import_module.assert_called_with(module_name)

    @patch("importlib.import_module")
    def test_import_callable(self, import_module):
        """Test import_callable."""

        class _Module:
            prop = "foo"

            def fn(self, prm="default"):
                """mock function"""
                return prm

        module_name = "foo.bar"
        import_module.return_value = _Module()
        self.assertEqual(import_callable(f"{module_name}.fn"), "default")
        self.assertEqual(import_callable(f"{module_name}.fn", "foo"), "foo")
        self.assertRaises(TypeError, lambda: import_callable(f"{module_name}.foo"))

        import_module.assert_called_with(module_name)
