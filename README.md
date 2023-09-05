# py-toolbox

`py-toolbox` is a set of utilities for Python projects

<!-- vscode-markdown-toc -->

-   [Requirements](#Requirements)
-   [Installation](#Installation)
-   [Development](#Development)
    -   [Code style](#Codestyle)
    -   [Testing](#Testing)
-   [License](#License)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Requirements'></a>Requirements

The toolbox has been written in **`Python 3`**, and it needs version `3.7`.

The dependencies are managed by `pip` using the file `requirements.txt`.

## <a name='Installation'></a>Installation

To add `py-toolbox` to your project, run the following command:

```sh
pip install git+https://github.com/jsconan/py-toolbox.git
```

## Usage

`py-toolbox` offers several utilities per domain.

### Files

The package `toolbox.files` offers file related utilities.

-   `create_file_path(path: str) -> bool`:

    Creates the parent path for a file.

    **Note:** exceptions are caught internally, the function will always
    return either with `True` in case of success, or `False` otherwise.

    Args:

    -   path (`str`): The path to the file.

    Returns:

    -   `bool`: `True` if the path has been created, `False` otherwise.

    ***

-   `delete_path(path: str) -> bool`:

    Deletes the file or the folder at the given path.

    If this is a folder, it must be empty.

    **Note:** exceptions are caught internally, the function will always
    return either with `True` in case of success, or `False` otherwise.

    Args:

    -   path (`str`): The path to the file or folder to delete.

    Returns:

    -   `bool`: `True` if the path has been deleted, `False` otherwise.

    ***

-   `get_application_name(name: str) -> str`:

    Gets the name of the application, based on the root folder.

    Args:

    -   name (`str`): The main package of the application.

    Returns:

    -   `str`: The name of the application.

    ***

-   `get_application_path(name: str) -> PurePath`:

    Gets the path to the application's root.

    Args:

    -   name (`str`): The main package of the application.

    Returns:

    -   `PurePath`: The path to the application's root.

    ***

-   `get_file_path(relative: str, name: str) -> PurePath`:

    Gets a full path for a file inside the application.

    Args:

    -   relative (`str`): The internal path the file from the application's root.
    -   name (`str`): The main package of the application.

    Returns:

    -   `PurePath`: The full path.

    ***

-   `get_module_folder_path(name: str) -> PurePath()`:

    Gets the path to the folder containing the given module.

    Args:

    -   name (`str`): The module for which get the path.

    Returns:

    -   `PurePath`|`None`: The path to the folder containing the given module.

    ***

-   `get_module_path(name: str) -> PurePath()`:

    Gets the path to the given module.

    Args:

    -   name (`str`): The module for which get the path.

    Returns:

    -   `PurePath`: The path to the module.

    ***

## <a name='Development'></a>Development

Check out the repository:

```sh
git clone git@github.com:jsconan/py-toolbox.git
```

Then, create the virtual env and install the dependencies:

```sh
cd py-toolbox
python3 -m venv ".venv"
source "./venv/bin/activate"
pip install -r requirements.txt
```

**Note:** For deactivating the virtual env, call the command `deactivate`.

**Automating the environment activation/deactivation**

For activating the virtual env automatically when entering the project folder, and deactivating it when leaving the folder, you can add this snippet to you shell profile:

```sh
cd() {
    builtin cd "$@"

    local venv=".venv"

    # If a Python virtualenv is active, deactivate it if the new folder is outside
    if [[ -v VIRTUAL_ENV ]] ; then
        local parent=$(dirname "${VIRTUAL_ENV}")
        if [[ "${PWD}"/ != "${parent}"/* ]] ; then
            deactivate
        fi
    fi

    # If a Python env folder is found then activate the virtualenv
    if [[ -d "./${venv}" ]] ; then
        # Is it a Python venv?
        if [[ -f "./${venv}/bin/activate" ]] ; then
            source "./${venv}/bin/activate"
        fi
    fi
}
```

### <a name='Codestyle'></a>Code style

Code is linted using PyLint and formatted using Black.

### <a name='Testing'></a>Testing

Each module comes with unit tests, by convention, a `test` folder must be added to each package

Unit tests are made using `unittest`. To run them:

```sh
python3 -m unittest
```

## <a name='License'></a>License

Copyright (c) 2023 Jean-Sébastien CONAN
Distributed under the MIT License (See LICENSE file or copy at [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)).
