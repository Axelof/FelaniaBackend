import logging
import sys
from types import FrameType
from typing import cast

from loguru import logger

from settings import settings

LEVEL = logging.DEBUG if settings.debug else logging.INFO
DATETIME_FORMAT = "DD.MM.YYYY HH^mm (ss)"
LOGGER_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<red><level>{level: <8}</level></red> | "
    "<cyan>{name}:{function}:{line}</cyan> | "
    "{message}"
)


def configure_logging():
    logger.remove()
    logger.add(
        sys.stdout,
        level=LEVEL,
        format=LOGGER_FORMAT,
        backtrace=False,
    )

    # configure file logging
    logger.add(
        f"logs/{{time:{DATETIME_FORMAT}}}.log",
        rotation="4 MB",
        compression="zip",
    )

    # handle all default logging
    logging.basicConfig(
        level=logging.INFO,
        force=True,
        handlers=[InterceptHandler()],
    )

    # configure default logging
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        frame, depth = logging.currentframe(), 0

        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame, depth = cast(FrameType, frame.f_back), depth + 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )
