import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classicmodels"
)

mycursor = mydb.cursor()

sql = "UPDATE employees SET email = 'uanchanquein@lee.com' WHERE lastName = 'Tseng'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
