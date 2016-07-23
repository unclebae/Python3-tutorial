import pymysql

db = pymysql.connect('localhost', 'kido', '1212', 'boards')

cursor = db.cursor()
sql = "SELECT * FROM BOARD"

#print (sql)
try :
    cursor.execute(sql)
    results = cursor.fetchall()
    #print (results)

    for result in results:
		print ("Fetched Data : boardId=[%d], title=[%s], content=[%s], author=[%s], createAt=[%s], modifyAt=[%s]" % \
				(result[0], result[1], result[2], result[3], result[4], result[5]))
    else:
        print ('no more datas')
except:
    print("Error: unable to fetch data")

db.close()
