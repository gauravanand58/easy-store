# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:56:07 2019

@author: Gaurav
"""

from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from models.item_model import ItemModel

class Item(Resource):
     
     parser = reqparse.RequestParser()
     parser.add_argument('price',
                              required = True,
                              type = float,
                              help = "Can't be left blank")
     parser.add_argument('store_id',
                              required = True,
                              type = float,
                              help = "Can't be left blank")
     
     @jwt_required()
     def get(self, name):
          item = ItemModel.find_by_name(name)
          if item:
               return item.json()
          else:
               return {'message': 'Item does not exist'}
          
     def post(self, name):
          data = Item.parser.parse_args()    # 'Item.parser' because parser belongs to class and not to a particular object
          if ItemModel.find_by_name(name):
               return {'message': 'Item already exists'}
          item = ItemModel(name, data['price'], data['store_id'])
          try:
               item.save_to_db()
          except:
               return {"mesage": "Error while inserting item"}, 500 # internal server error
          return item.json(), 201
          
     def delete(self, name):
          item = ItemModel.find_by_name(name)
          if item:
               item.delete_from_db()
               return {'message': 'item deleted'}
          else:
               return {'message': 'item does not exist'}
     
     def put(self, name):
          
          data = Item.parser.parse_args()
          item = ItemModel.find_by_name(name)
          if item:
               item.price = data['price']
          else:
               item = ItemModel(name, data['price'], data['store_id'])
          item.save_to_db()
          return item.json()
     

class ItemList(Resource):
     def get(self):
          return {'items': [item.json() for item in ItemModel.query.all()]}