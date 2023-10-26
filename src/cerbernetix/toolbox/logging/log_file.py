"""A custom logger that writes directly to a file.

Examples:
```python
from cerbernetix.toolbox.logging import LogFile

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
"""
from __future__ import annotations

import atexit
import logging

from cerbernetix.toolbox.files import delete_path
from cerbernetix.toolbox.logging.config import LOG_ENCODING

# The name of the logger, also used for the log events
LOG_FILE_NAME = "trace"

# The pattern for the log filename
LOG_FILE_PATTERN = "{name}.log"

# The default format for the log lines
LOG_FILE_LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"


class LogFile:
    """Offers a similar API to the Python builtin loggers for logging to a custom file.

    This is useful for keeping an audit log, aside the main log, or tracing a particular process
    without polluting the main log.

    Attributes:
        filename (str): The filename of the log file.
        level (int): The accepted log level.
        encoding (str): The file encoding.
        line_format (str): The format for the log events.
        name (str): The name of the logger, also used for the log events.

    Examples:
    ```python
    from cerbernetix.toolbox.logging import LogFile

    logger = LogFile()

    logger.info('The received value is %d', value)
    ```
    """

    def __init__(
        self,
        filename: str = None,
        level: int = logging.INFO,
        encoding: str = LOG_ENCODING,
        line_format: str = LOG_FILE_LOG_FORMAT,
        name: str = LOG_FILE_NAME,
    ) -> None:
        """Creates a file logger.

        Args:
            filename (str, optional): The filename of the log, if omitted the log name is used.
            Defaults to None.
            level (int, optional): The accepted log level. Defaults to logging.INFO.
            encoding (str, optional): The file encoding. Defaults to LOG_ENCODING.
            line_format (str, optional): The format for the log events. Defaults to
            LOG_FILE_LOG_FORMAT.
            name (str, optional): The name of the logger, also used for the log events. If the log
            filename is omitted, it will also be used for the filename. Defaults to LOG_FILE_NAME.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        # Create a log file at the current directory, named 'trace.log'
        logger = LogFile()

        # Create a log file at the given path
        logger = LogFile('path/to/file', logging.DEBUG)

        # Log something
        logger.debug('Start the process')
        logger.info('The received value is %d', value)
        logger.debug('Process completed')
        ```
        """
        self._filename = str(
            filename if filename is not None else LOG_FILE_PATTERN.format(name=name)
        )
        self._level = level
        self._encoding = encoding
        self._line_format = line_format
        self._name = name

        # The file handler will be created on the first call to .log()
        self._formatter = logging.Formatter(line_format)
        self._file_handler = None

        atexit.register(self.close)

    @property
    def filename(self) -> str:
        """The filename of the log.

        Returns:
            str: The filename of the log.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()


        print(logger.filename)
        ```
        """
        return self._filename

    @property
    def level(self) -> int:
        """The accepted log level.

        Returns:
            int: The accepted log level.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        print(logger.level)
        ```
        """
        return self._level

    @property
    def encoding(self) -> str:
        """The file encoding.

        Returns:
            str: The file encoding.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        print(logger.encoding)
        ```
        """
        return self._encoding

    @property
    def line_format(self) -> str:
        """The format for the log events.

        Returns:
            str: The format for the log events.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        print(logger.line_format)
        ```
        """
        return self._line_format

    @property
    def name(self) -> str:
        """The name of the logger.

        Returns:
            str: The name of the logger.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        print(logger.name)
        ```
        """
        return self._name

    def set_level(self, level: int) -> LogFile:
        """Sets the log level.

        Args:
            level (int): The new log level.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.set_level(logging.DEBUG)
        ```
        """
        self._level = level

        if self._file_handler:
            self._file_handler.setLevel(level)

        return self

    def set_format(self, line_format: str) -> LogFile:
        """Sets the log format.

        Args:
            line_format (str): The format for a log line.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.set_format('[%(asctime)s][%(levelname)s]: %(message)s')
        ```
        """
        self._line_format = line_format
        self._formatter = logging.Formatter(line_format)

        if self._file_handler:
            self._file_handler.setFormatter(self._formatter)

        return self

    def log(self, level: int, message: str, *args, **kwargs) -> LogFile:
        """Logs a message with the given level.

        Args:
            level (int): The log level of the message.
            message (str): The message to log. Format parameters are accepted.
            *args (tuple[Any]): Variable data to merge into the msg argument to obtain the
            event description.
            **kwargs (dict[str, Any]): Additional parameters for the event.
            The following is inspected :
            - pathname (str, optional): The full string path of the source file where the logging
            call was made.. Defaults to None.
            - lineno (int, optional): The line number in the source file where the logging call
            was made. Defaults to 0.
            - exc_info (tuple | None, optional) – An exception tuple with the current exception
            information, as returned by sys.exc_info(), or None if no exception information
            is available. Defaults to None.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.log(logging.INFO, 'The received value is %d', value)
        logger.log(logging.DEBUG, 'For debug purpose: %d given to %s', value, action)
        logger.log(logging.WARNING, 'Something bad happened, but the program can continue...')
        logger.log(logging.ERROR, 'An error occurred: %s', error)
        ```
        """
        if level < self._level:
            return

        pathname = None
        lineno = 0
        exc_info = None

        if "pathname" in kwargs:
            pathname = kwargs["pathname"]
            kwargs.pop("pathname")

        if "lineno" in kwargs:
            lineno = kwargs["lineno"]
            kwargs.pop("lineno")

        if "exc_info" in kwargs:
            exc_info = kwargs["exc_info"]
            kwargs.pop("exc_info")

        self.open()

        self._file_handler.emit(
            logging.LogRecord(
                name=self._name,
                level=level,
                pathname=pathname,
                lineno=lineno,
                msg=message,
                args=args,
                exc_info=exc_info,
                **kwargs,
            )
        )

        return self

    def info(self, message: str, *args, **kwargs) -> LogFile:
        """Logs an info message. Formatted string as for classical logging is supported.

        Args:
            message (str): The message to log.
            *args (tuple[Any]): Variable data to merge into the msg argument to obtain the
            event description.
            **kwargs (dict[str, Any]): Additional parameters for the event.
            The following is inspected :
            - pathname (str, optional): The full string path of the source file where the logging
            call was made.. Defaults to None.
            - lineno (int, optional): The line number in the source file where the logging call
            was made. Defaults to 0.
            - exc_info (tuple | None, optional) – An exception tuple with the current exception
            information, as returned by sys.exc_info(), or None if no exception information
            is available. Defaults to None.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.info('The received value is %d', value)
        ```
        """
        return self.log(logging.INFO, message, *args, **kwargs)

    def debug(self, message: str, *args, **kwargs) -> LogFile:
        """Logs a debug message. Formatted string as for classical logging is supported.

        Args:
            message (str): The message to log.
            *args (tuple[Any]): Variable data to merge into the msg argument to obtain the
            event description.
            **kwargs (dict[str, Any]): Additional parameters for the event.
            The following is inspected :
            - pathname (str, optional): The full string path of the source file where the logging
            call was made.. Defaults to None.
            - lineno (int, optional): The line number in the source file where the logging call
            was made. Defaults to 0.
            - exc_info (tuple | None, optional) – An exception tuple with the current exception
            information, as returned by sys.exc_info(), or None if no exception information
            is available. Defaults to None.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.debug('For debug purpose: %d given to %s', value, action)
        ```
        """
        return self.log(logging.DEBUG, message, *args, **kwargs)

    def warn(self, message: str, *args, **kwargs) -> LogFile:
        """Logs a warning message. Formatted string as for classical logging is supported.

        Args:
            message (str): The message to log.
            *args (tuple[Any]): Variable data to merge into the msg argument to obtain the
            event description.
            **kwargs (dict[str, Any]): Additional parameters for the event.
            The following is inspected :
            - pathname (str, optional): The full string path of the source file where the logging
            call was made.. Defaults to None.
            - lineno (int, optional): The line number in the source file where the logging call
            was made. Defaults to 0.
            - exc_info (tuple | None, optional) – An exception tuple with the current exception
            information, as returned by sys.exc_info(), or None if no exception information
            is available. Defaults to None.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.warn('Something bad happened, but the program can continue...')
        ```
        """
        return self.log(logging.WARNING, message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs) -> LogFile:
        """Logs an error message. Formatted string as for classical logging is supported.

        Args:
            message (str): The message to log.
            *args (tuple[Any]): Variable data to merge into the msg argument to obtain the
            event description.
            **kwargs (dict[str, Any]): Additional parameters for the event.
            The following is inspected :
            - pathname (str, optional): The full string path of the source file where the logging
            call was made.. Defaults to None.
            - lineno (int, optional): The line number in the source file where the logging call
            was made. Defaults to 0.
            - exc_info (tuple | None, optional) – An exception tuple with the current exception
            information, as returned by sys.exc_info(), or None if no exception information
            is available. Defaults to None.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.error('An error occurred: %s', error)
        ```
        """
        return self.log(logging.ERROR, message, *args, **kwargs)

    def open(self) -> LogFile:
        """Opens the log file.

        Note: If the file was already opened, it does nothing. This method is automatically called
        before logging anything. It is not need to call it explicitly.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.open() # not necessary since the .log() method will make sure the file is opened.

        logger.info('Something was done at %s', datetime.now())
        ```
        """
        if not self._file_handler:
            self._file_handler = logging.FileHandler(self._filename, encoding=self._encoding)
            self._file_handler.setLevel(self._level)
            self._file_handler.setFormatter(self._formatter)

        return self

    def close(self) -> LogFile:
        """Closes the log file.

        Note: If the file was already closed, it does nothing. This method is automatically called
        before exiting the program. It is not need to call it explicitly.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.info('Something was done at %s', datetime.now())

        logger.close() # not necessary since it will be called automatically upon exit.
        ```
        """
        if self._file_handler:
            self._file_handler.flush()
            self._file_handler.close()
            self._file_handler = None

        return self

    def delete(self) -> LogFile:
        """Deletes the log file.

        Returns:
            LogFile: Chains the instance.

        Examples:
        ```python
        from cerbernetix.toolbox.logging import LogFile

        logger = LogFile()

        logger.delete()
        ```
        """
        self.close()

        delete_path(self._filename)

        return self
