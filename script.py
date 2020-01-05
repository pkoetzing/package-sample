# Setup logging
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)-23s [%(filename)-11s] %(funcName)s')

logger.info('')

# Different ways to import and call the main function

import package
package.module.function()

# import package.module
# package.module.function()

# from package import module
# module.function()

# from package.module import function
# function()
