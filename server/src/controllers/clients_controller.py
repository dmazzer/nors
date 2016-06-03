""" 
clients_controller.py:  Restful resources - Clients context

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

def clients_client_id_get(client_id, limit) -> str:
    return ('Client_ID: ' + str(client_id))

def clients_client_id_post(client_id, sensor_data) -> str:
    return ('Client_ID: ' + str(client_id) +' | Sensor_Data: ' + str(sensor_data))

def clients_get(limit) -> str:
    return 'do some magic!'
