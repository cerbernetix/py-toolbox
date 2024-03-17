# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

-   `get_combinations(values, length, offset, columns)`: Computes combinations given a set of values and a length.

### Changed

-   Add options to JSONFile implementation (`sort_keys`, `skip_keys`, `ensure_ascii`, `separators`, `strict`).
-   Set the default CSV dialect to `'excel'` when writing (this reflects the default value from the Python library).
-   Set the default CSV dialect to `'auto'` when reading (the dialect will be sniffed from the first few rows).

### Fixed

-   Fix the link to the documentation in the readme.

## [0.9.1] - 2023-10-27

### Fixed

-   Correct the readme instructions for installing the package.

## [0.9.0] - 2023-10-26

### Changed

-   Move the package to the `cerbernetix` namespace.
-   Move the package to the `src` directory.
-   `FileManager.read_file(iterator)` - Accepts to return an iterator from `read_file()` instead of immediately the content.

### Added

-   `get_combination_rank(combination, offset)`: Gets the rank of a combination.
-   `get_combination_from_rank(rank, length, offset)`: Gets the combination corresponding to a particular rank.
-   `get_cache_path(name, create)` - Gets the path to a cache folder.
-   `ValueExtractor(entries, mapper)` - A tool for extracting values from a set of possible entries.
-   `decimal(separator, thousands)` - Creates a mapper for casting decimal values to floats.
-   `Weekday(day)` - Gets the date of a weekday given a particular date.
-   `FileManager.create_path()` - Creates the parent path of the file.
-   `FileManager.check(...)` - Tells if the file is valid with respect to the specified criteria.

## [0.8.1] - 2023-10-03

### Added

-   Script for running the unit tests and presenting the coverage.
-   Script for applying the linter.
-   Script for applying the formatting.

### Fixed

-   Correct the dependencies declaration.

## [0.8.0] - 2023-09-17

### Changed

-   Move the tests to a dedicated folder outside of the source code. This will avoid polluting the exports.

### Fixed

-   Better default value for the config option mapper (None instead of a default mapper function).

## [0.7.0] - 2023-09-14

### Changed

-   `read_pickle_file(...)` and `PickleFile.read_file()` - Can either return a list (default) or an iterator (when the iterator parameter is True).
-   `read_csv_file(...)` and `CSVFile.read_file()` - Can either return a list (default) or an iterator (when the iterator parameter is True).
-   `read_zip_csv(buffer, ...)` - Can either return a list (default) or an iterator (when the iterator parameter is True).

## [0.6.0] - 2023-09-14

### Added

-   `fetch_content(url, ...)` - Fetch content from a remote HTTP address.
-   `read_zip_file(buffer, ...)` - Reads a file content from a Zip archive.
-   `read_zip_csv(buffer, ...)` - Reads a CSV content from a Zip.

## [0.5.1] - 2023-09-13

### Changed

-   Increase coverage

### Fixed

-   Wrong use of `fieldnames=False` in `CSVFile.write()`.

## [0.5.0] - 2023-09-13

### Added

-   `Config` - A class for handling a configuration.
-   `ConfigOption` - A class for handling config options.
-   `create_options(options)` - Creates config options from a list of descriptors.
-   `passthrough(value)` - A passthrough mapper. It returns the value as it is.
-   `boolean(value)` - Converts a value to a boolean value.

## [0.4.0] - 2023-09-12

### Added

-   `TestCase` - Extends the default Python TestCase with more assertions.
-   `test_cases(cases)` - Decorates a test case with parameters.

## [0.3.0] - 2023-09-12

### Added

-   `LogFile` - Offers a similar API to the Python builtin loggers for logging to a custom file.
-   `setup_file_logging()` - Setup file logging for the application.
-   `handle_uncaught_exceptions()` - Installs a collector for logging uncaught exceptions.

### Changed

-   The documentation generator clears the `./docs` folder before generating the documentation.

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
    It was generating the error `TypeError: expected str, bytes or os.PathLike object, not list`

## [0.1.1] - 2023-09-05

### Changed

-   `get_application_path()`, `get_application_name()`, and `get_file_path()` now all require the name of the main package for getting the application's path.

### Fixed

-   Wrong detection of the application path, in `get_application_path()` (`__main__` has no attribute)
    The trick used was not working, the `__main__` module has no attribute.

## [0.1.0] - 2023-09-05

### Added

-   Helpers around file paths.
