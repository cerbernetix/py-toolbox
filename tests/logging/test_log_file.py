"""Test the file logger."""
import logging
import unittest
from unittest.mock import Mock, patch

from toolbox.logging import LOG_ENCODING, LOG_FILE_LOG_FORMAT, LOG_FILE_NAME, LogFile

# pylint: disable=protected-access


class TestLogFile(unittest.TestCase):
    """Test suite for the file logger."""

    @patch("atexit.register")
    @patch("logging.Formatter")
    def test_log_file_default(
        self,
        mock_format: Mock,
        mock_atexit: Mock,
    ):
        """Tests the construction of a log file with default parameters."""
        filename = "trace.log"

        logger = LogFile()

        self.assertEqual(logger.filename, filename)
        self.assertEqual(logger.level, logging.INFO)
        self.assertEqual(logger.encoding, LOG_ENCODING)
        self.assertEqual(logger.line_format, LOG_FILE_LOG_FORMAT)
        self.assertEqual(logger.name, LOG_FILE_NAME)

        mock_format.assert_called_once_with(LOG_FILE_LOG_FORMAT)
        mock_atexit.assert_called_once_with(logger.close)

    @patch("atexit.register")
    @patch("logging.Formatter")
    def test_log_file_custom(
        self,
        mock_format: Mock,
        mock_atexit: Mock,
    ):
        """Tests the construction of a log file with custom parameters."""
        filename = "foo.log"

        logger = LogFile(level=10, name="foo", encoding="ascii", line_format="bar")

        self.assertEqual(logger.filename, filename)
        self.assertEqual(logger.level, 10)
        self.assertEqual(logger.encoding, "ascii")
        self.assertEqual(logger.line_format, "bar")
        self.assertEqual(logger.name, "foo")

        mock_format.assert_called_once_with("bar")
        mock_atexit.assert_called_once_with(logger.close)

    @patch("atexit.register")
    @patch("logging.Formatter")
    def test_log_file_custom_filename(
        self,
        mock_format: Mock,
        mock_atexit: Mock,
    ):
        """Tests the construction of a log file with custom filename."""
        logger = LogFile(
            filename="foo.log",
            level=10,
            name="foo",
            encoding="ascii",
            line_format="bar",
        )

        self.assertEqual(logger.filename, "foo.log")
        self.assertEqual(logger.level, 10)
        self.assertEqual(logger.encoding, "ascii")
        self.assertEqual(logger.line_format, "bar")
        self.assertEqual(logger.name, "foo")

        mock_format.assert_called_once_with("bar")
        mock_atexit.assert_called_once_with(logger.close)

    @patch("atexit.register")
    def test_log_file_set_level(self, _):
        """Tests the set of log level."""

        logger = LogFile()

        logger.set_level(30)

        self.assertEqual(logger.level, 30)

        with patch("logging.FileHandler") as file_handler_mock:
            set_level_mock = Mock()
            file_handler_mock.return_value.setLevel = set_level_mock
            logger.open()
            set_level_mock.assert_called_once_with(30)

            logger.set_level(10)
            set_level_mock.assert_called_with(10)

    @patch("atexit.register")
    @patch("logging.Formatter")
    def test_log_file_set_format(self, mock_format: Mock, _):
        """Tests the set of log format."""

        logger = LogFile()

        logger.set_format("foo")

        self.assertEqual(logger.line_format, "foo")
        mock_format.assert_called_with("foo")

        with patch("logging.FileHandler") as file_handler_mock:
            set_formatter_mock = Mock()
            file_handler_mock.return_value.setFormatter = set_formatter_mock
            logger.open()
            set_formatter_mock.assert_called_once_with(logger._formatter)

            logger.set_format("bar")
            mock_format.assert_called_with("bar")
            set_formatter_mock.assert_called_with(logger._formatter)

    @patch("atexit.register")
    @patch("logging.FileHandler")
    @patch("logging.LogRecord")
    def test_log_file_log_logged(self, mock_record: Mock, mock_file_handler: Mock, _):
        """Tests the message is logged with the given level."""

        logger = LogFile()

        emit_mock = Mock()
        mock = Mock()
        mock.emit = emit_mock
        mock_file_handler.return_value = mock
        mock_record.return_value = "ok"

        logger.log(30, "foo bar", 1, 2)

        mock_record.assert_called_once_with(
            name=logger.name,
            level=30,
            pathname=None,
            lineno=0,
            msg="foo bar",
            args=(1, 2),
            exc_info=None,
        )
        emit_mock.assert_called_once_with("ok")

    @patch("atexit.register")
    @patch("logging.FileHandler")
    @patch("logging.LogRecord")
    def test_log_file_log_full_params(
        self, mock_record: Mock, mock_file_handler: Mock, _
    ):
        """Tests the message is logged with the given param."""

        logger = LogFile()

        emit_mock = Mock()
        mock = Mock()
        mock.emit = emit_mock
        mock_file_handler.return_value = mock
        mock_record.return_value = "ok"

        logger.log(
            30,
            "foo bar",
            1,
            2,
            pathname="foo",
            lineno=42,
            exc_info=("foo", "bar"),
            strace="bla bla",
        )

        mock_record.assert_called_once_with(
            name=logger.name,
            level=30,
            pathname="foo",
            lineno=42,
            msg="foo bar",
            args=(1, 2),
            exc_info=("foo", "bar"),
            strace="bla bla",
        )
        emit_mock.assert_called_once_with("ok")

    @patch("atexit.register")
    @patch("logging.FileHandler")
    @patch("logging.LogRecord")
    def test_log_file_log_not_logged(
        self, mock_record: Mock, mock_file_handler: Mock, _
    ):
        """Tests the message is not logged as the level is too low."""

        logger = LogFile()

        emit_mock = Mock()
        mock = Mock()
        mock.emit = emit_mock
        mock_file_handler.return_value = mock
        mock_record.return_value = "ok"

        logger.log(10, "foo bar", 1, 2)

        mock_record.assert_not_called()
        emit_mock.assert_not_called()

    @patch("atexit.register")
    @patch("logging.FileHandler")
    @patch("logging.LogRecord")
    def test_log_file_info(self, mock_record: Mock, mock_file_handler: Mock, _):
        """Tests the info message is logged."""

        logger = LogFile(level=0)

        emit_mock = Mock()
        mock = Mock()
        mock.emit = emit_mock
        mock_file_handler.return_value = mock
        mock_record.return_value = "ok"

        logger.info("foo bar bar", 1, 2, 3)

        mock_record.assert_called_once_with(
            name=logger.name,
            level=logging.INFO,
            pathname=None,
            lineno=0,
            msg="foo bar bar",
            args=(1, 2, 3),
            exc_info=None,
        )
        emit_mock.assert_called_once_with("ok")

    @patch("atexit.register")
    @patch("logging.FileHandler")
    @patch("logging.LogRecord")
    def test_log_file_debug(self, mock_record: Mock, mock_file_handler: Mock, _):
        """Tests the debug message is logged."""

        logger = LogFile(level=0)

        emit_mock = Mock()
        mock = Mock()
        mock.emit = emit_mock
        mock_file_handler.return_value = mock
        mock_record.return_value = "ok"

        logger.debug("foo bar bar", 1, 2, 3)

        mock_record.assert_called_once_with(
            name=logger.name,
            level=logging.DEBUG,
            pathname=None,
            lineno=0,
            msg="foo bar bar",
            args=(1, 2, 3),
            exc_info=None,
        )
        emit_mock.assert_called_once_with("ok")

    @patch("atexit.register")
    @patch("logging.FileHandler")
    @patch("logging.LogRecord")
    def test_log_file_warn(self, mock_record: Mock, mock_file_handler: Mock, _):
        """Tests the warning message is logged."""

        logger = LogFile(level=0)

        emit_mock = Mock()
        mock = Mock()
        mock.emit = emit_mock
        mock_file_handler.return_value = mock
        mock_record.return_value = "ok"

        logger.warn("foo bar bar", 1, 2, 3)

        mock_record.assert_called_once_with(
            name=logger.name,
            level=logging.WARNING,
            pathname=None,
            lineno=0,
            msg="foo bar bar",
            args=(1, 2, 3),
            exc_info=None,
        )
        emit_mock.assert_called_once_with("ok")

    @patch("atexit.register")
    @patch("logging.FileHandler")
    @patch("logging.LogRecord")
    def test_log_file_error(self, mock_record: Mock, mock_file_handler: Mock, _):
        """Tests the error message is logged."""

        logger = LogFile(level=0)

        emit_mock = Mock()
        mock = Mock()
        mock.emit = emit_mock
        mock_file_handler.return_value = mock
        mock_record.return_value = "ok"

        logger.error(
            "foo bar bar", 1, 2, 3, pathname="foo.bar", lineno=10, exc_info=("oops",)
        )

        mock_record.assert_called_once_with(
            name=logger.name,
            level=logging.ERROR,
            pathname="foo.bar",
            lineno=10,
            msg="foo bar bar",
            args=(1, 2, 3),
            exc_info=("oops",),
        )
        emit_mock.assert_called_once_with("ok")

    @patch("atexit.register")
    @patch("logging.FileHandler")
    def test_log_file_open(self, mock_file_handler: Mock, _):
        """Tests the log file is closed."""
        logger = LogFile()

        mock = Mock()
        mock.setLevel = Mock()
        mock.setFormatter = Mock()
        mock_file_handler.return_value = mock

        logger.open()
        logger.open()

        self.assertEqual(logger._file_handler, mock)
        mock_file_handler.assert_called_once()
        mock.setLevel.assert_called_once_with(logger.level)
        mock.setFormatter.assert_called_once_with(logger._formatter)

    @patch("atexit.register")
    @patch("logging.FileHandler")
    def test_log_file_close(self, mock_file_handler: Mock, _):
        """Tests the log file is closed."""
        logger = LogFile()

        mock = Mock()
        mock.flush = Mock()
        mock.close = Mock()
        mock_file_handler.return_value = mock

        logger.open()

        self.assertEqual(logger._file_handler, mock)

        logger.close()
        logger.close()

        self.assertIsNone(logger._file_handler)

        mock.flush.assert_called_once()
        mock.close.assert_called_once()

    @patch("atexit.register")
    @patch("logging.FileHandler")
    @patch("os.remove")
    def test_log_file_delete(self, mock_delete: Mock, mock_file_handler: Mock, _):
        """Tests the log file is erased."""
        filename = "trace.log"

        logger = LogFile()

        mock = Mock()
        mock.flush = Mock()
        mock.close = Mock()
        mock_file_handler.return_value = mock

        logger.open()

        self.assertEqual(logger._file_handler, mock)

        logger.delete()

        self.assertIsNone(logger._file_handler)

        mock.flush.assert_called_once()
        mock.close.assert_called_once()
        mock_delete.assert_called_once_with(filename)
