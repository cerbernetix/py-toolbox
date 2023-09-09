"""
Entry point for the `files` package.
"""
from toolbox.files.file import get_file_mode, read_file, write_file
from toolbox.files.file_manager import FileManager
from toolbox.files.path import (
    create_file_path,
    delete_path,
    get_application_name,
    get_application_path,
    get_file_path,
    get_module_folder_path,
    get_module_path,
)
