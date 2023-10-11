<!-- markdownlint-disable -->

<a href="../src/toolbox/testing/test_case.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.testing.test_case`
Extends the default Python TestCase with more assertions. 



**Examples:**
 ```python
from toolbox import testing

class TestMyStuff(testing.TestCase)
     def test_list(self):
         self.assertListsAlmostEqual(generator(), [1.23, 3.14, 1.61])

     def test_dict(self):
         self.assertListsAlmostEqual(create_dict(), {"value": 42.4242, "PI": 3.1415})
``` 



---

<a href="../src/toolbox/testing/test_case.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TestCase`
Test class with additional assertions. 




---

<a href="../src/toolbox/testing/test_case.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `assertListsAlmostEqual`

```python
assertListsAlmostEqual(
    first: Iterable[float],
    second: Iterable[float],
    places: int = 7
)
```

Asserts that 2 lists of float numbers are almost equal by the number of places. 



**Args:**
 
 - <b>`first`</b> (Iterable[float]):  The first list to compare. 
 - <b>`second`</b> (Iterable[float]):  The second list to compare. 
 - <b>`places`</b> (int, optional):  The number of decimal places under what the numbers must be equal. Defaults to 7. 



**Raises:**
 
 - <b>`AssertionError`</b>:  If the 2 lists are not almost equals by the number of places. 



**Examples:**
 ```python
from toolbox import testing

class TestMyStuff(testing.TestCase)
    def test_almost_equal(self):
         self.assertListsAlmostEqual(generator(), [1.23, 3.14, 1.61])
``` 

---

<a href="../src/toolbox/testing/test_case.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `assertListsNotAlmostEqual`

```python
assertListsNotAlmostEqual(
    first: Iterable[float],
    second: Iterable[float],
    places: int = 7
)
```

Asserts that 2 lists of float numbers are not almost equal by the number of places. 



**Args:**
 
 - <b>`first`</b> (Iterable[float]):  The first list to compare. 
 - <b>`second`</b> (Iterable[float]):  The second list to compare. 
 - <b>`places`</b> (int, optional):  The number of decimal places under what the numbers must be equal. Defaults to 7. 



**Raises:**
 
 - <b>`AssertionError`</b>:  If the 2 lists are almost equals by the number of places. 



**Examples:**
 ```python
from toolbox import testing

class TestMyStuff(testing.TestCase)
    def test_almost_equal(self):
         self.assertListsNotAlmostEqual(generator(), [1.23, 3.14, 1.61])
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
