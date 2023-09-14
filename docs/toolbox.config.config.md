<!-- markdownlint-disable -->

<a href="../toolbox/config/config.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.config.config`
A class for handling a configuration. 



**Examples:**
 ```python
from toolbox.config import Config

# Create an empty configuration
config = Config()

# Set some values
config["foo"] = bar
config.set("date") = "2023-11-12"

# Read some values
config["foo"]
config.get("foo")
config.foo

# Create a configuration, defining the options
config = Config(options=[
     # A config option can be created using the ConfigOption class
     ConfigOption("foo"),

     # A config option can also be created using a dictionary
     {"name": "value", "value": 42},
])

# Create a configuration, defining the values
config = Config({"foo": "bar", "value": 42})
``` 



---

<a href="../toolbox/config/config.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Config`
Handles a configuration. 

A configuration is a set of named options that can have a value and a default value. A configuration option can also have a description, a mapper function for casting and formatting the value, and can also be constrained to a list of possible choices. 



**Attributes:**
  Each config option can be access as an attribute. 



**Examples:**
 ```python
from toolbox.config import Config

# Create an empty configuration
config = Config()

# Set some values
config["foo"] = bar
config.set("date") = "2023-11-12"

# Options can be read using the array notation
config["foo"] # "bar"

# Options can be read using the method notation
config.get("foo") # "bar"

# Options can be read using the property notation
config.foo # "bar"

# Options can be defined later
config.set_option("foo", default="bar", description="FooBar")
config["foo"] # "bar"

# Create a configuration, defining the options
config = Config(options=[
     # A config option can be created using the ConfigOption class
     ConfigOption("foo"),

     # A config option can also be created using a dictionary
     {"name": "value", "value": 42},
])
config["foo"] # None as no value was set
config["value"] # 42

# Create a configuration, defining the values
config = Config({"foo": "bar", "value": 42})
config["foo"] # "bar"
config["value"] # 42

# Export the configuration to a dictionary
data = config.get_config()

# Import the configuration from a dictionary
config.set_config(data)
``` 

<a href="../toolbox/config/config.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(config: dict = None, options: list[ConfigOption] = None) → None
```

Creates a configuration handler. 

A configuration is a set of named options that can have a value and a default value. A configuration option can also have a description, a mapper function for casting and formatting the value, and can also be constrained to a list of possible choices. 



**Args:**
 
 - <b>`config`</b> (dict, optional):  The initial configuration. Defaults to None. 
 - <b>`options`</b> (list[ConfigOption], optional):  The list of available options. Defaults to None. 



**Examples:**
 ```python
from toolbox.config import Config

# Create an empty configuration
config = Config()

# Create a configuration from a list of values
config = Config({"foo": "bar"})

# Create a configuration using a schema
config = Config(options=[ConfigOption("foo", "bar"), ConfigOption("value", default=42)])

# Create a configuration using a schema and having initial values
config = Config({"foo": "bar"},
                 options=[ConfigOption("foo"), ConfigOption("value", default=42)])
``` 




---

<a href="../toolbox/config/config.py#L324"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `choices`

```python
choices(name: str) → tuple
```

Gets the possible values of a configuration option. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the configuration option. 



**Returns:**
 
 - <b>`tuple`</b>:  The list of possible values for the configuration option. Returns () if there is no list, or if the option does not exist. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config(options=[ConfigOption("foo", "bar", choices=["foo", "bar"])])

config.choices("foo") # ("foo", "bar")
config.choices("bar") # ()
``` 

---

<a href="../toolbox/config/config.py#L300"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `describe`

```python
describe(name: str) → str
```

Gets the description of a configuration option. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the configuration option. 



**Returns:**
 
 - <b>`str`</b>:  The description of the configuration option, if it exists. Returns "" otherwise. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config(options=[ConfigOption("foo", "bar", description="FooBar")])

config.describe("foo") # "FooBar"
config.describe("bar") # ""
``` 

---

<a href="../toolbox/config/config.py#L275"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `drop`

```python
drop(name: str) → bool
```

Removes a configuration option. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the option. 



**Returns:**
 
 - <b>`bool`</b>:  `True` if the configuration option was removed, `False` otherwise. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config({"foo": "bar"})

config.drop("foo") # True
config.drop("bar") # False
``` 

---

<a href="../toolbox/config/config.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(name: str, default: Any = None) → Any
```

Gets the value of a configuration option. 

If the corresponding option does not exist, None will be returned. 

A default value in case the option does not exist can be supplied. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the configuration option. 
 - <b>`default`</b> (Any, optional):  The value returned if the option does not exist. Defaults to None. 



**Returns:**
 
 - <b>`Any`</b>:  The value of the configuration option, or the default value or None. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config({"foo": "bar"})

config.get("foo") # "bar"
config.get("bar") # None
config.get("bar", "foo") # "foo"
``` 

---

<a href="../toolbox/config/config.py#L432"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_config`

```python
get_config() → dict
```

Exports the configuration options into a dictionary. 

Each key will be the name of an option, and the value will be the actual value of the option, or the default value if the value is not set. 



**Returns:**
 
 - <b>`dict`</b>:  The configuration options. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config({"foo": "bar"})

config.get_config() # {"foo": "bar"}
``` 

