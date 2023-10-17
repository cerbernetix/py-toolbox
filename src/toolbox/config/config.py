"""A class for handling a configuration.

Examples:
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
"""
from typing import Any, Callable, Iterator

from toolbox.config.config_option import ConfigOption, create_options


class Config:
    """Handles a configuration.

    A configuration is a set of named options that can have a value and a default value.
    A configuration option can also have a description, a mapper function for casting and
    formatting the value, and can also be constrained to a list of possible choices.

    Attributes:
        Each config option can be access as an attribute.

    Examples:
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
    """

    def __init__(
        self,
        config: dict = None,
        options: list[ConfigOption] = None,
    ) -> None:
        """Creates a configuration handler.

        A configuration is a set of named options that can have a value and a default value.
        A configuration option can also have a description, a mapper function for casting and
        formatting the value, and can also be constrained to a list of possible choices.

        Args:
            config (dict, optional): The initial configuration. Defaults to None.
            options (list[ConfigOption], optional): The list of available options. Defaults to None.

        Examples:
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
        """
        if options:
            self._options = {option.name: option for option in create_options(options)}
        else:
            self._options = {}

        if config:
            self.set_config(config)

    def keys(self) -> list:
        """Returns the name of each option in a view object.

        The view object changes according to the changes in the list of options.

        Returns:
            list: The list of option names.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config()
        keys = config.keys()

        print(list(keys)) # []

        config["foo"] = bar

        print(list(keys)) # ["foo"]
        ```
        """
        return self._options.keys()

    def has(self, name: str) -> bool:
        """Tells if a configuration option exists.

        Args:
            name (str): The name of the configuration option.

        Returns:
            bool: `True` if the configuration option exists, `False` otherwise.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.has("foo") # True
        config.has("bar") # False
        ```
        """
        return name in self._options

    def get(self, name: str, default: Any = None) -> Any:
        """Gets the value of a configuration option.

        If the corresponding option does not exist, None will be returned.

        A default value in case the option does not exist can be supplied.

        Args:
            name (str): The name of the configuration option.
            default (Any, optional): The value returned if the option does not exist.
            Defaults to None.

        Returns:
            Any: The value of the configuration option, or the default value or None.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.get("foo") # "bar"
        config.get("bar") # None
        config.get("bar", "foo") # "foo"
        ```
        """
        if name in self._options:
            return self._options[name].get()

        return default

    def set(self, name: str, value: Any) -> Any:
        """Sets the value of a configuration option.

        If the corresponding option exists, its value will be updated.
        Otherwise, a new option is created from the given name and value.

        Args:
            name (str): The name of the configuration option to set.
            value (Any): The value to set to the configuration option.

        Raises:
            ValueError: If the value mapper bound to the option cannot convert the value.
            ValueError: If a list of choices is defined and the value is not defined.
            ValueError: If a list of choices is defined and the value does not exist in the list.

        Returns:
            Any: The new value of the option.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.set("foo", "foo") # Set "foo" to the option "foo"
        config.set("bar", "bar") # Create the option "bar" with the value "bar"
        ```
        """
        if name in self._options:
            self._options[name].set(value)
        else:
            self.set_option(name, value)

        return self._options[name].get()

    def reset(self, name: str) -> None:
        """Resets a configuration option to its default value.

        If the corresponding option exists, its value will be updated.
        Otherwise, a new option is created from the given name and its value set to None.

        Args:
            name (str): The name of the configuration option.

        Raises:
            ValueError: If a list of choices is defined and the default value is not defined.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.reset("foo") # Set None to the option "foo"
        config.reset("bar") # Create the option "bar" with the value None
        ```
        """
        if name in self._options:
            self._options[name].reset()
        else:
            self.set_option(name)

    def drop(self, name: str) -> bool:
        """Removes a configuration option.

        Args:
            name (str): The name of the option.

        Returns:
            bool: `True` if the configuration option was removed, `False` otherwise.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.drop("foo") # True
        config.drop("bar") # False
        ```
        """
        if name in self._options:
            self._options.pop(name)
            return True

        return False

    def describe(self, name: str) -> str:
        """Gets the description of a configuration option.

        Args:
            name (str): The name of the configuration option.

        Returns:
            str: The description of the configuration option, if it exists. Returns "" otherwise.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config(options=[ConfigOption("foo", "bar", description="FooBar")])

        config.describe("foo") # "FooBar"
        config.describe("bar") # ""
        ```
        """
        if name in self._options:
            return self._options[name].description

        return ""

    def choices(self, name: str) -> tuple:
        """Gets the possible values of a configuration option.

        Args:
            name (str): The name of the configuration option.

        Returns:
            tuple: The list of possible values for the configuration option.
            Returns () if there is no list, or if the option does not exist.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config(options=[ConfigOption("foo", "bar", choices=["foo", "bar"])])

        config.choices("foo") # ("foo", "bar")
        config.choices("bar") # ()
        ```
        """
        if name in self._options:
            return self._options[name].choices

        return ()

    def get_option(self, name: str) -> ConfigOption:
        """Gets a config option.

        Args:
            name (str): The name of the option.

        Returns:
            ConfigOption: The config option, or None if the option does not exist.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config(options=[ConfigOption("foo", "bar")])

        config.get_option("foo") # ConfigOption("foo", "bar")
        config.get_option("bar") # None
        ```
        """
        return self._options.get(name)

    def set_option(
        self,
        name: str,
        value: Any = None,
        default: Any = None,
        description: str = None,
        mapper: Callable = None,
        choices: list = None,
    ) -> None:
        """Adds a configuration option.

        Args:
            name (str): The name of the option.
            value (Any, optional): The initial value of the option.
            Defaults to None.
            default (Any, optional): The value returned when there is no defined value.
            Defaults to None.
            description (str, optional): A description for the option.
            Defaults to "".
            mapper (ValueMapper, optional): A mapper function for casting the value.
            Defaults to None.
            choices (Iterable, optional): A list of possible values.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config()

        config.set_option("foo", "bar")
        config.set_option("bar", default="foo")
        config.set_option("number", mapper=int)
        ```
        """
        self._options[name] = ConfigOption(
            name=name,
            value=value,
            default=default,
            description=description,
            mapper=mapper,
            choices=choices,
        )

    def get_options(self) -> list[dict]:
        """Exports the list of options as a list of dictionaries.

        Each option is exported entirely to a dictionary using `option.get_dict()`.

        Returns:
            list[dict]: A list of all options defined by dictionaries.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.get_options() # [{"name": "foo", "value": "bar", "default": None, ...}]
        ```
        """
        return [option.get_dict() for option in self._options.values()]

    def get_config(self) -> dict:
        """Exports the configuration options into a dictionary.

        Each key will be the name of an option, and the value will be the actual value of the
        option, or the default value if the value is not set.

        Returns:
            dict: The configuration options.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.get_config() # {"foo": "bar"}
        ```
        """
        return {name: option.get() for name, option in self._options.items()}

    def set_config(self, config: dict) -> None:
        """Imports the configuration options from a dictionary.

        Each key must be the name of an option and the value the value of the option.

        If an option does not exist in the configuration, it will be created with default
        properties.

        Args:
            config (dict): The configuration options.

        Raises:
            ValueError: If the value mapper bound to the option cannot convert the value.
            ValueError: If a list of choices is defined and the value is not defined.
            ValueError: If a list of choices is defined and the value does not exist in the list.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config()

        config.set_config({"foo": "bar"})
        ```
        """
        for name, value in config.items():
            self.set(name, value)

    def reset_config(self) -> None:
        """Resets all configuration options to their default value.

        Raises:
            ValueError: If a list of choices is defined and the default value is not defined.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.reset()

        config.get_config() # {"foo": None}
        ```
        """
        for option in self._options.values():
            option.reset()

    def __getattr__(self, name: str) -> Any:
        """Gets the value of a configuration option.

        If the corresponding option does not exist, an AttributeError is raised.

        Args:
            name (str): The name of the configuration option.

        Raises:
            AttributeError: If the option does not exists.

        Returns:
            Any: The value of the configuration option.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config.foo # "bar"
        config.bar # AttributeError!
        ```
        """
        if name in self._options:
            return self._options[name].get()

        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __getitem__(self, name: str) -> Any:
        """Gets the value of a configuration option.

        If the corresponding option does not exist, an IndexError is raised.

        Args:
            name (str): The name of the configuration option.

        Raises:
            IndexError: If the option does not exists.

        Returns:
            Any: The value of the configuration option.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config["foo"] # "bar"
        config["bar"] # IndexError!
        ```
        """
        if name in self._options:
            return self._options[name].get()

        raise IndexError(f"the option {name} does not exist")

    def __setitem__(self, name: str, value: Any) -> None:
        """Sets the value of a configuration option.

        If the corresponding option exists, its value will be updated.
        Otherwise, a new option is created from the given name and value.

        Args:
            name (str): The name of the configuration option to set.
            value (Any): The value to set to the configuration option.

        Raises:
            ValueError: If the value mapper bound to the option cannot convert the value.
            ValueError: If a list of choices is defined and the value is not defined.
            ValueError: If a list of choices is defined and the value does not exist in the list.

        Returns:
            Any: The new value of the option.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        config["foo"] = "foo" # Set "foo" to the option "foo"
        config["bar"] = "bar" # Create the option "bar" with the value "bar"
        ```
        """
        self.set(name, value)

    def __delitem__(self, name: str) -> None:
        """Removes a configuration option.

        If the corresponding option does not exist, an IndexError is raised.

        Args:
            name (str): The name of the option.

        Raises:
            IndexError: If the option does not exists.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        del config["foo"] # OK
        del config["bar"] # IndexError!
        ```
        """
        if not self.drop(name):
            raise IndexError(f"the option {name} does not exist")

    def __len__(self) -> int:
        """Returns the number of options defined in the configuration.

        Returns:
            int: The number of configuration options.
        """
        return len(self._options)

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Allows to loop over config options.

        Yields:
            Iterator[tuple[str, Any]]: The name and value of an option

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar", "value": 42})

        for name, value in config:
            print(f"{name}={value}")
        ```
        """
        for name, option in self._options.items():
            yield name, option.get()

    def __contains__(self, name: str) -> bool:
        """Tells if a configuration option exists.

        Args:
            name (str): The name of the configuration option.

        Returns:
            bool: `True` if the configuration option exists, `False` otherwise.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar"})

        "foo" in config # True
        "bar" in config # False
        ```
        """
        return name in self._options

    def __str__(self) -> str:
        """Converts the configuration to a string.

        Each option is represented by the string "name=value".
        Each option is place on a separate line

        Returns:
            str: The string representation of the option.

        Examples:
        ```python
        from toolbox.config import Config

        config = Config({"foo": "bar", "value": 42})

        print(config)
        '''foo=bar
        value=42'''
        ```
        """
        return "\n".join([str(option) for option in self._options.values()])
