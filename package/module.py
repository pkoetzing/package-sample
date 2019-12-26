import logging
logger = logging.getLogger(__name__)

logger.info('module code')

# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).parents[1]))

# absolute import from repo-folder (PATH)
from package.subpkg import submod1, submod2

# alternate relative import:
# from .subpkg import submod1, submod2

# relative imports use the __name__ variable to determine
# the target modules position, and __name__ must have
# at least as many dots as you're trying to use in the
# import statement. Hence relative imports don't work
# in the top-level-script.


def function():
    print('------------------------+-------------'
          '+----------+----------------')
    logger.info('function code')
    submod1.func1()
    submod2.func2()


if __name__ == "__main__":
    # Use this main clause for code debugging (explorative testing)
    # during function development. Note that Python doesn't require a
    # main() function like Java or C and that in Python a function name
    # should be descriptive - which makes main() a rather bad choice.

    # Don't configure the root logger in module code,
    # since it can only be done once in a Python program!
    logging.basicConfig(
        level=logging.INFO,
        format='%(name)-23s : %(filename)-11s : '
            '%(funcName)-8s : %(message)s')
    print('\nNAME                    : FILE        '
        ': FUNCTION : MESSAGE\n'
        '------------------------+-------------'
        '+----------+---------------')
    logger.info('top-level')
    function()
