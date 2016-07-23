import pymysql

title=input("Enter the Title ('title') :")
content=input("Enter the Contents ('content bla~ bla~') :")
author=input("Enter the author ('john') :")

db = pymysql.connect("localhost", "kido", "1212", "boards")

cursor = db.cursor()

sql = "INSERT INTO BOARD (TITLE, CONTENT, AUTHOR) \
    VALUES ('%s', '%s', '%s')" % \
	(title, content, author)

try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()
