"""A class for handling config options.

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
print(name.get()) # "John"
print(age.get())  # 20
```
"""
from __future__ import annotations

from typing import Any, Iterable, Iterator

from toolbox.data import ValueMapper, passthrough


class ConfigOption:
    """Handles a config option.

    Each config option must be named. They can have a default value that will be returned while the
    value is not set.

    A mapper is responsible for casting the value to the correct type and format.

    Options can have a description, and can be constrained to a list of possible values.

    Attributes:
        name (str, readonly): The name of the option.
        value (Any, readonly): The current value of the option.
        default (Any, readonly): The default value for the option.
        description (str, readonly): A description of the option.
        mapper (ValueMapper, readonly): The mapper applied to cast and format the value.
        choices (tuple, readonly): The list of possible values for the option.


    Examples:
    ```python
    from toolbox.config import ConfigOption

    name = ConfigOption("name", mapper=str, default="bob")

    print(name.get()) # "bob"

    name.set("John")

    print(name.get()) # "John"
    ```
    """

    def __init__(
        self,
        name: str,
        value: Any = None,
        default: Any = None,
        description: str = "",
        mapper: ValueMapper = None,
        choices: Iterable = None,
    ) -> None:
        """Creates a named configuration option.

        The name is mandatory.

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
            Defaults to None.

        Raises:
            ValueError: If the name is missing.
            ValueError: If the mapper is not a callable.
            ValueError: If a list of choices is given but no value is set,
            or the value is not in the list.

        Examples:
        ```python
        from toolbox.config import ConfigOption

        name = ConfigOption("name", mapper=str, default="", description="The username")
        age = ConfigOption("age", mapper=int, default=0)
        group = ConfigOption("group", "user", mapper=str, choices=["user", "admin"])
        date = ConfigOption("date")
        ```
        """
        if not name:
            raise ValueError("The name is mandatory for a config option.")

        if mapper is None:
            mapper = passthrough

        if not callable(mapper):
            raise ValueError("A valid mapper is needed for casting the option's value.")

        self._name = str(name)
        self._description = str(description or "")
        self._mapper = mapper
        self._value = self.cast(value)
        self._default = self.cast(default)
        self._choices = tuple(choices) if choices else ()

        if (
            self._choices
            and (self._value is None or self._value not in self._choices)
            and (self._default is None or self._default not in self._choices)
        ):
            raise ValueError(
                "A valid value is required when constraining to a list of choices."
                + " At least a valid default value is expected."
            )

    @property
    def name(self) -> str:
        """The name of the option.

        Returns:
            str: The name of the option.
        """
        return self._name

    @property
    def value(self) -> Any:
        """The current value of the option.

        Returns:
            Any: The current value of the option.
        """
        return self._value

    @property
    def default(self) -> Any:
        """The default value for the option.

        Returns:
            Any: The default value for the option.
        """
        return self._default

    @property
    def description(self) -> str:
        """A description of the option.

        Returns:
            str: The description of the option.
        """
        return self._description

    @property
    def mapper(self) -> ValueMapper:
        """The mapper applied to cast and format the value.

        Returns:
            ValueMapper: The mapper applied to cast and format the value.
        """
        return self._mapper

    @property
    def choices(self) -> tuple:
        """The list of possible values for the option.

        Returns:
            tuple: The list of possible values for the option.
        """
        return self._choices

    def copy(self) -> ConfigOption:
        """Gets a copy of the option.

        Returns:
            ConfigOption: A copy of the option.

        Examples:
        ```python
        from toolbox.config import ConfigOption

        name = ConfigOption("name", mapper=str, default="", description="The username")

        name2 = name.copy()

        print(name == name2) # True
        print(name is name2) # False
        ```
        """
        return ConfigOption(
            name=self._name,
            value=self._value,
            default=self._default,
            description=self._description,
            mapper=self._mapper,
            choices=self._choices,
        )

    def get_dict(self) -> dict:
        """Gets the option as a dictionary.

        Returns:
            dict: A dictionary containing a representation of the option.

        Examples:
        ```python
        from toolbox.config import ConfigOption

        name = ConfigOption("foo", "bar")

        print(name.get_dict()) # {"name": "foo", "value": "bar", "default": None, ...}
        ```
        """
        return {
            "name": self.name,
            "value": self.value,
            "default": self.default,
            "description": self.description,
            "mapper": self.mapper,
            "choices": self.choices,
        }

    def get(self) -> Any:
        """Gets the value of the option.

        It returns the default value if the value is not defined yet.

        Returns:
            Any: The value of the option. It may be the default value.

        Examples:
        ```python
        from toolbox.config import ConfigOption

        name = ConfigOption("name", mapper=str, default="bob")

        print(name.get()) # "bob"

        name.set("John")

        print(name.get()) # "John"
        ```
        """
        return self._value if self._value is not None else self._default

    def set(self, value: Any) -> Any:
        """Sets the value of the option.

        Args:
            value (Any): The value of the option.

        Raises:
            ValueError: If the mapper cannot convert the value.
            ValueError: If a list of choices is defined and the value is not defined.
            ValueError: If a list of choices is defined and the value does not exist in the list.

        Returns:
            Any: The value of the option.

        Examples:
        ```python
        from toolbox.config import ConfigOption

        name = ConfigOption("name", mapper=str, default="bob")

        name.set("John")

        print(name.get()) # "John"

        name.set(None)

        print(name.get()) # "bob"
        ```
        """
        value = self.cast(value)

        if self._choices and value is None and self._default is None:
            raise ValueError(
                "A valid value is required when constraining to a list of choices."
                + " At least a valid default value is expected."
            )

        if self._choices and value is not None and value not in self._choices:
            raise ValueError(f"The value '{value}' is not in the list of choices.")

        self._value = value

        return self.value

    def reset(self) -> None:
        """Resets the option to its default value.

        Raises:
            ValueError: If a list of choices is defined and the default value is not defined.
        """
        if self._choices and self._default is None:
            raise ValueError(f"The option '{self._name}' does not have a default value.")

        if self._choices:
            self._value = self._default
        else:
            self._value = None

    def set_default(self, default: Any) -> Any:
        """Sets the default value of the option.

        Args:
            default (Any): The default value of the option.

        Raises:
            ValueError: If the mapper cannot convert the value.
            ValueError: If a list of choices is defined and the value is not defined.
            ValueError: If a list of choices is defined and the value does not exist in the list.

        Returns:
            Any: The default value of the option.

        Examples:
        ```python
        from toolbox.config import ConfigOption

        name = ConfigOption("name", mapper=str, default="bob")

        print(name.get()) # "bob"

        name.set_default("")

        print(name.get()) # ""
        ```
        """
        default = self.cast(default)

        if self._choices and default is None and self._value is None:
            raise ValueError(
                "A valid value is required when constraining to a list of choices."
                + " At least a valid default value is expected."
            )

        if self._choices and default is not None and default not in self._choices:
            raise ValueError(f"The value '{default}' is not in the list of choices.")

        self._default = default

        return self.default

    def set_description(self, description: str) -> None:
        """Sets the description of the option.

        Args:
            description (str): A description for the option.

        ```python
        from toolbox.config import ConfigOption

        name = ConfigOption("name")

        print(name.description) # ""

        name.set_description("This is an option")

        print(name.description) # "This is an option"
        ```
        """
        self._description = str(description or "")

    def cast(self, value: Any) -> Any:
        """Casts and format a value to what is expected by the config option.

        Args:
            value (Any): The value to cast and format.

        Returns:
            Any: The casted value.
        """
        if value is not None:
            return self._mapper(value)

        return None

    def __str__(self) -> str:
        """Converts the option to a string.

        The option is represented by the string "name=value".

        Returns:
            str: The string representation of the option.
        """
        return f"{self._name}={self._value}"

    def __eq__(self, other: object) -> bool:
        """Tells if the option is equal to another.

        Args:
            other (object): The other option to compare.

        Returns:
            bool: True if both options have the same name and the same value, False otherwise.
        """
        if not isinstance(other, self.__class__):
            return False

        return self._name == other._name and self._value == other._value


def create_options(options: Iterable) -> Iterator[ConfigOption]:
    """Create options from a list of descriptors.

    Depending on the type of the descriptor, the following will be done:
    - If it is a config option, a copy is yielded.
    - If it is a dictionary, a config option is created from the named parameters.
    - If it is a list or a tuple, a config option is created from the positioned parameters.
    - For any other types, a config option is created from the single parameter.

    Args:
        options (Iterable): A list of config option descriptor to create options from.

    Yields:
        Iterator[ConfigOption]: A config option created from the descriptor.

    Examples:
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
    """
    for option in options:
        if isinstance(option, ConfigOption):
            yield option.copy()
        elif isinstance(option, dict):
            yield ConfigOption(**option)
        elif isinstance(option, (list, tuple)):
            yield ConfigOption(*option)
        else:
            yield ConfigOption(option)
