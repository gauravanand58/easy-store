# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:16:45 2019

@author: Gaurav
"""
from db import db

class ItemModel(db.Model):
     
     __tablename__ = 'items'
     
     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(80))
     price = db.Column(db.Float(precision = 2))
     
     store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
     store = db.relationship('StoreModel')
     
     def __init__(self, name, price, store_id):
          self.name = name
          self.price = price
          self.store_id = store_id
     
     def json(self):
          return {'name': self.name, 'price': self.price, 'store_id': self.store_id}
          
     @classmethod
     def find_by_name(cls, name):
          return ItemModel.query.filter_by(name = name).first()  # same as SELECT * from items WHERE name=name
          # the above is returning a ItemModel object
     
     def save_to_db(self):
          db.session.add(self) #creates a new object and calls __init__() with passed payload values and then  add to db 
          db.session.commit()
          
     def delete_from_db(self):
          db.session.delete(self)
          db.session.commit()