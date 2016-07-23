import pymysql

db = pymysql.connect("localhost", "kido", "1212", "boards")

cursor = db.cursor()
sql = """
    INSERT INTO BOARD (TITLE, CONTENT, AUTHOR) 
	VALUES ('TEST post', 'Hello this is test post... I Like This post', 'kido')
"""

try :
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

db.close()
