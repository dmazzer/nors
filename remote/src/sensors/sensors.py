#!/usr/bin/env python2

""" 
sensors.py: Sensors controllers and readers 

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


class Nors_SensorService:
    def __init__(self):
        
        
    def work(self):
        # ZeroMQ Context
        context = zmq.Context()
        
        # Define the socket using the "Context"
        sock = context.socket(zmq.REP)
        sock.bind("ipc:///tmp/SensorCatalogService.pipe")
        
        # Run a simple "Echo" server
        while True:
            message = sock.recv()
            sock.send("Echo: " + message)
            print "Echo: " + message

if __name__ == '__main__':
    
    sys.path.append('../')
    from norsutils.logmsgs.logger import Logger
    logger = Logger()
    logger.log("GenericSensor started by command line")
    sensor = GenericSensor()
    sensor.sign_in()
else:
    from norsutils.logmsgs.logger import Logger
    logger = Logger()
    logger.log("GenericSensor started")
