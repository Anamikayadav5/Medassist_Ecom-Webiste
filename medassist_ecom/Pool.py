import pymysql as MySql
import pymysql.cursors

def ConnectionPooling():
    DB=MySql.connect(host='localhost',port=3306,user='root',passwd='12345',database='medassist_com',cursorclass=MySql.cursors.DictCursor)
    CMD=DB.cursor()
    return DB,CMD