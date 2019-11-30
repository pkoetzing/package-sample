import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
      level=logging.INFO,
      format='%(name)-30s : %(filename)-12s : %(funcName)-12s : %(message)s')

logger.info('top-level script')
from package import module_a

module_a.function_a()