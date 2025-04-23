import logging

class Log():

    def __init__(self, log_name):
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(f"logs/{log_name}.log")
            formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def log_info(self, message):

        self.logger.info(message)

    def log_warning (self, message):

        self.logger.warning(message)