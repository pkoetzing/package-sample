# Setup logging
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)-23s : %(filename)-11s : '
           '%(funcName)-8s : %(message)s')
print('\nNAME                    : FILE        '
      ': FUNCTION : MESSAGE\n'
      '------------------------+-------------'
      '+----------+----------------')
logger.info('top-level')


# Track changes in namespace
SCOPE = dir()
diff = lambda x: sorted(
    list(set(x) - set(SCOPE)
         - set(['SCOPE', 'diff', '__path__'])))


# Different ways to import and call the main function

# import package
# logger.info(f'local scope: {diff(dir())}')
# logger.info(f'package scope: {diff(dir(package))}')
# package.module.main()

import package.module
logger.info(f'local scope >\n\t{diff(dir())}')
logger.info(f'package scope >\n\t{diff(dir(package))}')
package.module.main()

# from package import module
# logger.info(f'local scope: {diff(dir())}')
# logger.info(f'module scope: {diff(dir(module))}')
# module.main()

# from package.module import main_function
# logger.info(f'local scope: {diff(dir())}')
# main()
