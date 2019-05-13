# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 23:47:33 2019

@author: Gaurav
"""

from flask_restful import Resource, reqparse
from models.user_model import UserModel
import sqlite3
     
class UserRegister(Resource):
     
     parser = reqparse.RequestParser()  # parsing input data from json payload
     parser.add_argument('username',
                         required = True)
     parser.add_argument('password',
                         required = True)
     
     def post(self):
          data = UserRegister.parser.parse_args()
          if UserModel.find_by_username(data['username']):
               return {"message": "User already exists"}
          user = UserModel(data['username'], data['password']) #we can also write as UserModel[**data]
          user.save_to_db()
          return {"message": "User created"}, 201

















