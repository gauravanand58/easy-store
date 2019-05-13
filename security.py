# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 23:47:25 2019

@author: Gaurav
"""

from models.user_model import UserModel

def authenticate(username, password):         # generates Token if authenticated  # this is called when user logs in
     user = UserModel.find_by_username(username)  #if not found then assign none
     if user and password == user.password:
          return user

def identity(payload):       #this is called when user request an endpoint which requires auth
     user_id = payload['identity']
     return UserModel.find_by_id(user_id)