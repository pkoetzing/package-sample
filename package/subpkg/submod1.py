import logging
logger = logging.getLogger(__name__)

logger.info('')

# absolute import:
# from package.helppkg.helpmod import helper

# relative import:
from ..helppkg.helpmod import helper


def func1():
    logger.info('')
    helper()
