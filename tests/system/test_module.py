"""Test the set of helpers for loading properties dynamically."""

import unittest
from unittest.mock import patch

from cerbernetix.toolbox.system import import_prop


class TestModule(unittest.TestCase):
    """Test suite for the set of helpers for loading properties dynamically."""

    @patch("importlib.import_module")
    def test_import_prop(self, import_module):
        """Test import_prop."""

        class _Module:
            prop = "foo"

        module_name = "foo.bar"
        prop_name = "prop"
        namespace = f"{module_name}.{prop_name}"
        import_module.return_value = _Module()
        self.assertIs(import_prop(namespace), _Module.prop)
        self.assertIs(import_prop("foo"), None)
        self.assertIs(import_prop(None), None)

        import_module.assert_called_with(module_name)
