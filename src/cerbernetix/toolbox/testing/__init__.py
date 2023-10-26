"""The `testing` package provides utilities for testing purpose.

It contains:
- `test_cases(cases)` - Decorates a test case with parameters.
- `TestCase` - Extends the default Python TestCase with more assertions.

Examples:
```python
from cerbernetix.toolbox import testing

class TestMyStuff(testing.TestCase)

    # Parameters can be given either as list of arguments or either as dictionary.
    # In both cases, the parameters must be present in the signature of the test method.
    @testing.test_cases([
        ["adding numbers", [10, 20, 12], 42],
        {
            "title": "returning numbers",
            "params": [100],
            "expected": 100,
        },
    ])
    def test_addition(self, title, params, expected):
        self.assertEqual(addition(*params), expected)

    def test_list(self):
        self.assertListsAlmostEqual(generator(), [1.23, 3.14, 1.61])
```
"""
from cerbernetix.toolbox.testing.decorators import test_cases
from cerbernetix.toolbox.testing.test_case import TestCase
