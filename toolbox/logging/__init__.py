"""The `logging` package provides several utilities for logging purpose.

It contains:
- Logging config:
    - `setup_file_logging()` - Setup file logging for the application.
    - `handle_uncaught_exceptions()` - Installs a collector for logging uncaught exceptions.

Examples:
```python
import logging

from toolbox.logging import setup_file_logging, handle_uncaught_exceptions

logging.setup_file_logging('path/to/app.log')
logging.handle_uncaught_exceptions()

def main() -> None:
    ...

if __name__ == "__main__":
    main()
```
"""
from toolbox.logging.config import (
    LOG_ENCODING,
    LOG_FILE,
    LOG_FORMAT,
    handle_uncaught_exceptions,
    setup_file_logging,
)
