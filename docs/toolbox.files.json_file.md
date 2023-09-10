<!-- markdownlint-disable -->

<a href="../toolbox/files/json_file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.json_file`
A simple API for reading and writing JSON files. 

**Global Variables**
---------------
- **JSON_ENCODING**
- **JSON_INDENT**

---

<a href="../toolbox/files/json_file.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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


---

<a href="../toolbox/files/json_file.py#L149"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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


---

<a href="../toolbox/files/json_file.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
 ```
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

<a href="../toolbox/files/json_file.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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




---

<a href="../toolbox/files/json_file.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

---

<a href="../toolbox/files/json_file.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
