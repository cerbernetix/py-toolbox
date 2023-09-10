<!-- markdownlint-disable -->

<a href="../toolbox/files/pickle_file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.pickle_file`
A simple API for reading and writing pickle files. 

**Global Variables**
---------------
- **PICKLE_READER_PARAMS**
- **PICKLE_WRITER_PARAMS**
- **FILE_OPEN_PARAMS**

---

<a href="../toolbox/files/pickle_file.py#L208"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_pickle_file`

```python
read_pickle_file(filename: 'str', **kwargs) → list
```

Loads a list of objects from a file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to read. 
 - <b>`fix_imports`</b> (bool, optional):  If fix_imports is true and protocol is less than 3, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2. Defaults to True. 
 - <b>`encoding`</b> (str, optional):  Tell pickle how to decode 8-bit string instances pickled by Python 2. The encoding can be ‘bytes’ to read these 8-bit string instances as bytes objects. Using encoding='latin1' is required for unpickling NumPy arrays and instances of datetime, date and time pickled by Python 2. Defaults to ‘ASCII’. 
 - <b>`errors`</b> (str, optional):  Tell pickle how to decode 8-bit string instances pickled by Python 2. Defaults to ‘strict’. 
 - <b>`buffers`</b> (optional):  If buffers is None (the default), then all data necessary for deserialization must be contained in the pickle stream. This means that the buffer_callback argument was None when a Pickler was instantiated (or when dump() or dumps() was called). If buffers is not None, it should be an iterable of buffer-enabled objects that is consumed each time the pickle stream references an out-of-band buffer view. Such buffers have been given in order to the buffer_callback of a Pickler object. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`list`</b>:  The list of objects read from the file. 


---

<a href="../toolbox/files/pickle_file.py#L242"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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


---

<a href="../toolbox/files/pickle_file.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PickleFile`
Offers a simple API for reading and writing pickle files. 

The class binds a filename with a set of properties so that it can be opened in a consistent way. 

The read API does not allow to size the data to read. However, it reads the file record by record. 



**Attributes:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`binary`</b> (bool):  The type of file, say binary. It must always be True. 



**Examples:**
 ```python
from toolbox.files import PickleFile

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

<a href="../toolbox/files/pickle_file.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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




---

<a href="../toolbox/files/pickle_file.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

---

<a href="../toolbox/files/pickle_file.py#L132"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_file`

```python
read_file() → list
```

Reads all the content from the file. 

Note: If the file was already opened, it is first closed, then opened in read mode. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`list`</b>:  The content read from the file. 

---

<a href="../toolbox/files/pickle_file.py#L187"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

---

<a href="../toolbox/files/pickle_file.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
