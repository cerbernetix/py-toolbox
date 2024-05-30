"""Test the set of helpers for types management."""

import unittest

from cerbernetix.toolbox.system import full_type


class TestType(unittest.TestCase):
    """Test suite for the set of helpers for types management."""

    def test_full_type(self):
        """Test full_type."""
        self.assertEqual(full_type(None), "None")
        self.assertEqual(full_type(""), "builtins.str")
        self.assertEqual(full_type([]), "builtins.list")
        self.assertEqual(full_type({}), "builtins.dict")
        self.assertEqual(full_type(full_type), "cerbernetix.toolbox.system.type.full_type")
        self.assertEqual(full_type(self), "tests.system.test_type.TestType")
