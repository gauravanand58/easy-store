# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:16:45 2019

@author: Gaurav
"""
from db import db

class StoreModel(db.Model):
     
     __tablename__ = 'stores'
     
     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(80))
     
     items = db.relationship('ItemModel', lazy = "dynamic") #it will not force to create objects of all the items present in all stores. We will use self.items.all() for getting the required items in json() method below
     
     def __init__(self, name):
          self.name = name
     
     def json(self):
          return {'name': self.name, 'items': [item.json() for item in self.items.all()]} # many calls to this method will slow down the processing since it will create objects of items in the 'stores' table
          
     @classmethod
     def find_by_name(cls, name):
          return StoreModel.query.filter_by(name = name).first()  # same as SELECT * from items WHERE name=name
          # the above is returning a ItemModel object
     
     def save_to_db(self):
          db.session.add(self) #creates a new object and calls __init__() with passed payload values and then  add to db 
          db.session.commit()
          
     def delete_from_db(self):
          db.session.delete(self)
          db.session.commit()