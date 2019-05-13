# -*- coding: utf-8 -*-
"""
Created on Fri May  3 23:50:39 2019

@author: Gaurav
"""
# We can delete this file and use SQLAlchemy to ccreate tables for us by scripting in app.py 


import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

delete_if_user_table_exists = 'DROP TABLE IF EXISTS users;'
cursor.execute(delete_if_user_table_exists)

delete_if_item_table_exists = 'DROP TABLE IF EXISTS items;'
cursor.execute(delete_if_item_table_exists)

create_users_query = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_users_query)

create_items_query = "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_items_query)

connection.commit()
connection.close()