# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:43:31 2019

@author: Gaurav
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
     db.create_all()   # this will create all the tables using prototypes of the tables defined in each model

jwt = JWT(app, authenticate, identity)  #creates /auth endpoint for the app

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
     """when we import something from a file then that file's statements are 
     executed. so if we import something app into another file, it will run 
     our app also. when we run file as 'python app.py' then app gets a 
     variable __name__ with __main__ value so we are checking it here
     """
     from db import db
     db.init_app(app)
     app.run(port=5000)