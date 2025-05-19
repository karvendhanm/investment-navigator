import logging

# logger
LOGGER_FILENAME = 'app.log'
LOGGER_FILEMODE = 'a' # 'a' for append, 'w' for overwrite on each run
LOGGER_LEVEL = logging.ERROR
LOGGER_FORMAT = '%(asctime)s - %(levelname)s - %(module)s:%(funcName)s:%(lineno)d - %(message)s'