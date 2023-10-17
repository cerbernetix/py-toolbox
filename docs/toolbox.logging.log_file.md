<!-- markdownlint-disable -->

<a href="../src/toolbox/logging/log_file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.logging.log_file`
A custom logger that writes directly to a file. 



**Examples:**
 ```python
from toolbox.logging import LogFile

# Create a log file at the current directory, named 'trace.log'
logger = LogFile()

# Create a log file at the given path
logger = LogFile('path/to/file')

# Log something
logger.info('The received value is %d', value)

# Log a debug info
logger.debug('For debug purpose: %d given to %s', value, action)

# Log a warning
logger.warn('Something bad happened, but the program can continue...')

# Log an error
logger.error('An error occurred: %s', error)
``` 

**Global Variables**
---------------
- **LOG_ENCODING**
- **LOG_FILE_NAME**
- **LOG_FILE_PATTERN**
- **LOG_FILE_LOG_FORMAT**


---

<a href="../src/toolbox/logging/log_file.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `LogFile`
Offers a similar API to the Python builtin loggers for logging to a custom file. 

This is useful for keeping an audit log, aside the main log, or tracing a particular process without polluting the main log. 



**Attributes:**
 
 - <b>`filename`</b> (str):  The filename of the log file. 
 - <b>`level`</b> (int):  The accepted log level. 
 - <b>`encoding`</b> (str):  The file encoding. 
 - <b>`line_format`</b> (str):  The format for the log events. 
 - <b>`name`</b> (str):  The name of the logger, also used for the log events. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.info('The received value is %d', value)
``` 

<a href="../src/toolbox/logging/log_file.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    filename: 'str' = None,
    level: 'int' = 20,
    encoding: 'str' = 'utf-8',
    line_format: 'str' = '%(asctime)s %(levelname)s: %(message)s',
    name: 'str' = 'trace'
) → None
```

Creates a file logger. 



**Args:**
 
 - <b>`filename`</b> (str, optional):  The filename of the log, if omitted the log name is used. Defaults to None. 
 - <b>`level`</b> (int, optional):  The accepted log level. Defaults to logging.INFO. 
 - <b>`encoding`</b> (str, optional):  The file encoding. Defaults to LOG_ENCODING. 
 - <b>`line_format`</b> (str, optional):  The format for the log events. Defaults to LOG_FILE_LOG_FORMAT. 
 - <b>`name`</b> (str, optional):  The name of the logger, also used for the log events. If the log filename is omitted, it will also be used for the filename. Defaults to LOG_FILE_NAME. 



**Examples:**
 ```python
from toolbox.logging import LogFile

# Create a log file at the current directory, named 'trace.log'
logger = LogFile()

# Create a log file at the given path
logger = LogFile('path/to/file', logging.DEBUG)

# Log something
logger.debug('Start the process')
logger.info('The received value is %d', value)
logger.debug('Process completed')
``` 


---

#### <kbd>property</kbd> encoding

The file encoding. 



**Returns:**
 
 - <b>`str`</b>:  The file encoding. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

print(logger.encoding)
``` 

---

#### <kbd>property</kbd> filename

The filename of the log. 



**Returns:**
 
 - <b>`str`</b>:  The filename of the log. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()


print(logger.filename)
``` 

---

#### <kbd>property</kbd> level

The accepted log level. 



**Returns:**
 
 - <b>`int`</b>:  The accepted log level. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

print(logger.level)
``` 

---

#### <kbd>property</kbd> line_format

The format for the log events. 



**Returns:**
 
 - <b>`str`</b>:  The format for the log events. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

print(logger.line_format)
``` 

---

#### <kbd>property</kbd> name

The name of the logger. 



**Returns:**
 
 - <b>`str`</b>:  The name of the logger. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

print(logger.name)
``` 



---

<a href="../src/toolbox/logging/log_file.py#L479"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `close`

```python
close() → LogFile
```

Closes the log file. 

Note: If the file was already closed, it does nothing. This method is automatically called before exiting the program. It is not need to call it explicitly. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.info('Something was done at %s', datetime.now())

logger.close() # not necessary since it will be called automatically upon exit.
``` 

---

<a href="../src/toolbox/logging/log_file.py#L359"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `debug`

```python
debug(message: 'str', *args, **kwargs) → LogFile
```

Logs a debug message. Formatted string as for classical logging is supported. 



**Args:**
 
 - <b>`message`</b> (str):  The message to log. 
 - <b>`*args (tuple[Any])`</b>:  Variable data to merge into the msg argument to obtain the event description. 
 - <b>`**kwargs (dict[str, Any])`</b>:  Additional parameters for the event. The following is inspected : 
    - pathname (str, optional): The full string path of the source file where the logging call was made.. Defaults to None. 
    - lineno (int, optional): The line number in the source file where the logging call was made. Defaults to 0. 
    - exc_info (tuple | None, optional) – An exception tuple with the current exception information, as returned by sys.exc_info(), or None if no exception information is available. Defaults to None. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.debug('For debug purpose: %d given to %s', value, action)
