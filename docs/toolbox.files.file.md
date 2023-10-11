<!-- markdownlint-disable -->

<a href="../src/toolbox/files/file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.file`
A collection of utilities for accessing files. 



**Examples:**
 ```python
from toolbox.files import fetch_content, get_file_mode, read_file, read_zip_file, write_file

# get_file_mode() is used to build a file access mode.
# For example to create a text file:
with open('path/to/file', get_file_mode(create=True)) as file:
     file.write('some content')

# Create a text file
text = 'Some content'
write_file('path/to/file', text, encoding='UTF-8')

# Create a binary file
data = b'...'
write_file('path/to/file', data, binary=True)

# Load a text file
text = read_file('path/to/file', encoding='UTF-8')

# Load a binary file
data = read_file('path/to/file', binary=True)

# Fetch text content from a remote address
text = fetch_content("http://example.com/text")

# Fetch binary content from a remote address
data = fetch_content("http://example.com/data", binary=True)

# Considering the fetched content is a zip archive, extract the first file
content = read_zip_file(data)
``` 


---

<a href="../src/toolbox/files/file.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

The file access mode is defined by a string that contains flags for selecting the modes. For more info see [builtin open](https://docs.python.org/3/library/functions.html#open). 



**Args:**
 
 - <b>`create`</b> (bool, optional):  Expect to create the file. If it exists, it will be replaced. Defaults to False. 
 - <b>`append`</b> (bool, optional):  Expect to extend the file. Data will be added at the end. Defaults to False. 
 - <b>`read`</b> (bool, optional):  Expect to also read the file. Defaults to False. 
 - <b>`write`</b> (bool, optional):  Expect to also write to the file. Defaults to False. 
 - <b>`binary`</b> (bool, optional):  Expect the file to be binary (text otherwise). Defaults to False. 



**Returns:**
 
 - <b>`str`</b>:  A string representing the file access mode. 



**Examples:**
 ```python
from toolbox.files import get_file_mode

# Create a text file
with open('path/to/file', get_file_mode(create=True)) as file:
    file.write('some content')

# Append to a text file
with open('path/to/file', get_file_mode(append=True)) as file:
    file.write('some content')

# Read a text file
with open('path/to/file', get_file_mode()) as file:
    text = file.read()

# Create a binary file
with open('path/to/file', get_file_mode(create=True, binary=True)) as file:
    file.write(b'...')

# Read a binary file
with open('path/to/file', get_file_mode(binary=True)) as file:
    data = file.read()
``` 


---

<a href="../src/toolbox/files/file.py#L121"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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



**Examples:**
 ```python
from toolbox.files import read_file

# Load a text file
text = read_file('path/to/file', encoding='UTF-8')

# Load a binary file
data = read_file('path/to/file', binary=True)
``` 


---

<a href="../src/toolbox/files/file.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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



**Examples:**
 ```python
from toolbox.files import write_file

# Create a text file
text = 'Some content'
write_file('path/to/file', text, encoding='UTF-8')

# Create a binary file
data = b'...'
write_file('path/to/file', data, binary=True)
``` 


---

<a href="../src/toolbox/files/file.py#L208"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `fetch_content`

```python
fetch_content(
    url: str,
    binary: bool = False,
    timeout: int | tuple = (6, 30),
    **kwargs
) → str | bytes
```

Downloads content from the given URL. 

It uses an HTTP/GET request to fetch the remote data. 

Under the hood, it relies on requests to process the query. 



**Args:**
 
 - <b>`url`</b> (str):  The URL of the content to fetch. 
 - <b>`binary`</b> (bool):  Tells if the content is binary (True) or text (False). When True, the function will return a bytes sequence, otherwise it will return a string sequence. 
 - <b>`timeout`</b> (int | tuple):  The request timeout. Defaults to (6, 30). 
 - <b>`**kwargs`</b>:  Additional parameters for the GET request. For more info, see [requests/api](https://requests.readthedocs.io/en/latest/api/). 



**Raises:**
 
 - <b>`requests.RequestException`</b>:  There was an ambiguous exception that occurred while handling the request. 
 - <b>`requests.ConnectionError`</b>:  A Connection error occurred. 
 - <b>`requests.HTTPError`</b>:  An HTTP error occurred. 
 - <b>`requests.URLRequired`</b>:  A valid URL is required to make a request. 
 - <b>`requests.TooManyRedirects`</b>:  Too many redirects. 
 - <b>`requests.ConnectTimeout`</b>:  The request timed out while trying to connect to the remote server. Requests that produced this error are safe to retry. 
 - <b>`requests.ReadTimeout`</b>:  The server did not send any data in the allotted amount of time. 
 - <b>`requests.Timeout`</b>:  The request timed out. Catching this error will catch both ConnectTimeout and ReadTimeout errors. 



**Returns:**
 
 - <b>`str | bytes`</b>:  Returns a bytes buffer. 



**Examples:**
 ```python
from toolbox.files import fetch_content

# Fetch text content from a remote address
text = fetch_content("http://example.com/text")

# Fetch binary content from a remote address
data = fetch_content("http://example.com/data", binary=True)
``` 


---

<a href="../src/toolbox/files/file.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_zip_file`

```python
read_zip_file(buffer: bytes, filename: str = None, ext: str = None) → bytes
```

Extracts a file content from a Zip archive. 

If a filename is given, the corresponding file will be extracted from the archive. Otherwise, if a file extension is given, the first file having this extension in the archive will be extracted. If no filename nor extension is given, the fist available file is extracted. 



**Args:**
 
 - <b>`buffer`</b> (bytes):  A buffer of bytes representing the Zip archive. 
 - <b>`filename`</b> (str, optional):  The name of the file to extract from the zip. If omitted, and the extension is given, the first file having the extension will be selected. Otherwise, the first available file will be selected. Defaults to None. 
 - <b>`ext`</b> (str, optional):  The extension of the file to extract from the zip. This value is used if the filename is omitted, and in this case, the first file having the extension will be selected. Defaults to None. 



**Raises:**
 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`bytes`</b>:  The content of the file extracted from the Zip archive. 



**Examples:**
 ```python
from toolbox.files import read_zip

with open('path/to/file.zip', 'rb') as file:
    zip = file.read()

    # The first file in the archive will be extracted
    data = read_zip(zip)

    # The specified file will be extracted from the archive
    data = read_zip(zip, filename='foo')

    # The first file having the extension will be extracted from the archive
    data = read_zip(zip, ext='.txt')
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
