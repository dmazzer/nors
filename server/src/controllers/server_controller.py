""" 
server_controller.py:  Restful resources - Server context

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS Project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys

sys.path.append('../../../remote/src/')
from norsutils.logmsgs.logger import Logger
logger = Logger('info')

def server_info_get() -> str:
    return ('received GET on server info')
