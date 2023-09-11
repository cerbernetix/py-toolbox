# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2023-09-11

### Added

-   `FileManager(filename, ...)` - Manages read and write for generic files.
-   `CSVFile(filename, ...)` - Manages read and write for CSV files.
-   `JSONFile(filename, ...)` - Manages read and write for JSON files.
-   `PickleFile(filename, ...)` - Manages read and write for pickle files.
-   `get_file_mode()` - Gets the file mode given the desired access type.
-   `read_file(filename, ...)` - Reads all the content from a file at once.
-   `write_file(filename, data, ...)` - Writes content to a file at once.
-   `read_csv_file(filename, ...)` - Reads all the content from a CSV file at once.
-   `write_csv_file(filename, data, ...)` - Writes content to a CSV file at once.
-   `read_json_file(filename, ...)` - Reads all the content from a JSON file at once.
-   `write_json_file(filename, data, ...)` - Writes content to a JSON file at once.
-   `read_pickle_file(filename, ...)` - Reads all the content from a pickle file at once.
-   `write_pickle_file(filename, data, ...)` - Writes content to a pickle file at once.
-   Reference documentation, in the `./docs` folder.
-   Documentation generator.

### Changed

-   `create_file_path`: It now returns true if the path already exists.

## [0.1.2] - 2023-09-05

### Fixed

-   Wrong use of the module path

## [0.1.1] - 2023-09-05

### Changed

-   `get_application_path()`, `get_application_name()`, and `get_file_path()` now all require the name of the main package for getting the application's path.

### Fixed

-   Wrong detection of the application path (`__main__` has no attribute)"

## [0.1.0] - 2023-09-05

### Added

-   Helpers around file paths.
