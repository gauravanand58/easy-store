# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:06:25 2019

@author: Gaurav
"""

from flask_restful import Resource
from models.store_model import StoreModel

class Store(Resource):
     def get(self, name):
          store = StoreModel.find_by_name(name)
          if store:
               return store.json()
          else:
               return {'message': 'store not found'}
     
     def post(self, name):
          if StoreModel.find_by_name(name):
               return {'message': 'store already present'}
          else:
               store = StoreModel(name)
               store.save_to_db()
               return store.json()
     
     def delete(self, name):
          store = StoreModel.find_by_name(name)
          if store:
               store.delete_from_db()
          else:
               return {'message': 'store not found'}
          return {'message': 'store deleted'}


class StoreList(Resource):
     def get(self):
          return {'stores': [store.json() for store in StoreModel.query.all()]}