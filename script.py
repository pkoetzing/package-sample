# 1. Setup logging
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)-23s [%(filename)-11s] %(funcName)s')

logger.info('')

# 2. Imports and declarations
from package.module import function

# 3. Code execution
function()
