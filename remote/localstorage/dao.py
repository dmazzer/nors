""" 
dao.py: MongoDB DAO

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"


import sys

sys.path.append('../')
from norsutils.logmsgs.logger import Logger

from pymongo import MongoClient
from pymongo.errors import AutoReconnect
import pymongo
from bson.objectid import ObjectId

logger = Logger()

def autoreconnect_retry(retries=3):

    """
    Decorator for connection retrial in mongoDB
    """
    
    def autoreconnect_retry_decorator(fn):
        def db_op_wrapper(*args, **kwargs):
            tries = 0
    
            while tries < retries:
                try:
                    return fn(*args, **kwargs)
    
                except AutoReconnect:
                    tries += 1
    
                raise Exception("No luck even after %d retries" % retries)
    
        return db_op_wrapper
    return autoreconnect_retry_decorator

class Nors_LocalStorage_DAO:
    def __init__(self, db='nors_local_storage', db_address='mongodb://localhost:27017/'):
        
        logger.log('connecting to LOCAL database ' + db + ' at ' + db_address)
        try:
            self.db_connection = MongoClient(db_address)
            self.db_client =  self.db_connection[str(db)]
            self.db_name = db
        except pymongo.errors.ConnectionFailure:
            logger.log('Could not connect to sever ' + db_address)
            raise

        logger.log('done connecting to database')

    def insert(self, CollectionName, jsonstring):
        collection = self.db_client[str(CollectionName)]
        post_id = collection.insert(jsonstring)
        return post_id

    def update(self, CollectionName, SearchDict, FieldsJson):
        collection = self.db_client[str(CollectionName)]
        post_id = collection.update_one(SearchDict, { "$set": FieldsJson})
        return post_id
    
    def get_itens_from_date(self, CollectionName, startDate, numberOfItems):
        '''
        Returns numberOfItems items from the database, if available data is less than numberOfItems, no data is returned. 
        '''
        searchd = {"date": {"$gt":str(startDate)}}
        return self.find(CollectionName, SearchString=searchd, SearchLimit=numberOfItems)

    def get_first_n_itens(self, CollectionName, numberOfItems):
        '''
        Returns numberOfItems items from the database, if available data is less than numberOfItems, no data is returned. 
        '''
        return self.find(CollectionName, SearchLimit=numberOfItems, Sort=[('_id', pymongo.ASCENDING), ])

    def get_item_by_id(self, CollectionName, item_id):
        '''
        Returns item from the database with id=item_id. 
        '''
        return self.find(CollectionName, SearchString={"_id": ObjectId(item_id)}, SearchLimit=1)
    
    def find(self, CollectionName, SearchString=None, SearchLimit=0, Sort=None):
        
        if (Sort is None) and (SearchString is not None):
            return self._find_string(CollectionName, SearchString, SearchLimit)
        
        elif (Sort is not None) and (SearchString is None):
            return self._find_with_sort_without_string(CollectionName, SearchLimit, Sort)
        
        else:
            return None
    
    def _find_with_sort_without_string(self, CollectionName, SearchLimit, Sort=None):
        collection = self.db_client[str(CollectionName)]
        collected = collection.find().limit(SearchLimit).sort(Sort)
        r = []
        for i in collected:
            r.append(i)
        return r

    def _find_string(self, CollectionName, SearchString, SearchLimit):
        collection = self.db_client[str(CollectionName)]
        collected = collection.find(SearchString).limit(SearchLimit)
        r = []
        for i in collected:
            r.append(i)
        return r
    
    def delete_by_id(self, CollectionName, item_id):
        collection = self.db_client[str(CollectionName)]
        result = collection.delete_one({'_id': ObjectId(item_id)})
        return result.deleted_count
    
    def dropCollection(self, CollectionName):
        collection = self.db_client[str(CollectionName)]
        collection.drop()
        
    def dropDB(self):
        database = self.db_connection.drop_database(self.db_name)
           
         
