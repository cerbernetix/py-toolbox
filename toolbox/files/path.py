"""
A collection of utilities around file paths.
"""
import os
import sys
from pathlib import PurePath


def get_module_path(name: str) -> PurePath():
    """
    Gets the path to the given module.

    Args:
        - name (str): The module for which get the path.

    Returns:
        PurePath: The path to the module.
    """
    if name in sys.modules:
        return PurePath(sys.modules[name].__file__)

    return PurePath()


def get_module_folder_path(name: str) -> PurePath():
    """
    Gets the path to the folder containing the given module.

    Args:
        - name (str): The module for which get the path.

    Returns:
        PurePath|None: The path to the folder containing the given module.
    """
    return get_module_path(name).parent


def get_application_path() -> PurePath:
    """
    Gets the path to the application's root.

    Returns:
        PurePath: The path to the application's root.
    """
    return get_module_folder_path("__main__")


def get_application_name() -> str:
    """
    Gets the name of the application, based on the root folder.

    Returns:
        - str: The name of the application.
    """
    return get_application_path().name


def get_file_path(relative) -> PurePath:
    """
    Gets a full path for a file inside the application.

    Args:
        - relative (str): The internal path the file from the application's root.

    Returns:
        PurePath: The full path.
    """
    return get_application_path().joinpath(relative)


def create_file_path(path: str) -> bool:
    """
    Creates the parent path for a file.

    Note: exceptions are caught internally, the function will always
    return either with `True` in case of success, or `False` otherwise.

    Args:
        - path (str): The path to the file.

    Returns:
        bool: `True` if the path has been created, `False` otherwise.
    """
    folder = str(PurePath(path).parent)

    try:
        if not os.path.isdir(folder):
            os.makedirs(folder)
            return True

    except OSError:
        return False

    return False


def delete_path(path: str) -> bool:
    """
    Deletes the file or the folder at the given path.

    If this is a folder, it must be empty.

    Note: exceptions are caught internally, the function will always
    return either with `True` in case of success, or `False` otherwise.

    Args:
        - path (str): The path to the file or folder to delete.

    Returns:
        bool: `True` if the path has been deleted, `False` otherwise.
    """
    try:
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)

    except FileNotFoundError:
        return False

    except OSError:
        return False

    return True
