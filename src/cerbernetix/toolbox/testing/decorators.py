"""A collection of decorators for testing purpose.

Examples:
```python
from cerbernetix.toolbox import testing

# Parameters can be given either as list of arguments or either as dictionaries.
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
```
"""
import functools
from typing import Callable


def test_cases(cases: list[dict | list]) -> Callable:
    """Creates a decorator for parametric test cases.

    Args:
        cases (list[dict | dict]): The list of parameters for each test case. The parameters can
        be given either as a list of positioned arguments, or either as a dictionary of named
        arguments. In both cases, the parameters must be present in the signature of the test
        method. The name of the case will be either the first arguments, when a list is given,
        or the named argument from ('title', 'message', '_') when a dictionary is given.

    Returns:
        Callable: The decorator that binds the list of test cases with the test method.

    Raises:
        ValueError: If there no test cases supplied.

    Examples:
    ```python
    from cerbernetix.toolbox.testing import test_cases
    @test_cases([
        ["adding numbers", [10, 20, 12], 42],
        {
            "title": "returning numbers",
            "params": [100],
            "expected": 100,
        },
    ])
    def test_addition(self, title, params, expected):
        self.assertEqual(addition(*params), expected)
    ```
    """
    if not isinstance(cases, (list, tuple)) or len(cases) == 0:
        raise ValueError("A list of test cases is required.")

    def decorator(method) -> Callable:
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs) -> None:
            for index, case in enumerate(cases):
                title = f"case {index}"
                case_args = args
                case_kwargs = kwargs

                if isinstance(case, dict):
                    title = case.get("title", case.get("message", case.get("_", title)))
                    case_kwargs = {**kwargs, **case}

                elif isinstance(case, (list, tuple)):
                    title = case[0] or title
                    case_args = list(case) + list(args)

                else:
                    case_args = [case] + list(args)

                with self.subTest(title):
                    method(self, *case_args, **case_kwargs)

        return wrapper

    return decorator
