import pymysql
import random

db = pymysql.connect('localhost', 'kido', '1212', 'boards')
cursor = db.cursor()

sql = """
    UPDATE BOARD SET content = '%s' WHERE id = 1 """ % (str(random.random()) + " are generaged.")

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

sql2 = """
    SELECT * FROM BOARD WHERE id = 1"""

try:
    cursor.execute(sql2)
    rows = cursor.fetchone()
    print(rows)
except:
	print("Error select modified data")


db.close()

