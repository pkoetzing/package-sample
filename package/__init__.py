import logging
logger = logging.getLogger(__name__)

logger.info('init code')

# convenience import:
from package.helppackage.helpmodule import helper
# helper is added to the main package namespace and can be imported as
# from package import helper
