""" 
remote.py: Remote data model class

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

from collections import namedtuple
from enum import Enum
import json

from utils import EnumEncoder

class Remote():
    '''
    Remote class
    Remote data model where properties are organized inside a named tuple
    '''
     
    def __init__(self, remote_id, name, description, location):
        
        
        Model = namedtuple('Remote', 'remote_id name description location')
        
        self.remote = Model(remote_id = remote_id,
                            name = name,
                            description = description,
                            location = location)  
        
        
    def get(self):
        return self.remote._asdict()
    
    def get_json(self, indentation=None):
        return json.dumps(self.get(), encoding='UTF-8', cls=EnumEncoder, indent=indentation)
    
    def get_remote_property(self, remote_property):
        return self.get()[remote_property]
        