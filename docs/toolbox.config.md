<!-- markdownlint-disable -->

<a href="../toolbox/config/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.config`
The `config` package provides classes for handling a configuration. 

It contains: 
- `Config(...)` - Manages a configuration. 
- `ConfigOption(name, value, ...)` - Manages a config option. 
- `create_options(options)` - Creates options from a list of descriptors. 



**Examples:**
 ```python
from toolbox.config import Config, ConfigOption

# Create a few options
name = ConfigOption("name", mapper=str, default="")
age = ConfigOption("age", mapper=int, default=0)

# Show some information
print(name, age)

# Set option values
name.set("John")
age.set("20")

# Get the values
print(name.get()) # print => "John"
print(age.get())  # print => 20

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
     name,
     age,

     # A config option can also be created using a dictionary
     {"name": "value", "value": 42},
])

# Create a configuration, only listing the options
config = Config(options=["name", "date", "value"])

# Create a configuration, defining the values
config = Config({"foo": "bar", "value": 42})
``` 

**Global Variables**
---------------
- **config_option**
- **config**




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
