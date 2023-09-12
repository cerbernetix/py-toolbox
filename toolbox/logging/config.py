"""A collection of utilities for logging purpose.

Examples:
```python
from toolbox.logging import setup_file_logging, handle_uncaught_exceptions

setup_file_logging('path/to/file.log')
handle_uncaught_exceptions()

def main() -> None:
    ...

if __name__ == "__main__":
    main()
```
"""
import logging
import sys

# The name for the log file
LOG_FILE = "app.log"

# The default format for the log lines
LOG_FORMAT = "%(asctime)s %(levelname)s:%(name)s:%(message)s"

# The default data encoding for log files
LOG_ENCODING = "utf-8"


def setup_file_logging(
    filename: str = LOG_FILE,
    level: int = logging.INFO,
    encoding: str = LOG_ENCODING,
    log_format: str = LOG_FORMAT,
    **kwargs,
) -> None:
    """Setup the application log to a file logger.

    By default, a file will be created in the current working directory, named 'app.log'.

    Args:
        filename (str, optional): The filename of the log file. Defaults to LOG_FILE.
        level (int, optional): The log level to accept. Defaults to logging.INFO.
        encoding (str, optional): The file encoding. Defaults to LOG_ENCODING.
        log_format (str, optional): The format for each log event. Defaults to LOG_FORMAT.

    Examples:
    ```python
    from toolbox.logging import setup_file_logging

    setup_file_logging('path/to/file.log')
    ```
    """
    logging.basicConfig(
        filename=filename,
        level=level,
        encoding=encoding,
        format=log_format,
        **kwargs,
    )


def handle_uncaught_exceptions() -> None:
    """Installs a collector for logging uncaught exceptions.

    When an exception is not handled in the code, it will be logged with the message:
    'Uncaught exception: <exception message>'.

    Examples:
    ```python
    from toolbox.logging import handle_uncaught_exceptions

    handle_uncaught_exceptions()

    def main() -> None:
        ...

    if __name__ == "__main__":
        main()
    ```
    """

    def error_handler(self, value, traceback):
        logging.exception("Uncaught exception: %s", value)
        sys.__excepthook__(self, value, traceback)

    sys.excepthook = error_handler
