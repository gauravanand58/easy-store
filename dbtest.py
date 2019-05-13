# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:59:56 2019

@author: Gaurav
"""

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

users = [(1, 'bob', 'asdf'),
         (2, 'jose', 'qwer')]

create_table = "CREATE TABLE users(id int, username text, password text)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES(?,?,?)"
cursor.executemany(insert_query, users)

for row in cursor.execute("SELECT * FROM users"):
     print(row)

connection.commit()
connection.close()