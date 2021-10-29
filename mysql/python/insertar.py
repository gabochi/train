import mysql.connector

# database configuration

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classicmodels"
)

# instanciate cursor
mycursor = mydb.cursor()

# command to find the max value in employeeNumber
mycursor.execute("SELECT MAX(employeeNumber) FROM employees")

# query
myresult = mycursor.fetchall()

# an annoying way of getting the int
a = myresult[0]
b = a[0]
number = b + 1

sql = "INSERT INTO employees (employeeNumber, firstName) VALUES (%s, %s)"
val = (number, "Cachito")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
