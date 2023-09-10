<!-- markdownlint-disable -->

<a href="../toolbox/files/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files`
The `files` package provides several utilities for handling files. 

It contains: 
- File manager for various types: 
    - `FileManager(filename, ...)` - Manages read and write for generic files. 
    - `CSVFile(filename, ...)` - Manages read and write for CSV files. 
    - `JSONFile(filename, ...)` - Manages read and write for JSON files. 
    - `PickleFile(filename, ...)` - Manages read and write for pickle files. 
- Read and Write helpers: 
    - `read_file(filename, ...)` - Reads all the content from a file at once. 
    - `write_file(filename, data, ...)` - Writes content to a file at once. 
    - `read_csv_file(filename, ...)` - Reads all the content from a CSV file at once. 
    - `write_csv_file(filename, data, ...)` - Writes content to a CSV file at once. 
    - `read_json_file(filename, ...)` - Reads all the content from a JSON file at once. 
    - `write_json_file(filename, data, ...)` - Writes content to a JSON file at once. 
    - `read_pickle_file(filename, ...)` - Reads all the content from a pickle file at once. 
    - `write_pickle_file(filename, data, ...)` - Writes content to a pickle file at once. 
- File helpers: 
    - `get_file_mode()` - Gets the file mode given the desired access type. 
    - `create_file_path(filepath)` - Creates the path to the given filename. 
    - `delete_path(filepath)` - Deletes the file or the folder at the given path. 
- Path helpers: 
    - `get_application_name(package)` - Gets the name of the application. 
    - `get_application_path(package)` - Gets the path of the application. 
    - `get_file_path(filename, package)` - Gets the path to a file inside the application. 
    - `get_module_folder_path(module)` - Gets the path to a module's parent folder. 
    - `get_module_path(module)` - Gets the path to a module. 

**Global Variables**
---------------
- **file**
- **file_manager**
- **csv_file**
- **CSV_DIALECT**
- **CSV_ENCODING**
- **json_file**
- **JSON_ENCODING**
- **JSON_INDENT**
- **path**
- **pickle_file**




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
