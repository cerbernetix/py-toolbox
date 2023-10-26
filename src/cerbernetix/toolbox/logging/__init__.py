"""The `logging` package provides several utilities for logging purpose.

It contains:
- Logging config:
    - `setup_file_logging()` - Setup file logging for the application.
    - `handle_uncaught_exceptions()` - Installs a collector for logging uncaught exceptions.
- File logger:
    - `LogFile(filename, ...)` - A custom logger that writes directly to a file.

Examples:
```python
import logging

from cerbernetix.toolbox.logging import LogFile, setup_file_logging, handle_uncaught_exceptions

logging.setup_file_logging('path/to/app.log')
logging.handle_uncaught_exceptions()

logger = logging.getLogger(__name__)

def action(log_file: LogFile) -> None:
    value = input('Please enter a value: ')

    log_file.info('The received value is %s', value)

def main() -> None:
    logger.info('Program started')

    log_file = logging.LogFile('path/to/action.log')

    action(log_file)

    logger.info('Program ended')

if __name__ == "__main__":
    main()
```
"""
from cerbernetix.toolbox.logging.config import (
    LOG_ENCODING,
    LOG_FILE,
    LOG_FORMAT,
    handle_uncaught_exceptions,
    setup_file_logging,
)
from cerbernetix.toolbox.logging.log_file import (
    LOG_FILE_LOG_FORMAT,
    LOG_FILE_NAME,
    LOG_FILE_PATTERN,
    LogFile,
)
