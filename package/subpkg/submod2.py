import logging
logger = logging.getLogger(__name__)
logger.info('')

# absolute import (recommended):
# from package.helppkg.helpmod import helper

# relative import (not recommended):
from ..helppkg.helpmod import helper


def func2():
    logger.info('')
    helper()
