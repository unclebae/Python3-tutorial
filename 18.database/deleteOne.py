import pymysql
import sys

boardId = int(input('enter board id if you want if you don''t want to delete enter the -1 : '))

if (boardId == -1):
    print('exit')
    sys.exit()

db = pymysql.connect('localhost', 'kido', '1212', 'boards')

cursor = db.cursor()

sql = """
    DELETE FROM BOARD WHERE id = '%d'""" % boardId

try:
	cursor.execute(sql)
	db.commit()
	print ('complete deleting board about id [%d]' % boardId)
except:
	db.rollback()

db.close()
