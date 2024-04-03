<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.pickle_file`
A simple API for reading and writing pickle files. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import PickleFile, read_pickle_file, write_pickle_file

filename = 'path/to/file.pkl'
data = [
     {'date': '2023-09-10', 'value': 42},
     {'date': '2023-09-11', 'value': 24},
     {'date': '2023-09-12', 'value': 44},
]

# Create a Pickle file from the given data
write_pickle_file(filename, data)

# Read the Pickle data from an existing file
data = read_pickle_file(filename)

# Use a file manager
pickle = PickleFile(filename)

# Create a Pickle file from the given data
pickle.write_file(data)

# Read the Pickle data from an existing file
data = pickle.read_file()

# Write Pickle object by object
with pickle.open(create=True):
     for obj in data:
         pickle.write(obj)

# Read all objects from the Pickle
data = [obj for obj in pickle]

# Read the first object
with file:
     first = file.read()
``` 

**Global Variables**
---------------
- **PICKLE_READER_PARAMS**
- **PICKLE_WRITER_PARAMS**
- **FILE_OPEN_PARAMS**

---

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L343"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_pickle_file`

```python
read_pickle_file(filename: 'str', iterator: 'bool' = False, **kwargs) → Iterable
```

Loads a list of objects from a file. 

The returned value can be either a list (default) or an iterator (when the iterator parameter is True). 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to read. 
 - <b>`iterator`</b> (bool, optional):  When True, the function will return an iterator instead of a list. Defaults to False. 
 - <b>`fix_imports`</b> (bool, optional):  If fix_imports is true and protocol is less than 3, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2. Defaults to True. 
 - <b>`encoding`</b> (str, optional):  Tell pickle how to decode 8-bit string instances pickled by Python 2. The encoding can be ‘bytes’ to read these 8-bit string instances as bytes objects. Using encoding='latin1' is required for unpickling NumPy arrays and instances of datetime, date and time pickled by Python 2. Defaults to ‘ASCII’. 
 - <b>`errors`</b> (str, optional):  Tell pickle how to decode 8-bit string instances pickled by Python 2. Defaults to ‘strict’. 
 - <b>`buffers`</b> (optional):  If buffers is None (the default), then all data necessary for deserialization must be contained in the pickle stream. This means that the buffer_callback argument was None when a Pickler was instantiated (or when dump() or dumps() was called). If buffers is not None, it should be an iterable of buffer-enabled objects that is consumed each time the pickle stream references an out-of-band buffer view. Such buffers have been given in order to the buffer_callback of a Pickler object. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`Iterable`</b>:  The list of objects read from the file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import read_pickle_file

data = read_pickle_file('path/to/file')

