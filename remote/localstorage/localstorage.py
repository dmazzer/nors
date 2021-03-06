""" 
localstorage.py: LocalStorage - Local database storage and database management

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"


from norsutils.logmsgs.logger import Logger
from dao import Nors_LocalStorage_DAO

logger = Logger()


class Nors_LocalStorage():
    def __init__(self, config, sensor_streams_name='sensors_streams', sensor_info_name='sensors_info'):

        self.local_db_sensor_streams_name = sensor_streams_name
        self.local_db_sensor_info_name = sensor_info_name
        
        # TODO: self.max_db_entries is the max number of entries in DB, if exceeds 
        # new data is droped. The values 0 disable the entries limitation.
        # This feature is not yet implemented.
        self.max_db_entries = 10000

        # TODO: self.db_entries_ttl may be used to define the time to live
        # of each new entry, leaving to MongoDB automatically delete
        # documents after the time in seconds specified. This feature is
        # not yet implemented on DAO.    
        self.db_entries_ttl = 1 * (60 * 24)
        
        self.local_dao = Nors_LocalStorage_DAO(db=self.local_db_sensor_streams_name)

    def store(self, data_to_insert):
        result = self.local_dao.insert(self.local_db_sensor_streams_name, data_to_insert)
        return result 

    def get_first(self):
        result = self.local_dao.get_first_n_itens(self.local_db_sensor_streams_name, 1)
        return result
    
    def delete(self, item_id):
        result = self.local_dao.delete_by_id(self.local_db_sensor_streams_name, item_id)
        return result
    
    def __transfer_to_external_db(self):
        pass
    
    def __prepare_data_to_transfer(self):
        pass
    
    def __remove(self):
        pass
        
    
        
    