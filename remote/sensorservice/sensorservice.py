#!/usr/bin/env python2

""" 
sensorservice.py: Sensors controllers and readers 

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "GPL"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import zmq
import sys
from threading import Thread
import Queue
import time
import json
import signal

class Nors_SensorService:
    def __init__(self, pull_sensors_interval, LocalStorage_class):
        '''
        :param pull_sensors_interval: Time in seconds that registered sensors are pulled
        :param LocalStorage_class: LocalStorage object
        '''
        
        logger.log('SensorService started', 'info')
        
        self.q = Queue.Queue()
        self.pull_sensors_interval = int(pull_sensors_interval)
        self.ipc_sensor_catalog = "ipc:///tmp/SensorCatalogService.pipe"

        self.SensorCatalog()
        self.sensor_catalog_list = []
    
        self.SensorPulling()
        
        self.LocalStorage = LocalStorage_class
    
    def SensorPulling(self):
        t_pulling = Thread(target=self.SensorPullingWork, name='SensorPullingWork', args=(self.q, ) )
        t_pulling.daemon = True
        t_pulling.start()


    def SensorCatalog(self):
        t_catalog = Thread(target=self.SensorCatalogWork, name='SensorCatalogWork', args=(self.q, ) )
        t_catalog.daemon = True
        t_catalog.start()
        
    def check_sensor_service_message(self, message):
        if ('status' in message) and ('message' in message):
            if message['status'] == 'valid':
                return True
            
        return False
         
    def SensorPullingWork(self, q):
        '''
        SensorPullingWork - Consult sensorservice to get sensor data
        
        Note: With this implementation, all sensorservice are inquired, one by one, by the same thread.
        The ZMQ sockets are created as needed.
        Another architecture option may spawn one thread per sensor, so each thread may inquire the 
        sensor in independent time intervals. With independent threads may be more simple to 
        identify non responding sensorservice.
        
        Note 2: Feature missing: The platform may be more flexible if it allows the ZMQ socket 
        to be other than only IPC, i.e.: TCP. 
        '''
        while True:
            for sensor in self.sensor_catalog_list:
                logger.log('Pulling: ' + sensor['name'] + ' ' + sensor['sensor_id'])
            
                # ZeroMQ Context
                context = zmq.Context()
                 
                # Define the socket using the "Context"
                socket = context.socket(zmq.REQ)
                ipc_sensor_pulling = "ipc:///tmp/" + sensor['sensor_id'] + ".pipe"
                socket.setsockopt(zmq.LINGER, 0)
                socket.connect(ipc_sensor_pulling)
                poller = zmq.Poller()
                poller.register(socket, zmq.POLLIN)

#                 logger.log('Sensor data requesting...')
                socket.send_json({"query":"sensor_data"})
#                 logger.log('Sensor data requested.')

                if poller.poll(15*1000): # 15s timeout in milliseconds
                    sensor_service_message = json.loads(socket.recv_json())
                    if self.check_sensor_service_message(sensor_service_message) is True:
#                         sensor_data = socket.recv_json()
                        sensor_data = sensor_service_message['message']
                        logger.log(sensor['name'] + ': ' + str(sensor_data), 'debug')
                        try:
                            self.LocalStorage.store(sensor_data)
                        except Exception, e:
                            logger.log('There is a problem to save the sensor value to database.', 'error')
                            logger.log('Maybe a wrong or malformed JSON string...', 'error')
                            print str(e)
                            raise SystemExit
                    else:
                        logger.log('No sensor data', 'debug')
                else:
                    logger.log('Timeout sensor data request ' + sensor['name'] + ' ' + sensor['sensor_id'])
                    # TODO: After some timeouts, the problematic sensor must be deregistered
                

            time.sleep(self.pull_sensors_interval)
        
    def SensorCatalogWork(self, q):
        # ZeroMQ Context
        context = zmq.Context()
        
        # Define the socket using the "Context"
        socket = context.socket(zmq.REP)
        socket.bind(self.ipc_sensor_catalog)
        
        while True:
            message = json.loads(socket.recv_json())
            if self.SensorCatalogRegisterCheckID(message):
                self.ipc_sensor_pulling = "ipc:///tmp/" + message['sensor_id'] + ".pipe"
                socket.send_json({"result":"registered"})
            else:
                socket.send_json({"result":"denied"})
    
    def SensorCatalogRegisterCheckID(self, message):
        
        # in future, the ID may be checked to prevent duplicated sensorservice and dead sensorservice to be pulled.
        
        sensor_id = message['sensor_id']
        sensor_name = message['name']
        
        if sensor_id == '':
            return False
        else:
            logger.log('Registering ' + sensor_name + ' - '  + sensor_id)
            self.sensor_catalog_list.append(message)
            return True

if __name__ == '__main__':
    
    sys.path.append('../')
    from norsutils.logmsgs.logger import Logger
    logger = Logger('debug')
    logger.log("SensorService started by command line")
    sensor_service = Nors_SensorService()

    def do_exit(sig, stack):
        raise SystemExit('Exiting')
    
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGUSR1, do_exit)
    
    signal.pause()    

else:
    sys.path.append('../')
    from norsutils.logmsgs.logger import Logger
    logger = Logger('debug')