# An iterator can be returned instead of a list
for obj in read_pickle_file('path/to/file', iterator=True):
    print(obj
``` 


---

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L393"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_pickle_file`

```python
write_pickle_file(filename: 'str', data: 'Iterable', **kwargs) → int
```

Writes a list of objects to a file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to write. 
 - <b>`data`</b> (Iterable):  The list of objects to write to the file. 
 - <b>`protocol`</b> (int, optional):  Tells the pickle writer to use the given protocol; supported protocols are 0 to HIGHEST_PROTOCOL. If a negative number is specified, HIGHEST_PROTOCOL is selected. Defaults is DEFAULT_PROTOCOL. 
 - <b>`fix_imports`</b> (bool, optional):  If fix_imports is true and protocol is less than 3, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2. Defaults to True. 
 - <b>`buffer_callback`</b> (optional):  If buffer_callback is None (the default), buffer views are serialized into file as part of the pickle stream. If buffer_callback is not None, then it can be called any number of times with a buffer view. If the callback returns a false value (such as None), the given buffer is out-of-band; otherwise the buffer is serialized in-band, i.e. inside the pickle stream. It is an error if buffer_callback is not None and protocol is None or smaller than 5. Defaults to None. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written to the file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import write_pickle_file

data = [
    {'date': '2023-09-10', 'value': 42},
    {'date': '2023-09-11', 'value': 24},
    {'date': '2023-09-12', 'value': 44},
]

write_pickle_file('path/to/file', data)
``` 


---

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PickleFile`
Offers a simple API for reading and writing pickle files. 

The class binds a filename with a set of properties so that it can be opened in a consistent way. 

The read API does not allow to size the data to read. However, it reads the file record by record. 



**Attributes:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`binary`</b> (bool):  The type of file, say binary. It must always be True. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import PickleFile

file = PickleFile("path/to/the/file")

# write some objects to the file
with file(create=True):
    file.write(users)
    file.write(profiles)

# read the records from the file
with file:
    users = file.read()
    profiles = file.read()

# gets the records in a list
data = [obj for obj in file]

# write records to the file
file.write_file(data)

# load the whole file, handling internally its opening
data = file.read_file()
``` 

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    filename: 'str',
    create: 'bool' = False,
    append: 'bool' = False,
    read: 'bool' = False,
    write: 'bool' = False,
    **kwargs
)
```

Creates a file manager for pickle files. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`create`</b> (bool, optional):  Expect to create the file. If it exists, it will be replaced. Defaults to False. 
 - <b>`append`</b> (bool, optional):  Expect to extend the file. Data will be added at the end. Defaults to False. 
 - <b>`read`</b> (bool, optional):  Expect to also read the file. Defaults to False. 
 - <b>`write`</b> (bool, optional):  Expect to also write to the file. Defaults to False. 
 - <b>`protocol`</b> (int, optional):  Tells the pickle writer to use the given protocol; supported protocols are 0 to HIGHEST_PROTOCOL. If a negative number is specified, HIGHEST_PROTOCOL is selected. When reading, the protocol version of the pickle is detected automatically. Defaults is DEFAULT_PROTOCOL. 
 - <b>`fix_imports`</b> (bool, optional):  If fix_imports is true and protocol is less than 3, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2. Defaults to True. 
 - <b>`encoding`</b> (str, optional):  Tell pickle how to decode 8-bit string instances pickled by Python 2. The encoding can be ‘bytes’ to read these 8-bit string instances as bytes objects. Using encoding='latin1' is required for unpickling NumPy arrays and instances of datetime, date and time pickled by Python 2. Defaults to ‘ASCII’. 
 - <b>`errors`</b> (str, optional):  Tell pickle how to decode 8-bit string instances pickled by Python 2. Defaults to ‘strict’. 
 - <b>`buffers`</b> (optional):  If buffers is None (the default), then all data necessary for deserialization must be contained in the pickle stream. This means that the buffer_callback argument was None when a Pickler was instantiated (or when dump() or dumps() was called). If buffers is not None, it should be an iterable of buffer-enabled objects that is consumed each time the pickle stream references an out-of-band buffer view. Such buffers have been given in order to the buffer_callback of a Pickler object. 
 - <b>`buffer_callback`</b> (optional):  If buffer_callback is None (the default), buffer views are serialized into file as part of the pickle stream. If buffer_callback is not None, then it can be called any number of times with a buffer view. If the callback returns a false value (such as None), the given buffer is out-of-band; otherwise the buffer is serialized in-band, i.e. inside the pickle stream. It is an error if buffer_callback is not None and protocol is None or smaller than 5. Defaults to None. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import PickleFile

# Create a file manager
file = PickleFile('path/to/filename')

# File can be opened directly as the manager is created
with PickleFile('path/to/filename') as file:
    data = file.read()

with PickleFile('path/to/filename', create=True) as file:
    file.write(data)

# A file manager can open explicitly a file
with file.open():
    obj = file.read()

with file.open(create=True):
    file.write(obj)

# It can also be opened implicitly
with file:
    obj = file.read()

# To create the file while opening implicitly
with file(create=True):
    file.write(obj)

# The file is also (re)opened when using the iteration protocol
data = [obj for obj in file]
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

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L275"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read() → object
```

Reads the next object from the file. 

Note: the file must be opened upfront. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the file is not opened. 
 - <b>`OSError`</b>:  If the file cannot be read. 



**Returns:**
 
 - <b>`object`</b>:  The object loaded from the file, or None if the file is at EOF. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import PickleFile

file = PickleFile('path/to/filename')

# When calling the read API, the next object in the file is read.
with file:
    obj1 = file.read()
    obj2 = file.read()

# The objects can also be read using the iteration protocol
data = [obj for obj in file]
``` 

---

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L206"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_file`

```python
read_file(iterator: 'bool' = False) → Iterable
```

Reads all the content from the file. 

The returned value can be either a list (default) or an iterator (when the iterator parameter is True). 

Note: If the file was already opened, it is first closed, then opened in read mode. 



**Args:**
 
 - <b>`iterator`</b> (bool, optional):  When True, the function will return an iterator instead of a list. Defaults to False. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`Iterable`</b>:  The content read from the file. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import PickleFile

file = PickleFile('path/to/filename')

# A file can be read all at once
data = file.read_file()

# An iterator can be returned instead of a list
for obj in file.read_file(iterator=True):
    print(obj)
``` 

---

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L310"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write`

```python
write(data: 'object') → int
```

Writes an object to the file. 

Note: the file must be opened upfront. 



**Args:**
 
 - <b>`data`</b> (object):  The object to write to the file. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the file is not opened. 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import PickleFile

file = PickleFile('path/to/filename')

# When calling the write API, an object is written to the file.
with file(create=True):
    file.write(object1)
    file.write(object2)
``` 

---

<a href="../src/cerbernetix/toolbox/files/pickle_file.py#L244"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write_file`

```python
write_file(data: 'Iterable') → int
```

Writes whole content to the file. 

Note: If the file was already opened, it is first closed, then opened in write mode. 



**Args:**
 
 - <b>`data`</b> (Iterable):  The content to write to the file. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written. 



**Examples:**
 ```python
from cerbernetix.toolbox.files import PickleFile

file = PickleFile('path/to/filename')

# A file can be written all at once
file.write_file(data)
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
