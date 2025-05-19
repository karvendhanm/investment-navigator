import config
import logging

logging.basicConfig(
    level=config.LOGGER_LEVEL,
    format=config.LOGGER_FORMAT,
    filename=config.LOGGER_FILENAME,
    filemode=config.LOGGER_FILEMODE
)
logger = logging.getLogger(__name__)