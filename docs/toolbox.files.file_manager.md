<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.file_manager`
A simple class for reading and writing files. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

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

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
from cerbernetix.toolbox.files import FileManager

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

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
from cerbernetix.toolbox.files import FileManager

# Create a file manager
file = FileManager('path/to/filename')

# File can be opened directly as the manager is created
with FileManager('path/to/filename') as file:
    data = file.read()

with FileManager('path/to/filename', create=True) as file:
    file.write(data)
``` 


---

#### <kbd>property</kbd> age

Gets the age of the file. Say the time elapsed since it was last modified. 



**Returns:**
 
 - <b>`float`</b>:  The number of seconds elapsed since the file was modified. It will be 0 if the file does not exist. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

if file.age > 3600:
    print('The file is there for more than 1 hour')
``` 

---

#### <kbd>property</kbd> basename

Gets the base filename, without the path. 



**Returns:**
 
 - <b>`str`</b>:  The base name of the file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/file.txt')

# Print 'file.txt'
print(file.basename)
``` 

---

#### <kbd>property</kbd> date

Gets the modification date of the file. 



**Returns:**
 
 - <b>`float`</b>:  The last modification date of the file. It will be 0 if the file does not exist. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

date = file.date
``` 

---

#### <kbd>property</kbd> dirname

Gets the folder path of the file. 



**Returns:**
 
 - <b>`str`</b>:  The base name of the file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/file.txt')

# Print 'path/to'
print(file.dirname)
``` 

---

#### <kbd>property</kbd> ext

Gets the file extension from the filename. 



**Returns:**
 
 - <b>`str`</b>:  The extension of the file, including the dot. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/file.txt')

# Print '.txt'
print(file.ext)
``` 

---

#### <kbd>property</kbd> name

Gets the file name without the extension. 



**Returns:**
 
 - <b>`str`</b>:  The name of the file without the extension. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/file.txt')

# Print 'file'
print(file.name)
``` 

---

#### <kbd>property</kbd> size

Gets the size of the file. 



**Returns:**
 
 - <b>`int`</b>:  The size of the file. It will be 0 if the file does not exist. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

size = file.size
``` 



---

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L508"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check`

```python
check(
    must_exist: 'bool' = None,
    min_time: 'int' = None,
    max_time: 'int' = None,
    min_age: 'int' = None,
    max_age: 'int' = None,
    min_size: 'int' = None,
    max_size: 'int' = None
) → bool
```

Tells if the file is valid with respect to the specified criteria. 



**Args:**
 
 - <b>`must_exist`</b> (bool, optional):  Should the file exist (True) or not (False). Defaults to None. 
 - <b>`min_time`</b> (int, optional):  The file must be created after the given timestamp. Defaults to None. 
 - <b>`max_time`</b> (int, optional):  The file must be created before the given timestamp. Defaults to None. 
 - <b>`min_age`</b> (int, optional):  The file must be older than the given age in seconds. Defaults to None. 
 - <b>`max_age`</b> (int, optional):  The file must be younger than the given age in seconds. Defaults to None. 
 - <b>`min_size`</b> (int, optional):  The file must be greater than the given size in bytes. Defaults to None. 
 - <b>`max_size`</b> (int, optional):  The file must be smaller than the given size in bytes. Defaults to None. 



**Returns:**
 
 - <b>`bool`</b>:  Returns True if the file matches the specified criteria, otherwise, False. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename"')

# Check the file is not too old
if file.check(max_age=14400):
    print('The file is still up to date.')
else:
    print('The file must be updated!')

# Check the file is not too big
if file.check(max_size=4096):
    print('The file can accept more data.')
else:
    print('The file must be trimmed!')
``` 

# Check the file has been created before a given date if file.check(min_time=datetime(2023, 10, 10).timestamp()): print('The file has been created before.') else: print('The file has been created after!') ```


---

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L333"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
from cerbernetix.toolbox.files import FileManager

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

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L625"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_path`

```python
create_path() → bool
```

Creates the parent path of the file. 

Note: exceptions are caught internally, the function will always return either with `True` in case of success, or `False` otherwise. 



**Returns:**
 
 - <b>`bool`</b>:  `True` if the path has been created, `False` otherwise. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename"')

# Create the parent folder to the file
if file.create_path():
    print('The path to the parent folder has been created!')
else:
    print('The path has not been created!')
``` 

---

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L596"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(must_exist: 'bool' = False) → bool
```

Deletes the file. 



**Args:**
 
 - <b>`must_exist`</b> (bool, optional):  Deletes the file only if it exists. Defaults to False. 



**Returns:**
 
 - <b>`bool`</b>:  Returns True if the file has been deleted, False otherwise. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

# Delete if the file exists
file.delete(True)

# Delete the file anyway, will raise an error if the file does not exist
file.delete()
``` 

---

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L488"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `exists`

```python
exists() → bool
```

Tells if the file already exists. 



**Returns:**
 
 - <b>`bool`</b>:  Returns True if the file exists, False otherwise. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

# Read only if the file exists
if file.exists():
    with file:
         data = file.read()
``` 

---

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L272"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
from cerbernetix.toolbox.files import FileManager

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

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L428"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

# When calling the read API, the next chunk in the file is read.
# With the base class, all the content is read.
with file:
    data = file.read()
``` 

---

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L364"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_file`

```python
read_file(iterator: 'bool' = False) → str | bytes | Iterable[str | bytes]
```

Reads all the content from the file. 

Note: If the file was already opened, it is first closed, then opened in read mode. 



**Args:**
 
 - <b>`iterator`</b> (bool, optional):  When True, the function will return an iterator instead. However, with the base implementation, it will return the whole content of the file from a unique iteration. Defaults to False. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`str | bytes | Iterable[str | bytes]`</b>:  The content read from the file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

# A file can be read all at once
data = file.read_file()

# An iterator can be returned instead
for data in file.read_file(iterator=True):
    print(data)
``` 

---

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L457"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

# When calling the write API, a chunk of data is written to the file.
with file(create=True):
    file.write(data)
``` 

---

<a href="../src/cerbernetix/toolbox/files/file_manager.py#L401"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
from cerbernetix.toolbox.files import FileManager

file = FileManager('path/to/filename')

# A file can be written all at once
file.write_file(data)
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
