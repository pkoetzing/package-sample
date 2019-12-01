import logging
logger = logging.getLogger(__name__)

logger.info('module code')

# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).parents[1]))

from package.subpackage import submodule_1, submodule_2


def main_function():
    logger.info('function code')
    submodule_1.function_1()
    submodule_2.function_2()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(name)-30s : %(filename)-14s : %(funcName)-13s : %(message)s')
    print('\nNAME                           : FILE           '
          ': FUNCTION      : MESSAGE         \n'
          '-------------------------------+----------------'
          '+---------------+-----------------')
    logger.info('top-level script')
    main_function()
