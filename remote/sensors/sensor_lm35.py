#!/usr/bin/env python2

""" 
sensor_lm35.py: LM35 temperature sensor driver

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys
import signal
from random import randint

# sys.path.append('./genericsensor/')
# sys.path.append('./norsutils/')
# sys.path.append('../../')

from genericsensor.genericsensor import Nors_GenericSensor

from grovepi import *

from norsutils.logmsgs.logger import Logger

from nors_

logger = Logger('debug')
logger.log("SENSOR - Transmitter temp sensor", 'info')

class RealSensor(Nors_GenericSensor):
    def __init__(self):

        self.meanvalue = 0
        self.sensor_name = 'LM35-TX'
        
        super(RealSensor, self).__init__(
                                         gs_name = self.sensor_name,
                                         gs_id = '2e845abe-aa9c-11e6-8ff3-080027bc22fd',
                                         gs_description = 'Transmitter temp sensor', 
                                         gs_interface = None,
                                         gs_read_interval = 14)

        
    def SensorRead(self):
        v = randint(0,100)
        logger.log( "Value = " + str(v) , 'debug')     
        return {'value': v}

    def SensorDataProcessing(self,sensor_data):
        # y = (x[n] + x[n-1]) / 2
        self.meanvalue = (self.meanvalue + sensor_data['value']) / 2
        sensor_data['value'] = self.meanvalue
        return sensor_data
        

if __name__ == '__main__':
    sensor = RealSensor()


    def do_exit(sig, stack):
        raise SystemExit('Exiting')
    
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGUSR1, do_exit)
    
    signal.pause()    

    
