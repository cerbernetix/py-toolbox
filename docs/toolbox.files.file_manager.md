<!-- markdownlint-disable -->

<a href="../toolbox/files/file_manager.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.file_manager`
A simple class for reading and writing files. 



**Examples:**
 ```python
from toolbox.files import FileManager

filename = 'path/to/file.txt'
data = "Some content"

# Manage a text file
file = FileManager(filename, encoding='UTF-8')

# Create the file
file.write_file(data)

# It can also be done using the open/write API
with file.open(create=True):
     file.write(data)

# Show the file
print(file.read_file(filename))

# It can also be done using the open/read API
with file:
     print(file.read())
``` 



---

<a href="../toolbox/files/file_manager.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `FileManager`
Offers a simple API for reading and writing files. 

The class binds a filename with a set of properties so that it can be opened in a consistent way. 

The read API does not allow to size the data to read. The FileManager reads all the content. However, it comes better with the specialized child classes, which can read chunks of the file based on a specific format. See CSVFile, JSONFile, or PickleFile for more information. 



**Attributes:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`binary`</b> (bool):  The type of file: binary (True) or text (False). 
 - <b>`encoding`</b> (str, optional):  The file encoding, only needed for text files. 



**Examples:**
 ```python
from toolbox.files import FileManager

file = FileManager("path/to/the/file", binary=False, encoding="UTF-8")

# open the file, then read its content
with file:
    content = file.read()

# write data to the file
with file(create=True):
    for chunk in data:
         file.write(chunk)

# load the whole file, handling internally its opening
content = file.read_file()
``` 

<a href="../toolbox/files/file_manager.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    filename: 'str',
    binary: 'bool' = False,
    create: 'bool' = False,
    append: 'bool' = False,
    read: 'bool' = False,
    write: 'bool' = False,
    encoding: 'str' = None,
    **kwargs
)
```

Creates a file manager. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`binary`</b> (bool, optional):  The type of file: binary (True) or text (False). Defaults to False. 
 - <b>`create`</b> (bool, optional):  Expect to create the file. If it exists, it will be replaced. Defaults to False. 
 - <b>`append`</b> (bool, optional):  Expect to extend the file. Data will be added at the end. Defaults to False. 
 - <b>`read`</b> (bool, optional):  Expect to also read the file. Defaults to False. 
 - <b>`write`</b> (bool, optional):  Expect to also write to the file. Defaults to False. 
 - <b>`encoding`</b> (str, optional):  The file encoding, only needed for text files. Defaults to None. 



**Examples:**
 ```python
from toolbox.files import FileManager

# Create a file manager
file = FileManager('path/to/filename')

# File can be opened directly as the manager is created
with FileManager('path/to/filename') as file:
    data = file.read()

with FileManager('path/to/filename', create=True) as file:
    file.write(data)
``` 




---

<a href="../toolbox/files/file_manager.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `close`

```python
close() → FileManager
```

Closes the file. 

Note: it does nothing if the file is already closed. 



**Returns:**
 
 - <b>`FileManager`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.files import FileManager

file = FileManager('path/to/filename')

# A file is closed implicitly when using the context manager
with file:
    data = file.read()

# However, open/close can be explicitly called
file.open(create=True)
file.write(data)
file.close()
``` 

---

<a href="../toolbox/files/file_manager.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `open`

```python
open(
    create: 'bool' = False,
    append: 'bool' = False,
    read: 'bool' = False,
    write: 'bool' = False
) → FileManager
```

Opens the file for access. 

Note: If the file was already opened, it is first closed. 



**Args:**
 
 - <b>`create`</b> (bool, optional):  Expect to create the file. If it exists, it will be replaced. Defaults to False. 
 - <b>`append`</b> (bool, optional):  Expect to extend the file. Data will be added at the end. Defaults to False. 
 - <b>`read`</b> (bool, optional):  Expect to also read the file. Defaults to False. 
 - <b>`write`</b> (bool, optional):  Expect to also write to the file. Defaults to False. 



**Returns:**
 
 - <b>`FileManager`</b>:  Chains the instance. 



**Examples:**
 ```python
from toolbox.files import FileManager

file = FileManager('path/to/filename')

# A file manager can open explicitly a file
with file.open():
    data = file.read()

with file.open(create=True):
    file.write(data)

# It can also be opened implicitly
with file:
    data = file.read()

# To create the file while opening implicitly
with file(create=True):
    file.write(data)

# The file is also (re)opened when using the iteration protocol
data = [dat for dat in file]
``` 

---

<a href="../toolbox/files/file_manager.py#L265"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read() → str | bytes
```

Reads the next content from the file. 

Note: the file must be opened upfront. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the file is not opened. 
 - <b>`OSError`</b>:  If the file cannot be read. 



**Returns:**
 
 - <b>`str|bytes`</b>:  The content loaded from the file, or None if the file is at EOF. 



**Examples:**
 ```python
from toolbox.files import FileManager

file = FileManager('path/to/filename')

# When calling the read API, the next chunk in the file is read.
# With the base class, all the content is read.
with file:
    data = file.read()
``` 

---

<a href="../toolbox/files/file_manager.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_file`

```python
read_file() → str | bytes
```

Reads all the content from the file. 

Note: If the file was already opened, it is first closed, then opened in read mode. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`str|bytes`</b>:  The content read from the file. 



**Examples:**
 ```python
from toolbox.files import FileManager

file = FileManager('path/to/filename')

# A file can be read all at once
data = file.read_file()
``` 

---

<a href="../toolbox/files/file_manager.py#L294"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write`

```python
write(data: 'str | bytes') → int
```

Writes content to the file. 

Note: the file must be opened upfront. 



**Args:**
 
 - <b>`data`</b> (str|bytes):  The content to write to the file. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the file is not opened. 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written. 



**Examples:**
 ```python
from toolbox.files import FileManager

file = FileManager('path/to/filename')

# When calling the write API, a chunk of data is written to the file.
with file(create=True):
    file.write(data)
``` 

---

<a href="../toolbox/files/file_manager.py#L238"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write_file`

```python
write_file(data: 'str | bytes') → int
```

Writes whole content to the file. 

Note: If the file was already opened, it is first closed, then opened in write mode. 



**Args:**
 
 - <b>`data`</b> (str|bytes):  The content to write to the file. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written. 



**Examples:**
 ```python
from toolbox.files import FileManager

file = FileManager('path/to/filename')

# A file can be written all at once
file.write_file(data)
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
