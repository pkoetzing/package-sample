import logging
logger = logging.getLogger(__name__)
logger.info('module code')

from package.subpackage_2.module_2a import function_2a

def function_1b():
    logger.info('function code')
    function_2a()