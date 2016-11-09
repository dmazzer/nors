""" 
sensor_service_model.py: Helper class to create a sensor service message

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

class SensorServiceModel():
    '''
    '''
    
    def __init__(self, message_status, message):
        self.message_status = message_status
        self.message = message
        
    def get(self):
        return({'status': self.message_status, 'message': self.message})
        
