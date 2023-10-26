<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/files/json_file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.json_file`
A simple API for reading and writing JSON files. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import JSONFile, read_json_file, write_json_file

filename = 'path/to/file.json'
json_data = [
     {'date': '2023-09-10', 'value': 42},
     {'date': '2023-09-11', 'value': 24},
     {'date': '2023-09-12', 'value': 44},
]

# Create a JSON file from the given data
write_json_file(filename, json_data, encoding='UTF-8', indent=2)

# Read the JSON data from an existing file
json_data = read_json_file(filename, encoding='UTF-8', indent=2)

# Use a file manager
json = JSONFile(filename, encoding='UTF-8', indent=2)

# Create a JSON file from the given data
json.write_file(json_data)

# Read the JSON data from an existing file
json_data = json.read_file()

# Write JSON content
with json.open(create=True):
     json.write(json_data)

# Read JSON content
with file:
     json_data = file.read()
``` 

**Global Variables**
---------------
- **JSON_ENCODING**
- **JSON_INDENT**

---

<a href="../src/cerbernetix/toolbox/files/json_file.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_json_file`

```python
read_json_file(filename: str, encoding: str = 'utf-8', **kwargs) → Any
```

Reads a JSON content from a file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to read. 
 - <b>`encoding`</b> (str, optional):  The file encoding. Defaults to JSON_ENCODING. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`Any`</b>:  The data read from the JSON file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import read_json_file

json_data = read_json_file('path/to/file', encoding='UTF-8')
``` 


---

<a href="../src/cerbernetix/toolbox/files/json_file.py#L249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_json_file`

```python
write_json_file(
    filename: str,
    data: Any,
    encoding: str = 'utf-8',
    indent: int = 4,
    **kwargs
) → int
```

Writes a JSON content to a file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to write. 
 - <b>`data`</b> (Any):  The content to write to the file. 
 - <b>`encoding`</b> (str, optional):  The file encoding. Defaults to JSON_ENCODING. 
 - <b>`indent`</b> (int, optional):  The line indent. Defaults to JSON_INDENT. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written to the file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import write_json_file

json_data = [
    {'date': '2023-09-10', 'value': 42},
    {'date': '2023-09-11', 'value': 24},
    {'date': '2023-09-12', 'value': 44},
]

write_json_file('path/to/file', json_data, encoding='UTF-8', indent=2)
``` 


---

<a href="../src/cerbernetix/toolbox/files/json_file.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `JSONFile`
Offers a simple API for reading and writing JSON files. 

The class binds a filename with a set of properties so that it can be opened in a consistent way. 

The read API reads all the content at once, and so do the write API too. 



**Attributes:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`binary`</b> (bool):  The type of file, say text. It must always be False. 
 - <b>`encoding`</b> (str, optional):  The file encoding. 
 - <b>`indent`</b> (int, optional):  The line indent. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import JSONFile

file = JSONFile("path/to/the/file.json", indent=4, encoding="UTF-8")

# write content to the file
file.write_file(json)

# open the file, then read its content
with file:
    json = file.read()

# write data to the file
with file(create=True):
    file.write(json)

# load the whole file, handling internally its opening
json = file.read_file()
``` 

<a href="../src/cerbernetix/toolbox/files/json_file.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    filename: str,
    create: bool = False,
    append: bool = False,
    read: bool = False,
    write: bool = False,
    encoding: str = 'utf-8',
    indent: int = 4,
    **kwargs
)
```

Creates a file manager for JSON files. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`create`</b> (bool, optional):  Expect to create the file. If it exists, it will be replaced. Defaults to False. 
 - <b>`append`</b> (bool, optional):  Expect to extend the file. Data will be added at the end. Defaults to False. 
 - <b>`read`</b> (bool, optional):  Expect to also read the file. Defaults to False. 
 - <b>`write`</b> (bool, optional):  Expect to also write to the file. Defaults to False. 
 - <b>`encoding`</b> (str, optional):  The file encoding. Defaults to JSON_ENCODING. 
 - <b>`indent`</b> (int, optional):  The line indent. Defaults to JSON_INDENT. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import JSONFile

# Create a file manager
file = JSONFile('path/to/filename')

# File can be opened directly as the manager is created
with JSONFile('path/to/filename') as file:
    data = file.read()

with JSONFile('path/to/filename', create=True) as file:
    file.write(data)

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

<a href="../src/cerbernetix/toolbox/files/json_file.py#L157"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read() → Any
```

Reads the content from the file. 

Note: the file must be opened upfront. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the file is not opened. 
 - <b>`OSError`</b>:  If the file cannot be read. 



**Returns:**
 
 - <b>`Any`</b>:  The data read from the file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import JSONFile

file = JSONFile('path/to/filename')

# When calling the read API, the whole JSON content is read from the file.
with file:
    json = file.read()
``` 

---

<a href="../src/cerbernetix/toolbox/files/json_file.py#L187"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write`

```python
write(data: Any) → int
```

Writes content to the file. 

Note: the file must be opened upfront. 



**Args:**
 
 - <b>`data`</b> (Any):  The content to write to the file. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the file is not opened. 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import JSONFile

file = JSONFile('path/to/filename')

# When calling the write API, the whole JSON is written to the file.
with file(create=True):
    file.write(json)
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
