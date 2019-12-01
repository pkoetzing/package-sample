import logging
logger = logging.getLogger(__name__)

logger.info('module code')

from package import helper


def function_2():
    logger.info('function code')
    helper()
