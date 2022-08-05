import logging


def get_logger(module_name):
    logger = logging.getLogger(module_name)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
