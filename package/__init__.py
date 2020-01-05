import logging
logger = logging.getLogger(__name__)

logger.info('')

# convenience import:
from package.helppkg.helpmod import helper
# helper is added to the main package namespace and can be imported as
# from package import helper
