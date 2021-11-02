import mysql.connector
import os
import argparse

# get enviromental variables
user = os.environ['USER']
base = os.environ.get('DB_NAME')
passw = os.environ.get('DB_PASS')

# debug
# print(user,base,passw)

# Instanciar objeto parser
parser = argparse.ArgumentParser()

# Agregar argumentos a la instancia
parser.add_argument("-s", "--set", default="", help="Columna a actualizar")
parser.add_argument("-v", "--value", default="", help="Valor a actualizar")
parser.add_argument("-w", "--where", default="", help="Condición necesaria")

# Asignar parámetros parseados a args
args = parser.parse_args()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=passw,
  database=base
)

mycursor = mydb.cursor()

sql = "UPDATE employees SET " + args.set + " = " + args.value + " WHERE " + args.where

print(sql)
exit

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# Mostrar la lista completa

# Arma el comando con los argumentos
comando = "SELECT * FROM employees"

# Ejecutar comando en la instancia
mycursor.execute(comando)
# print(comando)

# Asignar resultados del comando a myresult
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


