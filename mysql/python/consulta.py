import mysql.connector
import argparse

# Instanciar objeto parser
parser = argparse.ArgumentParser()

# Agregar argumentos a la instancia
parser.add_argument("-c", "--column", default="city", help="Columna a consultar")
parser.add_argument("-v", "--value", default="%", help="Valor a consultar")

# Asignar parámetros parseados a args
args = parser.parse_args()

# Configuración mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classicmodels"
)

# Intanciar objeto base
mycursor = mydb.cursor()

# Arma el comando con los argumentos
comando = "SELECT * FROM offices WHERE " + args.column + " LIKE '" + args.value + "'"

# Ejecutar comando en la instancia
mycursor.execute(comando)
#print(comando)

# Asignar resultados del comando a myresult
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
