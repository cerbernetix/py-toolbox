<!-- markdownlint-disable -->

# API Overview

## Modules

- [`toolbox`](./toolbox.md#module-toolbox): `py-toolbox` is a collection of utilities offering solutions to a set of common problems.
- [`toolbox.config`](./toolbox.config.md#module-toolboxconfig): The `config` package provides classes for handling a configuration.
- [`toolbox.config.config`](./toolbox.config.config.md#module-toolboxconfigconfig): A class for handling a configuration.
- [`toolbox.config.config_option`](./toolbox.config.config_option.md#module-toolboxconfigconfig_option): A class for handling config options.
- [`toolbox.data`](./toolbox.data.md#module-toolboxdata): A collection of data utilities.
- [`toolbox.data.mappers`](./toolbox.data.mappers.md#module-toolboxdatamappers): A collection of data mappers.
- [`toolbox.data.value_extractor`](./toolbox.data.value_extractor.md#module-toolboxdatavalue_extractor): A tool for extracting values from a set of possible entries.
- [`toolbox.files`](./toolbox.files.md#module-toolboxfiles): The `files` package provides several utilities for handling files.
- [`toolbox.files.csv_file`](./toolbox.files.csv_file.md#module-toolboxfilescsv_file): A simple API for reading and writing CSV files.
- [`toolbox.files.file`](./toolbox.files.file.md#module-toolboxfilesfile): A collection of utilities for accessing files.
- [`toolbox.files.file_manager`](./toolbox.files.file_manager.md#module-toolboxfilesfile_manager): A simple class for reading and writing files.
- [`toolbox.files.json_file`](./toolbox.files.json_file.md#module-toolboxfilesjson_file): A simple API for reading and writing JSON files.
- [`toolbox.files.path`](./toolbox.files.path.md#module-toolboxfilespath): A collection of utilities around file paths.
- [`toolbox.files.pickle_file`](./toolbox.files.pickle_file.md#module-toolboxfilespickle_file): A simple API for reading and writing pickle files.
- [`toolbox.iterators`](./toolbox.iterators.md#module-toolboxiterators): A collection of iterators.
- [`toolbox.iterators.iter_deep`](./toolbox.iterators.iter_deep.md#module-toolboxiteratorsiter_deep): An iterator for returning elements from nested iterables.
- [`toolbox.logging`](./toolbox.logging.md#module-toolboxlogging): The `logging` package provides several utilities for logging purpose.
- [`toolbox.logging.config`](./toolbox.logging.config.md#module-toolboxloggingconfig): A collection of utilities for logging purpose.
- [`toolbox.logging.log_file`](./toolbox.logging.log_file.md#module-toolboxlogginglog_file): A custom logger that writes directly to a file.
- [`toolbox.math`](./toolbox.math.md#module-toolboxmath): A collection of Math related tools.
- [`toolbox.math.combination`](./toolbox.math.combination.md#module-toolboxmathcombination): A set of functions for working with combinations.
- [`toolbox.math.utils`](./toolbox.math.utils.md#module-toolboxmathutils): A set of helper functions related to math.
- [`toolbox.system`](./toolbox.system.md#module-toolboxsystem): The `system` package provides several utilities for low level management.
- [`toolbox.system.module`](./toolbox.system.module.md#module-toolboxsystemmodule): A set of helpers for loading properties dynamically.
- [`toolbox.system.type`](./toolbox.system.type.md#module-toolboxsystemtype): A set of helpers for types management.
- [`toolbox.testing`](./toolbox.testing.md#module-toolboxtesting): The `testing` package provides utilities for testing purpose.
- [`toolbox.testing.decorators`](./toolbox.testing.decorators.md#module-toolboxtestingdecorators): A collection of decorators for testing purpose.
- [`toolbox.testing.test_case`](./toolbox.testing.test_case.md#module-toolboxtestingtest_case): Extends the default Python TestCase with more assertions.
- [`toolbox.time`](./toolbox.time.md#module-toolboxtime): A collection of time related utilities.
- [`toolbox.time.duration`](./toolbox.time.duration.md#module-toolboxtimeduration): Represents a nanosecond duration.
- [`toolbox.time.timer`](./toolbox.time.timer.md#module-toolboxtimetimer): Captures the time spent.
- [`toolbox.time.weekday`](./toolbox.time.weekday.md#module-toolboxtimeweekday): A tool for getting the date of a weekday.

## Classes

- [`config.Config`](./toolbox.config.config.md#class-config): Handles a configuration.
- [`config_option.ConfigOption`](./toolbox.config.config_option.md#class-configoption): Handles a config option.
- [`mappers.ValueMapper`](./toolbox.data.mappers.md#class-valuemapper): The interface for a value mapper.
- [`value_extractor.ValueExtractor`](./toolbox.data.value_extractor.md#class-valueextractor): Extracts a value from a set of possible entries.
- [`csv_file.CSVFile`](./toolbox.files.csv_file.md#class-csvfile): Offers a simple API for reading and writing CSV files.
- [`file_manager.FileManager`](./toolbox.files.file_manager.md#class-filemanager): Offers a simple API for reading and writing files.
- [`json_file.JSONFile`](./toolbox.files.json_file.md#class-jsonfile): Offers a simple API for reading and writing JSON files.
- [`pickle_file.PickleFile`](./toolbox.files.pickle_file.md#class-picklefile): Offers a simple API for reading and writing pickle files.
- [`log_file.LogFile`](./toolbox.logging.log_file.md#class-logfile): Offers a similar API to the Python builtin loggers for logging to a custom file.
- [`test_case.TestCase`](./toolbox.testing.test_case.md#class-testcase): Test class with additional assertions.
- [`duration.Duration`](./toolbox.time.duration.md#class-duration): Represents a nanosecond duration.
- [`timer.Timer`](./toolbox.time.timer.md#class-timer): Capture the time spent.
- [`weekday.Weekday`](./toolbox.time.weekday.md#class-weekday): Gets the date of a weekday given a particular date.

## Functions

- [`config_option.create_options`](./toolbox.config.config_option.md#function-create_options): Create options from a list of descriptors.
- [`mappers.boolean`](./toolbox.data.mappers.md#function-boolean): Converts a value to a boolean value.
- [`mappers.decimal`](./toolbox.data.mappers.md#function-decimal): Creates a mapper for casting decimal values to floats.
- [`mappers.passthrough`](./toolbox.data.mappers.md#function-passthrough): A passthrough mapper. It returns the value as it is.
- [`csv_file.read_csv_file`](./toolbox.files.csv_file.md#function-read_csv_file): Reads a CSV content from a file.
- [`csv_file.read_zip_csv`](./toolbox.files.csv_file.md#function-read_zip_csv): Reads a CSV content from a Zip.
- [`csv_file.write_csv_file`](./toolbox.files.csv_file.md#function-write_csv_file): Writes a CSV content to a file.
- [`file.fetch_content`](./toolbox.files.file.md#function-fetch_content): Downloads content from the given URL.
- [`file.get_file_mode`](./toolbox.files.file.md#function-get_file_mode): Gets the file access mode given the expectations.
- [`file.read_file`](./toolbox.files.file.md#function-read_file): Reads a content from a file.
- [`file.read_zip_file`](./toolbox.files.file.md#function-read_zip_file): Extracts a file content from a Zip archive.
- [`file.write_file`](./toolbox.files.file.md#function-write_file): Writes a content to a file.
- [`json_file.read_json_file`](./toolbox.files.json_file.md#function-read_json_file): Reads a JSON content from a file.
- [`json_file.write_json_file`](./toolbox.files.json_file.md#function-write_json_file): Writes a JSON content to a file.
- [`path.create_file_path`](./toolbox.files.path.md#function-create_file_path): Creates the parent path for a file.
- [`path.delete_path`](./toolbox.files.path.md#function-delete_path): Deletes the file or the folder at the given path.
- [`path.get_application_name`](./toolbox.files.path.md#function-get_application_name): Gets the name of the application, based on the root folder.
- [`path.get_application_path`](./toolbox.files.path.md#function-get_application_path): Gets the path to the application's root.
- [`path.get_cache_path`](./toolbox.files.path.md#function-get_cache_path): Gets the path to a cache folder.
- [`path.get_file_path`](./toolbox.files.path.md#function-get_file_path): Gets a full path for a file inside the application.
- [`path.get_module_folder_path`](./toolbox.files.path.md#function-get_module_folder_path): Gets the path to the folder containing the given module.
- [`path.get_module_path`](./toolbox.files.path.md#function-get_module_path): Gets the path to the given module.
- [`pickle_file.read_pickle_file`](./toolbox.files.pickle_file.md#function-read_pickle_file): Loads a list of objects from a file.
- [`pickle_file.write_pickle_file`](./toolbox.files.pickle_file.md#function-write_pickle_file): Writes a list of objects to a file.
- [`iter_deep.iter_deep`](./toolbox.iterators.iter_deep.md#function-iter_deep): Creates an iterator that returns elements from each iterable including nested ones.
- [`config.handle_uncaught_exceptions`](./toolbox.logging.config.md#function-handle_uncaught_exceptions): Installs a collector for logging uncaught exceptions.
- [`config.setup_file_logging`](./toolbox.logging.config.md#function-setup_file_logging): Setup the application log to a file logger.
- [`combination.get_combination_from_rank`](./toolbox.math.combination.md#function-get_combination_from_rank): Gets the combination corresponding to a particular rank.
- [`combination.get_combination_rank`](./toolbox.math.combination.md#function-get_combination_rank): Gets the rank of a combination.
- [`combination.get_combinations`](./toolbox.math.combination.md#function-get_combinations): Yields lists of combined values according to the combinations defined by the lengths.
- [`utils.limit`](./toolbox.math.utils.md#function-limit): Limits a value inside boundaries.
- [`utils.minmax`](./toolbox.math.utils.md#function-minmax): Returns with the min and the max value from the arguments.
- [`utils.quantity`](./toolbox.math.utils.md#function-quantity): Gets a quantity with respect to a quota applied to a total.
- [`module.import_and_call`](./toolbox.system.module.md#function-import_and_call): Imports a callable from the given namespace, then call it with the given parameters.
- [`module.import_property`](./toolbox.system.module.md#function-import_property): Imports a property from the given namespace.
- [`type.full_type`](./toolbox.system.type.md#function-full_type): Gets the fully qualified type of a value.
- [`decorators.test_cases`](./toolbox.testing.decorators.md#function-test_cases): Creates a decorator for parametric test cases.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
