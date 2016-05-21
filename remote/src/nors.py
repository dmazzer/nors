#!/usr/bin/env python2

""" 
nors.py: Noticia Remote Management and Supervisor

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "GPL"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import signal
from sensorservice.sensorservice import Nors_SensorService
from localstorage.localstorage import Nors_LocalStorage
from sensors import sensor_dht
from sensors import sensor_bmp180

from uuid import uuid1
from config.config import Nors_Configuration

from norsutils.logmsgs.logger import Logger

logger = Logger('debug')

def load_configuration():
    config = Nors_Configuration()
    server_ip = config.ReadConfig('server', 'ip')
    server_port = config.ReadConfig('server', 'port')
    
    client_auth = config.ReadConfig('client', 'auth')
    client_id = config.ReadConfig('client', 'id')
    
    if client_id == None:
        client_id = str(uuid1())
        logger.log('Generating UUID: ' + client_id, level='info')
        config.SaveConfig('client', 'id', client_id)

    logger.log('Server IP  : ' + server_ip, 'debug')
    logger.log('Server Port: ' + server_port, 'debug')
    logger.log('Client ID  : ' + client_id, 'debug')
    logger.log('Client Auth: ' + client_auth, 'debug')
    
    return config


if __name__ == '__main__':
    
    logger.log("NORS - Noticia Remote Management and Supervisor", 'info')
    
    # Load configuration parameters 
    config = load_configuration()
    
    # Initialize local services
    local_storage = Nors_LocalStorage(CollectionName='nors_local_storage')
    sensor_service = Nors_SensorService(local_storage)
#     sensor_generic1 = Nors_GenericSensor(gs_name='fake1', gs_pull_interval=2, gs_read_fisical_interval=1)
#     sensor_generic1.SignIn()
#     sensor_generic2 = Nors_GenericSensor(gs_name='fake2', gs_pull_interval=2, gs_read_fisical_interval=1)
#     sensor_generic2.SignIn()
    
    # Initialize real sensors services
    sensor_dht = sensor_dht.RealSensor()
    sensor_bmp180 = sensor_bmp180.RealSensor()

    # Initialize connection with remote server
    # TODO: ada
    

    # Hold forever
    def do_exit(sig, stack):
        raise SystemExit('Exiting')
     
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGUSR1, do_exit)
     
    signal.pause()    
