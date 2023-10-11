# py-toolbox

`py-toolbox` is a set of utilities for Python projects

<!-- vscode-markdown-toc -->

-   [Requirements](#Requirements)
-   [Installation](#Installation)
-   [Usage](#Usage)
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

## <a name='Usage'></a>Usage

`py-toolbox` offers several utilities per domain.

Please refer to the [documentation](./docs/README.md) for more information.

The documentation is generated using [lazydocs](https://github.com/ml-tooling/lazydocs).

The script `./pydoc.sh` can be used to regenerate it.

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
pip install -e .
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

Code is linted using [PyLint](https://pylint.org/) and formatted using [Black](https://github.com/psf/black). The docstrings are validated using [pydocstyle](https://github.com/PyCQA/pydocstyle).

### <a name='Testing'></a>Testing

Each module comes with unit tests, by convention, a `test` folder must be added to each package

Unit tests are made using `unittest`. To run them:

```sh
python3 -m unittest
```

## <a name='License'></a>License

Copyright (c) 2023 Jean-Sébastien CONAN
Distributed under the MIT License (See LICENSE file or copy at [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)).
