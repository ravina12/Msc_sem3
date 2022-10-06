import pymysql

db = "school"
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Hinayadav18@',
                             database='cfl',
                             cursorclass=pymysql.cursors.DictCursor)


cursor = connection.cursor()
cursor.execute('SHOW TABLES;')

table_name = "students"


backup_dbname = db + '_backup2'
try:
	cursor.execute(f'CREATE DATABASE {backup_dbname}')
except:
	pass
cursor.execute(f'USE {backup_dbname}')

cursor.execute(f'CREATE TABLE school_entry_backup SELECT * FROM {db}.students')

	





