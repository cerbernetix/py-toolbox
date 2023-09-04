# py-toolbox

A set of utilities for Python projects

<!-- vscode-markdown-toc -->

-   [Requirements](#Requirements)
-   [Installation](#Installation)
-   [Development](#Development)
-   [Testing](#Testing)
-   [License](#License)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Requirements'></a>Requirements

The toolbox has been written in **`Python 3`**, and it needs version `3.11`.

The dependencies are managed by `pip` using the file `requirements.txt`.

## <a name='Installation'></a>Installation

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

## <a name='Development'></a>Development

Code is linted using PyLint and formatted using Black.

## <a name='Testing'></a>Testing

Each module comes with unit tests, by convention, a `test` folder must be added to each package

Unit tests are made using `unittest`. To run them:

```sh
python3 -m unittest
```

## <a name='License'></a>License

Copyright (c) 2023 Jean-Sébastien CONAN
Distributed under the MIT License (See LICENSE file or copy at [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)).
