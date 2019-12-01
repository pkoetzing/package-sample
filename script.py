# 1. Setup Logging
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)-30s : %(filename)-14s : %(funcName)-13s : %(message)s')
print('\nNAME                           : FILE           '
      ': FUNCTION      : MESSAGE         \n'
      '-------------------------------+----------------'
      '+---------------+-----------------')
logger.info('top-level script')

# 2. Do all imports and function declarations
from package import module

# 3. Execute the code
module.main_function()
