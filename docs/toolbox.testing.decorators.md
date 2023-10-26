<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/testing/decorators.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.testing.decorators`
A collection of decorators for testing purpose. 



**Examples:**
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


---

<a href="../src/cerbernetix/toolbox/testing/decorators.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `test_cases`

```python
test_cases(cases: list[dict | list]) → Callable
```

Creates a decorator for parametric test cases. 



**Args:**
 
 - <b>`cases`</b> (list[dict | dict]):  The list of parameters for each test case. The parameters can be given either as a list of positioned arguments, or either as a dictionary of named arguments. In both cases, the parameters must be present in the signature of the test method. The name of the case will be either the first arguments, when a list is given, or the named argument from ('title', 'message', '_') when a dictionary is given. 



**Returns:**
 
 - <b>`Callable`</b>:  The decorator that binds the list of test cases with the test method. 



**Raises:**
 
 - <b>`ValueError`</b>:  If there no test cases supplied. 



**Examples:**
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




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
