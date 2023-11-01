"""
Module to define logging handlers and logers 
"""
import logging
from logging import Logger


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    # Customize handlers and loggers

    # handlers = {},

    # loggers = {},
)

def get_logger() -> Logger:
    return logging.getLogger(__name__)
