<!-- markdownlint-disable -->

<a href="../src/toolbox/config/config_option.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.config.config_option`
A class for handling config options. 



**Examples:**
 ```python
from toolbox.config import ConfigOption

# Create a few options
name = ConfigOption("name", mapper=str, default="")
age = ConfigOption("age", mapper=int, default=0)

# Show some information
print(name, age)

# Set option values
name.set("John")
age.set("20")

# Get the values
print(name.get()) # "John"
print(age.get())  # 20
``` 


---

<a href="../src/toolbox/config/config_option.py#L418"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_options`

```python
create_options(options: 'Iterable') → Iterator[ConfigOption]
```

Create options from a list of descriptors. 

Depending on the type of the descriptor, the following will be done: 
- If it is a config option, a copy is yielded. 
- If it is a dictionary, a config option is created from the named parameters. 
- If it is a list or a tuple, a config option is created from the positioned parameters. 
- For any other types, a config option is created from the single parameter. 



**Args:**
 
 - <b>`options`</b> (Iterable):  A list of config option descriptor to create options from. 



**Yields:**
 
 - <b>`Iterator[ConfigOption]`</b>:  A config option created from the descriptor. 



**Examples:**
 ```python
from toolbox.config import create_options

for option in create_options([
    ConfigOption("foo"), # a copy will be created
    {"name": "foo"},     # will call ConfigOption(name="foo")
    ["foo"],             # will call ConfigOption("foo")
    "foo",               # will call ConfigOption("foo")
]):
    print(option)
``` 


---

<a href="../src/toolbox/config/config_option.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ConfigOption`
Handles a config option. 

Each config option must be named. They can have a default value that will be returned while the value is not set. 

A mapper is responsible for casting the value to the correct type and format. 

Options can have a description, and can be constrained to a list of possible values. 



**Attributes:**
 
 - <b>`name`</b> (str, readonly):  The name of the option. 
 - <b>`value`</b> (Any, readonly):  The current value of the option. 
 - <b>`default`</b> (Any, readonly):  The default value for the option. 
 - <b>`description`</b> (str, readonly):  A description of the option. 
 - <b>`mapper`</b> (ValueMapper, readonly):  The mapper applied to cast and format the value. 
 - <b>`choices`</b> (tuple, readonly):  The list of possible values for the option. 





**Examples:**
 ```python
from toolbox.config import ConfigOption

name = ConfigOption("name", mapper=str, default="bob")

print(name.get()) # "bob"

name.set("John")

print(name.get()) # "John"
``` 

<a href="../src/toolbox/config/config_option.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    name: 'str',
    value: 'Any' = None,
    default: 'Any' = None,
    description: 'str' = '',
    mapper: 'ValueMapper' = None,
    choices: 'Iterable' = None
) → None
```

Creates a named configuration option. 

The name is mandatory. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the option. 
 - <b>`value`</b> (Any, optional):  The initial value of the option. Defaults to None. 
 - <b>`default`</b> (Any, optional):  The value returned when there is no defined value. Defaults to None. 
 - <b>`description`</b> (str, optional):  A description for the option. Defaults to "". 
 - <b>`mapper`</b> (ValueMapper, optional):  A mapper function for casting the value. Defaults to None. 
 - <b>`choices`</b> (Iterable, optional):  A list of possible values. Defaults to None. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the name is missing. 
 - <b>`ValueError`</b>:  If the mapper is not a callable. 
 - <b>`ValueError`</b>:  If a list of choices is given but no value is set, or the value is not in the list. 



**Examples:**
 ```python
from toolbox.config import ConfigOption

name = ConfigOption("name", mapper=str, default="", description="The username")
age = ConfigOption("age", mapper=int, default=0)
group = ConfigOption("group", "user", mapper=str, choices=["user", "admin"])
date = ConfigOption("date")
``` 


---

#### <kbd>property</kbd> choices

The list of possible values for the option. 



**Returns:**
 
 - <b>`tuple`</b>:  The list of possible values for the option. 

---

#### <kbd>property</kbd> default

The default value for the option. 



**Returns:**
 
 - <b>`Any`</b>:  The default value for the option. 

---

#### <kbd>property</kbd> description

A description of the option. 



**Returns:**
 
 - <b>`str`</b>:  The description of the option. 

---

#### <kbd>property</kbd> mapper

The mapper applied to cast and format the value. 



**Returns:**
 
 - <b>`ValueMapper`</b>:  The mapper applied to cast and format the value. 

---

#### <kbd>property</kbd> name

The name of the option. 



**Returns:**
 
 - <b>`str`</b>:  The name of the option. 

---

#### <kbd>property</kbd> value

The current value of the option. 



**Returns:**
 
 - <b>`Any`</b>:  The current value of the option. 



---

<a href="../src/toolbox/config/config_option.py#L379"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `cast`

```python
cast(value: 'Any') → Any
```

Casts and format a value to what is expected by the config option. 



**Args:**
 
 - <b>`value`</b> (Any):  The value to cast and format. 



**Returns:**
 
 - <b>`Any`</b>:  The casted value. 

---

<a href="../src/toolbox/config/config_option.py#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `copy`

```python
copy() → ConfigOption
```

Gets a copy of the option. 



**Returns:**
 
 - <b>`ConfigOption`</b>:  A copy of the option. 



**Examples:**
 ```python
from toolbox.config import ConfigOption

name = ConfigOption("name", mapper=str, default="", description="The username")

name2 = name.copy()

print(name == name2) # True
print(name is name2) # False
``` 

---

<a href="../src/toolbox/config/config_option.py#L236"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get() → Any
```

Gets the value of the option. 

It returns the default value if the value is not defined yet. 



**Returns:**
 
 - <b>`Any`</b>:  The value of the option. It may be the default value. 



**Examples:**
 ```python
from toolbox.config import ConfigOption

name = ConfigOption("name", mapper=str, default="bob")

print(name.get()) # "bob"

name.set("John")

print(name.get()) # "John"
``` 

---

<a href="../src/toolbox/config/config_option.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_dict`

```python
get_dict() → dict
```

Gets the option as a dictionary. 



**Returns:**
 
 - <b>`dict`</b>:  A dictionary containing a representation of the option. 



**Examples:**
 ```python
from toolbox.config import ConfigOption

name = ConfigOption("foo", "bar")

print(name.get_dict()) # {"name": "foo", "value": "bar", "default": None, ...}
``` 

---

<a href="../src/toolbox/config/config_option.py#L303"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset`

```python
reset() → None
```

Resets the option to its default value. 



**Raises:**
 
 - <b>`ValueError`</b>:  If a list of choices is defined and the default value is not defined. 

---

<a href="../src/toolbox/config/config_option.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set`

```python
set(value: 'Any') → Any
```

Sets the value of the option. 



**Args:**
 
 - <b>`value`</b> (Any):  The value of the option. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the mapper cannot convert the value. 
 - <b>`ValueError`</b>:  If a list of choices is defined and the value is not defined. 
 - <b>`ValueError`</b>:  If a list of choices is defined and the value does not exist in the list. 



**Returns:**
 
 - <b>`Any`</b>:  The value of the option. 



**Examples:**
 ```python
from toolbox.config import ConfigOption

name = ConfigOption("name", mapper=str, default="bob")

name.set("John")

print(name.get()) # "John"

name.set(None)

print(name.get()) # "bob"
``` 

---

<a href="../src/toolbox/config/config_option.py#L317"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_default`

```python
set_default(default: 'Any') → Any
```

Sets the default value of the option. 



**Args:**
 
 - <b>`default`</b> (Any):  The default value of the option. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the mapper cannot convert the value. 
 - <b>`ValueError`</b>:  If a list of choices is defined and the value is not defined. 
 - <b>`ValueError`</b>:  If a list of choices is defined and the value does not exist in the list. 



**Returns:**
 
 - <b>`Any`</b>:  The default value of the option. 



**Examples:**
 ```python
from toolbox.config import ConfigOption

name = ConfigOption("name", mapper=str, default="bob")

print(name.get()) # "bob"

name.set_default("")

print(name.get()) # ""
``` 

---

<a href="../src/toolbox/config/config_option.py#L359"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_description`

```python
set_description(description: 'str') → None
```

Sets the description of the option. 



**Args:**
 
 - <b>`description`</b> (str):  A description for the option. 

```python
from toolbox.config import ConfigOption

name = ConfigOption("name")

print(name.description) # ""

name.set_description("This is an option")

print(name.description) # "This is an option"
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
