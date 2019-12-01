import logging
logger = logging.getLogger(__name__)

logger.info('module code')

from package.helppackage import helpmodule


def function_1():
    logger.info('function code')
    helpmodule.helper()
