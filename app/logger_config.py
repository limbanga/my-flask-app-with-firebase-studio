import logging
from colorlog import ColoredFormatter
from logging.handlers import RotatingFileHandler

# Cấu hình logger cho Flask
def setup_logger(name="flask_app", level=logging.DEBUG, log_file="app.log"):
    # Formatter cho console (màu sắc)
    console_formatter = ColoredFormatter(
        "%(log_color)s[%(asctime)s] [%(levelname)-8s] [%(name)s] [%(filename)s:%(lineno)d]%(reset)s | %(message_log_color)s%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
        secondary_log_colors={
            "message": {
                "DEBUG": "cyan",
                "INFO": "white",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            }
        },
    )

    # Formatter cho file (không cần màu)
    file_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)-8s] [%(name)s] [%(filename)s:%(lineno)d] | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()  # Xoá handler cũ nếu có

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler có xoay file nếu quá lớn
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5MB
        backupCount=3,  # Lưu tối đa 3 file log cũ
        encoding="utf-8",
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger
