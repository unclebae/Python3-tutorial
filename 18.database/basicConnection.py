#!/usr/local/bin/python3

import pymysql

# Oepn database connection
db = pymysql.connect("localhost", "kido", "1212", "boards")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()
