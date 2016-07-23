import pymysql

boardId = int(input('Please enter board id :'))

db = pymysql.connect('localhost', 'kido', '1212', 'boards')

cursor = db.cursor()
sql = "SELECT * FROM BOARD \
	WHERE ID = '%d'" % (boardId)
#print (sql)
try :
    cursor.execute(sql)
    result = cursor.fetchone()
    #print (result)

    if (result is not None):
		print ("Fetched Data : boardId=[%d], title=[%s], content=[%s], author=[%s], createAt=[%s], modifyAt=[%s]" % \
				(result[0], result[1], result[2], result[3], result[4], result[5]))
    else:
        print ('There is no data')
except:
    print("Error: unable to fetch data")

db.close()
