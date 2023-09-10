<!-- markdownlint-disable -->

<a href="../toolbox/files/path.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.path`
A collection of utilities around file paths. 


---

<a href="../toolbox/files/path.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_module_path`

```python
get_module_path(name: str)
```

Gets the path to the given module. 



**Args:**
 
 - <b>`name`</b> (str):  The module for which get the path. 



**Returns:**
 
 - <b>`PurePath`</b>:  The path to the module. 


---

<a href="../toolbox/files/path.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_module_folder_path`

```python
get_module_folder_path(name: str)
```

Gets the path to the folder containing the given module. 



**Args:**
 
 - <b>`name`</b> (str):  The module for which get the path. 



**Returns:**
 
 - <b>`PurePath`</b>:  The path to the folder containing the given module. 


---

<a href="../toolbox/files/path.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_application_path`

```python
get_application_path(name: str) → PurePath
```

Gets the path to the application's root. 



**Args:**
 
 - <b>`name`</b> (str):  The main package of the application. 



**Returns:**
 
 - <b>`PurePath`</b>:  The path to the application's root. 


---

<a href="../toolbox/files/path.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_application_name`

```python
get_application_name(name: str) → str
```

Gets the name of the application, based on the root folder. 



**Args:**
 
 - <b>`name`</b> (str):  The main package of the application. 



**Returns:**
 
 - <b>`str`</b>:  The name of the application. 


---

<a href="../toolbox/files/path.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_file_path`

```python
get_file_path(relative: str, name: str) → PurePath
```

Gets a full path for a file inside the application. 



**Args:**
 
 - <b>`relative`</b> (str):  The internal path the file from the application's root. 
 - <b>`name`</b> (str):  The main package of the application. 



**Returns:**
 
 - <b>`PurePath`</b>:  The full path. 


---

<a href="../toolbox/files/path.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_file_path`

```python
create_file_path(path: str) → bool
```

Creates the parent path for a file. 

Note: exceptions are caught internally, the function will always return either with `True` in case of success, or `False` otherwise. 



**Args:**
 
 - <b>`path`</b> (str):  The path to the file. 



**Returns:**
 
 - <b>`bool`</b>:  `True` if the path has been created, `False` otherwise. 


---

<a href="../toolbox/files/path.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_path`

```python
delete_path(path: str) → bool
```

Deletes the file or the folder at the given path. 

If this is a folder, it must be empty. 

Note: exceptions are caught internally, the function will always return either with `True` in case of success, or `False` otherwise. 



**Args:**
 
 - <b>`path`</b> (str):  The path to the file or folder to delete. 



**Returns:**
 
 - <b>`bool`</b>:  `True` if the path has been deleted, `False` otherwise. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
