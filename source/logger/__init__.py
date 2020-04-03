import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from source import app
import logging.config


class Logger:
    def __init__(self):
        if not os.path.exists('logs'):
            os.mkdir('logs')
        # ToDo перенести в yaml
        log_file = os.path.join(os.getcwd(), 'cfg', 'log.config')
        logging.config.fileConfig(log_file)

        main_logger = logging.getLogger("Main")
        s_logger = logging.getLogger("S")

        main_logger.info("test")
        print("test 1")
        import time
        s_logger.warning("message 1")
        print("test 2")
        time.sleep(5)
        main_logger.exception("message 2")
        print("test 3")

        # app.logger.addHandler(file_handler)
        # app.logger.setLevel(logging.INFO)
        # app.logger.info('DataSite startup')
