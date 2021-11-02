import mysql.connector
import os

user = os.environ['USER']
base = os.environ.get('DB_NAME')
passw = os.environ.get('DB_PASS')

#print(user,base,passw)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=passw,
  database=base
)

mycursor = mydb.cursor()

sql = "UPDATE employees SET email = 'uanchanquein@lee.com' WHERE lastName = 'Tseng'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