---

<a href="../toolbox/config/config.py#L349"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_option`

```python
get_option(name: str) → ConfigOption
```

Gets a config option. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the option. 



**Returns:**
 
 - <b>`ConfigOption`</b>:  The config option, or None if the option does not exist. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config(options=[ConfigOption("foo", "bar")])

config.get_option("foo") # ConfigOption("foo", "bar")
config.get_option("bar") # None
``` 

---

<a href="../toolbox/config/config.py#L413"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_options`

```python
get_options() → list[dict]
```

Exports the list of options as a list of dictionaries. 

Each option is exported entirely to a dictionary using `option.get_dict()`. 



**Returns:**
 
 - <b>`list[dict]`</b>:  A list of all options defined by dictionaries. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config({"foo": "bar"})

config.get_options() # [{"name": "foo", "value": "bar", "default": None, ...}]
``` 

---

<a href="../toolbox/config/config.py#L161"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `has`

```python
has(name: str) → bool
```

Tells if a configuration option exists. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the configuration option. 



**Returns:**
 
 - <b>`bool`</b>:  `True` if the configuration option exists, `False` otherwise. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config({"foo": "bar"})

config.has("foo") # True
config.has("bar") # False
``` 

---

<a href="../toolbox/config/config.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys`

```python
keys() → list
```

Returns the name of each option in a view object. 

The view object changes according to the changes in the list of options. 



**Returns:**
 
 - <b>`list`</b>:  The list of option names. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config()
keys = config.keys()

print(list(keys)) # []

config["foo"] = bar

print(list(keys)) # ["foo"]
``` 

---

<a href="../toolbox/config/config.py#L248"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset`

```python
reset(name: str) → None
```

Resets a configuration option to its default value. 

If the corresponding option exists, its value will be updated. Otherwise, a new option is created from the given name and its value set to None. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the configuration option. 



**Raises:**
 
 - <b>`ValueError`</b>:  If a list of choices is defined and the default value is not defined. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config({"foo": "bar"})

config.reset("foo") # Set None to the option "foo"
config.reset("bar") # Create the option "bar" with the value None
``` 

---

<a href="../toolbox/config/config.py#L480"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset_config`

```python
reset_config() → None
```

Resets all configuration options to their default value. 



**Raises:**
 
 - <b>`ValueError`</b>:  If a list of choices is defined and the default value is not defined. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config({"foo": "bar"})

config.reset()

config.get_config() # {"foo": None}
``` 

---

<a href="../toolbox/config/config.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set`

```python
set(name: str, value: Any) → Any
```

Sets the value of a configuration option. 

If the corresponding option exists, its value will be updated. Otherwise, a new option is created from the given name and value. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the configuration option to set. 
 - <b>`value`</b> (Any):  The value to set to the configuration option. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the value mapper bound to the option cannot convert the value. 
 - <b>`ValueError`</b>:  If a list of choices is defined and the value is not defined. 
 - <b>`ValueError`</b>:  If a list of choices is defined and the value does not exist in the list. 



**Returns:**
 
 - <b>`Any`</b>:  The new value of the option. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config({"foo": "bar"})

config.set("foo", "foo") # Set "foo" to the option "foo"
config.set("bar", "bar") # Create the option "bar" with the value "bar"
``` 

---

<a href="../toolbox/config/config.py#L452"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_config`

```python
set_config(config: dict) → None
```

Imports the configuration options from a dictionary. 

Each key must be the name of an option and the value the value of the option. 

If an option does not exist in the configuration, it will be created with default properties. 



**Args:**
 
 - <b>`config`</b> (dict):  The configuration options. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the value mapper bound to the option cannot convert the value. 
 - <b>`ValueError`</b>:  If a list of choices is defined and the value is not defined. 
 - <b>`ValueError`</b>:  If a list of choices is defined and the value does not exist in the list. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config()

config.set_config({"foo": "bar"})
``` 

---

<a href="../toolbox/config/config.py#L370"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_option`

```python
set_option(
    name: str,
    value: Any = None,
    default: Any = None,
    description: str = None,
    mapper: Callable = <function passthrough at 0x101b45580>,
    choices: list = None
) → None
```

Adds a configuration option. 



**Args:**
 
 - <b>`name`</b> (str):  The name of the option. 
 - <b>`value`</b> (Any, optional):  The initial value of the option. Defaults to None. 
 - <b>`default`</b> (Any, optional):  The value returned when there is no defined value. Defaults to None. 
 - <b>`description`</b> (str, optional):  A description for the option. Defaults to "". 
 - <b>`mapper`</b> (ConfigOptionMapper, optional):  A mapper function for casting the value. Defaults to passthrough. 
 - <b>`choices`</b> (Iterable, optional):  A list of possible values. 



**Examples:**
 ```python
from toolbox.config import Config

config = Config()

config.set_option("foo", "bar")
config.set_option("bar", default="foo")
config.set_option("number", mapper=int)
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
