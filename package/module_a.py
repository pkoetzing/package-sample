import logging
logger = logging.getLogger(__name__)
logger.info('module code')

from package.subpackage_1 import module_1b

def function_a():
    logger.info('function code')

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(name)s - %(filename)s - %(funcName)s: %(message)s')
    logger.info('top-level script')