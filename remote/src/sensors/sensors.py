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
from threading import Thread
import Queue
import time
from uuid import uuid1
import json
import signal
import os

class Nors_SensorService:
    def __init__(self):
        
        logger.log('SensorService started')
        
        self.q = Queue.Queue()
        self.ipc_sensor_catalog = "ipc:///tmp/SensorCatalogService.pipe"

        self.SensorCatalog()
        self.sensor_catalog_list = []
    
        self.SensorPulling()
    
    def SensorPulling(self):
        t_pulling = Thread(target=self.SensorPullingWork, name='SensorPullingWork', args=(self.q, ) )
        t_pulling.daemon = True
        t_pulling.start()


    def SensorCatalog(self):
        t_catalog = Thread(target=self.SensorCatalogWork, name='SensorCatalogWork', args=(self.q, ) )
        t_catalog.daemon = True
        t_catalog.start()
        
    def SensorPullingWork(self, q):
        while True:
            for sensor in self.sensor_catalog_list:
                logger.log('Pulling :' + sensor['name'] + ' ' + sensor['sensor_id'])
            
                # ZeroMQ Context
                context = zmq.Context()
                 
                # Define the socket using the "Context"
                socket = context.socket(zmq.REQ)
                ipc_sensor_pulling = "ipc:///tmp/" + sensor['sensor_id'] + ".pipe"
                socket.setsockopt(zmq.LINGER, 0)
                socket.connect(ipc_sensor_pulling)
                poller = zmq.Poller()
                poller.register(socket, zmq.POLLIN)

                socket.send_json({"query":"sensor_data"})
            
                if poller.poll(10*1000): # 10s timeout in milliseconds
                    result = socket.recv_json()
                else:
                    logger.log('Timeout processing auth request' + sensor['name'] + ' ' + sensor['sensor_id'])
            
               
                
            time.sleep(5)
        
        

    def SensorCatalogWork(self, q):
        # ZeroMQ Context
        context = zmq.Context()
        
        # Define the socket using the "Context"
        socket = context.socket(zmq.REP)
        socket.bind(self.ipc_sensor_catalog)
        
        while True:
            message = json.loads(socket.recv_json())
            if self.SensorCatalogRegisterCheckID(message['name'], message['id']):
                logger.log('Registering ' + message['name'] + ' - '  + message['id'])
                self.ipc_sensor_pulling = "ipc:///tmp/" + message['id'] + ".pipe"
                socket.send_json({"result":"registered"})
            else:
                socket.send_json({"result":"registered"})
    
    def SensorCatalogRegisterCheckID(self, sensor_name, sensor_id):
        # in future, the ID may be checked to prevent duplicated sensors and dead sensors to be pulled.
        
        if sensor_id == '':
            return False
        else:
            sensor_append = {'name': sensor_name, 'sensor_id': sensor_id} 
            self.sensor_catalog_list.append(sensor_append)
            return True

if __name__ == '__main__':
    
    sys.path.append('../')
    from norsutils.logmsgs.logger import Logger
    logger = Logger()
    logger.log("SensorService started by command line")
    sensor_service = Nors_SensorService()

    def do_exit(sig, stack):
        raise SystemExit('Exiting')
    
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGUSR1, do_exit)
    
    signal.pause()    

