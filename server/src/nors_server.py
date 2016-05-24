#!/usr/bin/env python3

""" 
nors_server.py:  

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS Project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"


    #TODO:
    #
    # create cloud DB
    # connect to DB
    # receive DB connection address and name as a paramether
    # ... 


import connexion
import sys

sys.path.append('../../remote/src/')
from norsutils.logmsgs.logger import Logger
logger = Logger('info')

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('api.yaml', arguments={'title': 'NORS project rest API documentation'})
    app.run(port=8080, debug=True)
