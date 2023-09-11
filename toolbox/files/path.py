"""A collection of utilities around file paths.

Examples:
```python
from toolbox.files import (
    create_file_path,
    delete_path,
    get_application_name,
    get_application_path,
    get_file_path,
    get_module_folder_path,
    get_module_path,
)

# Get the path to a file below your application's root
folder = get_file_path('path/to/folder', 'my_package')
filename = f'{folder}/file'

# Create the parent folder to the file
if create_file_path(filename):
    print('The path to the parent folder has been created!')

    with open(filename, 'wt') as file:
        file.write('some content')

    # Delete the file
    if delete_path(filename):
        print('The file has been deleted!')
    else:
        print('Cannot delete the file!')

    # Delete the folder
    if delete_path(foldername):
        print('The folder has been deleted!')
    else:
        print('Cannot delete the folder, is it empty?')
else:
    print('The path has not been created!')
```
"""
import os
import sys
from pathlib import PurePath


def get_module_path(name: str) -> PurePath():
    """Gets the path to the given module.

    Args:
        name (str): The module for which get the path.

    Returns:
        PurePath: The path to the module.

    Examples:
    ```python
    from toolbox.files import get_module_path

    # Get the path of the module foo
    path = get_module_path('foo')
    ```
    """
    if name in sys.modules:
        return PurePath(sys.modules[name].__file__)

    return PurePath()


def get_module_folder_path(name: str) -> PurePath():
    """Gets the path to the folder containing the given module.

    Args:
        name (str): The module for which get the path.

    Returns:
        PurePath: The path to the folder containing the given module.

    Examples:
    ```python
    from toolbox.files import get_module_folder_path

    # Get the path to the folder containing the module foo
    path = get_module_folder_path('foo')
    ```
    """
    return get_module_path(name).parent


def get_application_path(name: str) -> PurePath:
    """Gets the path to the application's root.

    Args:
        name (str): The main package of the application.

    Returns:
        PurePath: The path to the application's root.

    Examples:
    ```python
    from toolbox.files import get_application_path

    # Get the path to the application, given the main package
    app_path = get_application_path('my_package')
    ```
    """
    return get_module_folder_path(name).parent


def get_application_name(name: str) -> str:
    """Gets the name of the application, based on the root folder.

    Args:
        name (str): The main package of the application.

    Returns:
        str: The name of the application.

    Examples:
    ```python
    from toolbox.files import get_application_name

    # Get the name of the application, given the main package
    print(get_application_name('my_package'))
    ```
    """
    return get_application_path(name).name


def get_file_path(relative: str, name: str) -> PurePath:
    """Gets a full path for a file inside the application.

    Args:
        relative (str): The internal path the file from the application's root.
        name (str): The main package of the application.

    Returns:
        PurePath: The full path.

    Examples:
    ```python
    from toolbox.files import get_file_path

    # Get the path to a file below your application's root
    filename = get_file_path('path/to/file', 'my_package')
    ```
    """
    return get_application_path(name).joinpath(relative)


def create_file_path(path: str) -> bool:
    """Creates the parent path for a file.

    Note: exceptions are caught internally, the function will always
    return either with `True` in case of success, or `False` otherwise.

    Args:
        path (str): The path to the file.

    Returns:
        bool: `True` if the path has been created, `False` otherwise.

    Examples:
    ```python
    from toolbox.files import create_file_path

    # Create the parent folder to the file
    if create_file_path('path/to/file):
        print('The path to the parent folder has been created!')
    else:
        print('The path has not been created!')
    ```
    """
    folder = str(PurePath(path).parent)

    try:
        if not os.path.isdir(folder):
            os.makedirs(folder)

        return True

    except OSError:
        return False


def delete_path(path: str) -> bool:
    """Deletes the file or the folder at the given path.

    If this is a folder, it must be empty.

    Note: exceptions are caught internally, the function will always
    return either with `True` in case of success, or `False` otherwise.

    Args:
        path (str): The path to the file or folder to delete.

    Returns:
        bool: `True` if the path has been deleted, `False` otherwise.

    Examples:
    ```python
    from toolbox.files import delete_path

    # Delete a file
    if delete_path('path/to/file):
        print('The file has been deleted!')
    else:
        print('Cannot delete the file!')

    # Delete a folder
    if delete_path('path/to/folder):
        print('The folder has been deleted!')
    else:
        print('Cannot delete the folder, is it empty?')
    ```
    """
    try:
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)

        return True

    except FileNotFoundError:
        return False

    except OSError:
        return False
