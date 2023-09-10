<!-- markdownlint-disable -->

<a href="../toolbox/files/file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.file`
A collection of utilities for accessing files. 


---

<a href="../toolbox/files/file.py#L4"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_file_mode`

```python
get_file_mode(
    create: bool = False,
    append: bool = False,
    read: bool = False,
    write: bool = False,
    binary: bool = False
) → str
```

Gets the file access mode given the expectations. 

The file access mode is defined by a string that contains flags for selecting the modes. More info at https://docs.python.org/3/library/functions.html#open 



**Args:**
 
 - <b>`create`</b> (bool, optional):  Expect to create the file. If it exists, it will be replaced. Defaults to False. 
 - <b>`append`</b> (bool, optional):  Expect to extend the file. Data will be added at the end. Defaults to False. 
 - <b>`read`</b> (bool, optional):  Expect to also read the file. Defaults to False. 
 - <b>`write`</b> (bool, optional):  Expect to also write to the file. Defaults to False. 
 - <b>`binary`</b> (bool, optional):  Expect the file to be binary (text otherwise). Defaults to False. 



**Returns:**
 
 - <b>`str`</b>:  A string representing the file access mode. 


---

<a href="../toolbox/files/file.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_file`

```python
read_file(
    filename: str,
    binary: bool = False,
    encoding: str = None,
    **kwargs
) → str | bytes
```

Reads a content from a file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to read. 
 - <b>`binary`</b> (bool, optional):  The type of file: binary (True) or text (False). Defaults to False. 
 - <b>`encoding`</b> (str, optional):  The file encoding, only needed for text files. Defaults to None. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`str|bytes`</b>:  The content read from the file. 


---

<a href="../toolbox/files/file.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_file`

```python
write_file(
    filename: str,
    data: str | bytes,
    binary: bool = False,
    encoding: str = None,
    **kwargs
) → int
```

Writes a content to a file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to write. 
 - <b>`data`</b> (str|bytes):  The content to write to the file. 
 - <b>`binary`</b> (bool, optional):  The type of file: binary (True) or text (False). Defaults to False. 
 - <b>`encoding`</b> (str, optional):  The file encoding, only needed for text files. Defaults to None. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written to the file. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
