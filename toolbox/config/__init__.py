"""The `config` package provides classes for handling a configuration.

It contains:
- `ConfigOption(name, value, ...)` - Manages a config option.
- `create_options(options)` - Creates options from a list of descriptors.

Examples:
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
print(name.get()) # print => "John"
print(age.get())  # print => 20
```
"""
from toolbox.config.config_option import ConfigOption, create_options
