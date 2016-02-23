#!/usr/bin/env python2

""" 
genericsensor.py: Generic Sensor representation and registration application

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"
__status__ = "Development"

import zmq
import sys
from uuid import uuid1
import json
#from Logger import Logger

class Nors_GenericSensor:
    '''
    GenericSensor class, should be overloaded on specific sensors implementation
    '''
    
    def __init__(self):
        #self.logger = logger.Logger()

        logger.log('GenericSensor started')
        sensor_id = str(uuid1())
        logger.log('Sensor UUID: ' + sensor_id)
        self.sensor_properties = {'name': 'Generic Sensor',
                                  'id': sensor_id,
                                  'type': 'generic',
                                  'pull_interval': 1
                                  }

        
    def sign_in(self):
        # ZeroMQ Context
        context = zmq.Context()
        
        # Define the socket using the "Context"
        sock = context.socket(zmq.REQ)
        sock.connect("ipc:///tmp/SensorCatalogService.pipe")
        
        # Send a "message" using the socket
        sock.send(json.dumps(self.sensor_properties))
        print sock.recv()


if __name__ == '__main__':
    
    sys.path.append('../')
    from norsutils.logmsgs.logger import Logger
    logger = Logger()
    logger.log("GenericSensor started by command line")
    sensor = Nors_GenericSensor()
    sensor.sign_in()
else:
    from norsutils.logmsgs.logger import Logger
    logger = Logger()
    logger.log("GenericSensor started")

    
