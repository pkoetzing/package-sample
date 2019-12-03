import logging
logger = logging.getLogger(__name__)

logger.info('module code')

from package.helppackage.helpmodule import helper


def function_1():
    logger.info('function code')
    helper()
