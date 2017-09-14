#!/usr/bin/env python2

""" 
sensor_reed.py: Magnetic reed switch sensor

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2017, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import signal
from time import time

from genericsensor.genericsensor import Nors_GenericSensor

from grovepi import *

from norsutils.logmsgs.logger import Logger

logger = Logger('debug')
logger.log("SENSOR - Reed switch", 'info')

class RealSensor(Nors_GenericSensor):
    def __init__(self):

        self.sensor_name = 'REED'
        
        self.magnetic_switch_port = 3
        grovepi.pinMode(self.magnetic_switch_port,"INPUT")

        self.read_interval = 10
        self.timeout_to_send_data_if_idle = 5*60 # minutes
        self.counter_send_data_if_idle_reset = (self.timeout_to_send_data_if_idle / self.read_interval)
        self.counter_send_data_if_idle = self.counter_send_data_if_idle_reset
        print('counter reset is: ' + self.counter_send_data_if_idle_reset)

        self.reed_state = {'open': 1, 'closed':0}
        self.reed_last_state = self.reed_state['open']

        super(RealSensor, self).__init__(
                                         gs_name = self.sensor_name,
                                         gs_id = '40c9e2d8-98ef-11e7-8ac6-0022fb74da72',
                                         gs_description = 'Reed switch', 
                                         gs_interface = None,
                                         gs_read_interval = self.read_interval)
        
    def SensorRead(self):
        try:
            v = grovepi.digitalRead(self.magnetic_switch_port)
            logger.log( "Value = " + str(v) , 'debug')     
        except (IOError,TypeError) as e:
            logger.log("Error reading sensor " + self.sensor_name, 'error')
            return None
        return {'value': v}

    def SensorDataProcessing(self,sensor_data):
        # if there is no event, no data will be sent.
        if self.IdleCheck():
            return sensor_data
        if sensor_data == self.reed_last_state:
            return None
        else:
            self.IdleCheck(reset=True)
            return sensor_data
        
        sensor_data['value'] = 0
        return sensor_data
    
    def IdleCheck(self, reset=False):
        print('counter is: ' + self.counter_send_data_if_idle)
        if reset == True:
            self.counter_send_data_if_idle = self.counter_send_data_if_idle_reset
            return False

        if self.counter_send_data_if_idle == 0:
            self.counter_send_data_if_idle = self.counter_send_data_if_idle_reset
            return True
        else:        
            self.counter_send_data_if_idle -= 1
            return False



if __name__ == '__main__':
    sensor = RealSensor()


    def do_exit(sig, stack):
        raise SystemExit('Exiting')
    
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGUSR1, do_exit)
    
    signal.pause()    

    
