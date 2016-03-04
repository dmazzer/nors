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

# import sys
import signal
from sensorservice.sensorservice import Nors_SensorService
from genericsensor.genericsensor import Nors_GenericSensor
from sensors import sensor_dht
from sensors import sensor_bmp180

if __name__ == '__main__':
    
    from norsutils.logmsgs.logger import Logger

    logger = Logger()
    logger.log("NORS - Noticia Remote Management and Supervisor")
    sensor_service = Nors_SensorService()
#     sensor_generic1 = Nors_GenericSensor(gs_name='fake1', gs_pull_interval=2, gs_read_fisical_interval=1)
#     sensor_generic1.SignIn()
#     sensor_generic2 = Nors_GenericSensor(gs_name='fake2', gs_pull_interval=2, gs_read_fisical_interval=1)
#     sensor_generic2.SignIn()
    
    sensor_dht = sensor_dht.RealSensor()
    sensor_bmp180 = sensor_bmp180.RealSensor()

    
    def do_exit(sig, stack):
        raise SystemExit('Exiting')
     
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGUSR1, do_exit)
     
    signal.pause()    
