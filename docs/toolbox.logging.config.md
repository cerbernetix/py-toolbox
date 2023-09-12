<!-- markdownlint-disable -->

<a href="../toolbox/logging/config.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.logging.config`
A collection of utilities for logging purpose. 



**Examples:**
 ```python
from toolbox.logging import setup_file_logging, handle_uncaught_exceptions

setup_file_logging('path/to/file.log')
handle_uncaught_exceptions()

def main() -> None:
     ...

if __name__ == "__main__":
     main()
``` 

**Global Variables**
---------------
- **LOG_FILE**
- **LOG_FORMAT**
- **LOG_ENCODING**

---

<a href="../toolbox/logging/config.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `setup_file_logging`

```python
setup_file_logging(
    filename: str = 'app.log',
    level: int = 20,
    encoding: str = 'utf-8',
    log_format: str = '%(asctime)s %(levelname)s:%(name)s:%(message)s',
    **kwargs
) → None
```

Setup the application log to a file logger. 

By default, a file will be created in the current working directory, named 'app.log'. 



**Args:**
 
 - <b>`filename`</b> (str, optional):  The filename of the log file. Defaults to LOG_FILE. 
 - <b>`level`</b> (int, optional):  The log level to accept. Defaults to logging.INFO. 
 - <b>`encoding`</b> (str, optional):  The file encoding. Defaults to LOG_ENCODING. 
 - <b>`log_format`</b> (str, optional):  The format for each log event. Defaults to LOG_FORMAT. 



**Examples:**
 ```python
from toolbox.logging import setup_file_logging

setup_file_logging('path/to/file.log')
``` 


---

<a href="../toolbox/logging/config.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `handle_uncaught_exceptions`

```python
handle_uncaught_exceptions() → None
```

Installs a collector for logging uncaught exceptions. 

When an exception is not handled in the code, it will be logged with the message: 'Uncaught exception: <exception message>'. 



**Examples:**
 ```python
from toolbox.logging import handle_uncaught_exceptions

handle_uncaught_exceptions()

def main() -> None:
     ...

if __name__ == "__main__":
     main()
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
