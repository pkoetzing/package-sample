import logging
logger = logging.getLogger(__name__)

logger.info('module code')

# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).parents[1]))

# absolute import from repo-folder (PATH)
from package.subpackage import submodule_1, submodule_2

# alternate relative import:
# from .subpackage import submodule_1, submodule_2
# relative imports use the __name__ variable to determine
# the target modules position, and __name__ must have at least as many
# dots as you're trying to use in the import statement. Hence relative
# imports don't work in the top-level-script.


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
