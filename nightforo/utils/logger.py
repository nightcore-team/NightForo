import logging
from dataclasses import dataclass
from typing import Optional

__all__ = ("LoggerData", "setup_logging")


@dataclass
class LoggerData:
    handler: Optional[logging.Handler] = None
    formatter: Optional[logging.Formatter] = None
    level: Optional[int] = None
    root: bool = True


def setup_logging(data: Optional[LoggerData]) -> None:
    level = data.level if data else None
    handler = data.handler if data else None
    formatter = data.formatter if data else None
    root = data.root if data else None

    if level is None:
        level = logging.INFO

    if handler is None:
        handler = logging.StreamHandler()

    if formatter is None:
        dt_fmt = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(
            "[{asctime}] [{levelname:<8}] {name}: {message}",
            dt_fmt,
            style="{",
        )

    if root:
        logger = logging.getLogger()
    else:
        library = __name__
        logger = logging.getLogger(library)

    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)
