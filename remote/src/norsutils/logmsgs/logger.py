import logging

class Logger():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s %(threadName)s] %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')
    def log(self, msg):
        self.logger.info(msg)