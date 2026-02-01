import logging
from logging.handlers import RotatingFileHandler

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

sv_logger = logging.getLogger("sv_logger")
sv_logger.setLevel(logging.DEBUG)
sv_logger.propagate = False

if not sv_logger.handlers:
    file_handler = RotatingFileHandler(
        "sv_logger.log",
        maxBytes=10**6,
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    sv_logger.addHandler(file_handler)
    sv_logger.addHandler(console_handler)
