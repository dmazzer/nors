#!/usr/bin/env python3

""" 
nors_server.py:  Restful web server

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

from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

sys.path.append('../../remote/src/')
from norsutils.logmsgs.logger import Logger
logger = Logger('info')


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = connexion.App(__name__, specification_dir='./swagger/')
app.add_api('api.yaml', arguments={'title': 'NORS project rest API documentation'})

#    app = Flask(__name__)
#    app.debug = True
#app.config['SECRET_KEY'] = 'super-secret'


jwt = JWT(app, authenticate, identity)


@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

if __name__ == '__main__':

    app.run(port=8080, debug=True)