``` 

---

<a href="../src/toolbox/logging/log_file.py#L506"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete() → LogFile
```

Deletes the log file. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.delete()
``` 

---

<a href="../src/toolbox/logging/log_file.py#L421"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `error`

```python
error(message: 'str', *args, **kwargs) → LogFile
```

Logs an error message. Formatted string as for classical logging is supported. 



**Args:**
 
 - <b>`message`</b> (str):  The message to log. 
 - <b>`*args (tuple[Any])`</b>:  Variable data to merge into the msg argument to obtain the event description. 
 - <b>`**kwargs (dict[str, Any])`</b>:  Additional parameters for the event. The following is inspected : 
    - pathname (str, optional): The full string path of the source file where the logging call was made.. Defaults to None. 
    - lineno (int, optional): The line number in the source file where the logging call was made. Defaults to 0. 
    - exc_info (tuple | None, optional) – An exception tuple with the current exception information, as returned by sys.exc_info(), or None if no exception information is available. Defaults to None. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.error('An error occurred: %s', error)
``` 

---

<a href="../src/toolbox/logging/log_file.py#L328"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `info`

```python
info(message: 'str', *args, **kwargs) → LogFile
```

Logs an info message. Formatted string as for classical logging is supported. 



**Args:**
 
 - <b>`message`</b> (str):  The message to log. 
 - <b>`*args (tuple[Any])`</b>:  Variable data to merge into the msg argument to obtain the event description. 
 - <b>`**kwargs (dict[str, Any])`</b>:  Additional parameters for the event. The following is inspected : 
    - pathname (str, optional): The full string path of the source file where the logging call was made.. Defaults to None. 
    - lineno (int, optional): The line number in the source file where the logging call was made. Defaults to 0. 
    - exc_info (tuple | None, optional) – An exception tuple with the current exception information, as returned by sys.exc_info(), or None if no exception information is available. Defaults to None. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.info('The received value is %d', value)
``` 

---

<a href="../src/toolbox/logging/log_file.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `log`

```python
log(level: 'int', message: 'str', *args, **kwargs) → LogFile
```

Logs a message with the given level. 



**Args:**
 
 - <b>`level`</b> (int):  The log level of the message. 
 - <b>`message`</b> (str):  The message to log. Format parameters are accepted. 
 - <b>`*args (tuple[Any])`</b>:  Variable data to merge into the msg argument to obtain the event description. 
 - <b>`**kwargs (dict[str, Any])`</b>:  Additional parameters for the event. The following is inspected : 
    - pathname (str, optional): The full string path of the source file where the logging call was made.. Defaults to None. 
    - lineno (int, optional): The line number in the source file where the logging call was made. Defaults to 0. 
    - exc_info (tuple | None, optional) – An exception tuple with the current exception information, as returned by sys.exc_info(), or None if no exception information is available. Defaults to None. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.log(logging.INFO, 'The received value is %d', value)
logger.log(logging.DEBUG, 'For debug purpose: %d given to %s', value, action)
logger.log(logging.WARNING, 'Something bad happened, but the program can continue...')
logger.log(logging.ERROR, 'An error occurred: %s', error)
``` 

---

<a href="../src/toolbox/logging/log_file.py#L452"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `open`

```python
open() → LogFile
```

Opens the log file. 

Note: If the file was already opened, it does nothing. This method is automatically called before logging anything. It is not need to call it explicitly. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.open() # not necessary since the .log() method will make sure the file is opened.

logger.info('Something was done at %s', datetime.now())
``` 

---

<a href="../src/toolbox/logging/log_file.py#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_format`

```python
set_format(line_format: 'str') → LogFile
```

Sets the log format. 



**Args:**
 
 - <b>`line_format`</b> (str):  The format for a log line. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.set_format('[%(asctime)s][%(levelname)s]: %(message)s')
``` 

---

<a href="../src/toolbox/logging/log_file.py#L208"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_level`

```python
set_level(level: 'int') → LogFile
```

Sets the log level. 



**Args:**
 
 - <b>`level`</b> (int):  The new log level. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.set_level(logging.DEBUG)
``` 

---

<a href="../src/toolbox/logging/log_file.py#L390"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `warn`

```python
warn(message: 'str', *args, **kwargs) → LogFile
```

Logs a warning message. Formatted string as for classical logging is supported. 



**Args:**
 
 - <b>`message`</b> (str):  The message to log. 
 - <b>`*args (tuple[Any])`</b>:  Variable data to merge into the msg argument to obtain the event description. 
 - <b>`**kwargs (dict[str, Any])`</b>:  Additional parameters for the event. The following is inspected : 
    - pathname (str, optional): The full string path of the source file where the logging call was made.. Defaults to None. 
    - lineno (int, optional): The line number in the source file where the logging call was made. Defaults to 0. 
    - exc_info (tuple | None, optional) – An exception tuple with the current exception information, as returned by sys.exc_info(), or None if no exception information is available. Defaults to None. 



**Returns:**
 
 - <b>`LogFile`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.logging import LogFile

logger = LogFile()

logger.warn('Something bad happened, but the program can continue...')
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
