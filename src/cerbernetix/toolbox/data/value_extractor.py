"""A tool for extracting values from a set of possible entries.

Examples:
```python
from cerbernetix.toolbox.data import ValueExtractor

# Extracts a date from various possible entries
extractor = ValueExtractor(["date", "time", "day"])
data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]

# Build full names from multiple entries
extractor = ValueExtractor(["firstname", "lastname"], " ".join)
data = [
    {"firstname": "John", "lastname": "Smith"},
    {"firstname": "Jane", "lastname": "Doe"},
]
print([extractor.aggregate(row) for row in data]) # ["John Smith", "Jane Doe"]
```
"""
from typing import Any, Iterable

from cerbernetix.toolbox.data.mappers import ValueMapper, passthrough


class ValueExtractor:
    """Extracts a value from a set of possible entries.

    Attributes:
        entries (tuple[str], readonly): The list of possible entries to look at from
        the structure on which the extractor will be applied.
        mapper (ValueMapper, readonly): A mapper for casting the extracted value.

    Examples:
    ```python
    from cerbernetix.toolbox.data import ValueExtractor

    extractor = ValueExtractor(["date", "time", "day"])
    data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
    print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]
    ```
    """

    def __init__(
        self,
        entries: Iterable[str] | str,
        mapper: ValueMapper = None,
    ) -> None:
        """Creates a value extractor.

        Args:
            entries (Iterable[str] | str): The list of possible entries to look at from
            the structure on which the extractor will be applied.
            mapper (ValueMapper, optional): A mapper for casting the extracted value.
            Defaults to None.

        Raises:
            ValueError: If an invalid mapper is given.

        Examples:
        ```python
        from cerbernetix.toolbox.data import ValueExtractor

        extractor = ValueExtractor(["date", "time", "day"])
        data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
        print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]
        ```
        """
        if mapper is None:
            mapper = passthrough

        if not callable(mapper):
            raise ValueError("A valid mapper is needed for casting the extracted value.")

        self._entries = (entries,) if isinstance(entries, str) else tuple(entries)
        self._mapper = mapper

    @property
    def entries(self) -> tuple[str]:
        """The list of possible entries to look at from the structure on which apply the extractor.

        Returns:
            tuple[str]: The list of possible entries to look at from the structure
            on which the extractor will be applied.
        """
        return self._entries

    @property
    def mapper(self) -> ValueMapper:
        """The mapper applied to cast and format the extracted value.

        Returns:
            ValueMapper: The mapper applied to cast and format the extracted value.
        """
        return self._mapper

    def extract(self, structure: dict) -> Any:
        """Extracts the value from the specified structure.

        It checks successively each entry configured till one exists in the structure,
        and it returns the first that match. If none of the entries exists in the structure,
        it returns None.

        Args:
            structure (dict): The structure from which extract the value.

        Returns:
            Any: The value extracted from the structure. It returns None if no entry is found.

        Examples:
        ```python
        from cerbernetix.toolbox.data import ValueExtractor

        # Extracts a date from various possible entries
        extractor = ValueExtractor(["date", "time", "day"])
        data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
        print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]

        # Extracts a number from various possible entries, casting it to an integer
        extractor = ValueExtractor(["value", "val", "number"], int)
        data = [{"val": "42"}, {"value": 12, {"number": 100}]
        print([extractor.extract(row) for row in data]) # [42, 12, 100]
        ```
        """
        for name in self._entries:
            if name in structure:
                return self._mapper(structure[name])

        return None

    def aggregate(self, structure: dict) -> Any:
        """Aggregates a value from the specified structure.

        Args:
            structure (dict): The structure from which aggregate the value.

        Returns:
            Any: The value aggregated from the structure.

        Examples:
        ```python
        from cerbernetix.toolbox.data import ValueExtractor

        # Build full names from multiple entries
        extractor = ValueExtractor(["firstname", "lastname"], " ".join)
        data = [
            {"firstname": "John", "lastname": "Smith"},
            {"firstname": "Jane", "lastname": "Doe"},
        ]
        print([extractor.aggregate(row) for row in data]) # ["John Smith", "Jane Doe"]

        # Build a list from multiple entries
        extractor = ValueExtractor(["value_1", "value_2", "value_3"])
        data = [
            {"value_1": 42, "value_2": 12, "value_3": 100},
            {"value_1": 10, "value_2": 20, "value_3": 30},
        ]
        print([extractor.aggregate(row) for row in data]) # [[42, 12, 100], [10, 20, 30]]
        ```
        """
        return self._mapper([structure[name] for name in self._entries if name in structure])
