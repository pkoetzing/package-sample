import logging
logger = logging.getLogger(__name__)
logger.info('')

from package import helper


def func1():
    logger.info('')
    helper()
