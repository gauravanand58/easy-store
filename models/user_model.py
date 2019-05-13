# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:10:34 2019

@author: Gaurav
"""

from db import db

class UserModel(db.Model):
     
     __tablename__ = 'users'
     
     id = db.Column(db.Integer, primary_key = True)
     username = db.Column(db.String(80))
     password = db.Column(db.String(80))
     
     def __init__(self, username, password): # no need to specify id in the constructor, it will auto added by SQLAlchemy coz of its a primary key
          self.username = username
          self.password = password
     
     @classmethod
     def find_by_username(cls, username):
          return UserModel.query.filter_by(username = username).first()
     
     @classmethod
     def find_by_id(cls, _id):    #cls used in place of self coz nowhere we need to use self in code
          return UserModel.query.filter_by(id = _id).first()
     
     def save_to_db(self):
          db.session.add(self)
          db.session.commit()