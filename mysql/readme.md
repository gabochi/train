# Aprendiendo MySql
## Bitácora
***
## Instalación y configuración

1. Instalé VirtualBox `sudo dnf install VirtualBox`
2. Lo corrí y creé una vm con el mismo sistema que tengo acá (Fedora-64)
3. Quise iniciar la vm pero me tiró error porque necesito instalar el kernel (?) así que decidí instalar mysql directamente en mi máquina por el momento `sudo dnf install mysql`
4. Pensé que podía correrlo directamente con `mysql` pero no, así que leo un poco con `man mysql` a ver qué onda.
5. También encontré este [tutorial](https://www.mysqltutorial.org/) y veo que debería tener instalado un servicio, puede ser que la instalación que hice está incompleta. Consulto en (https://docs.fedoraproject.org/en-US/quick-docs/installing-mysql-mariadb/) y me instalo el paquete que se indica ahí: `community-mysql-server`
6. Tiro un `systemctl status mysqld` y ahora sí, efectivamente, está instalado.
7. `systemctl enabled mysqld`, `systemctl start mysqld`
8. Me conecto al server como root `mysql -u root -p`, le doy enter en el pass y funca.
9. Pruebo un primer comando `show databases;` y el output es el esperado.

## Probando con una base de ejemplo
Usé esta [refe](https://www.mysqltutorial.org/mysql-sample-database.aspx)

1. Descargo la base *mysampledatabase.sql*
2. La cargo con el comando `source [archivo]`
3. Hago un `USE classicmodels` y `SELECT * FROM offices`, me muestra los resultados, todo ok.
4. Pruebo consultas básicas con `SELECT` `FROM` `ORDER` etc. [refe](https://www.mysqltutorial.org/mysql-basics/)

## Cómo crear una base e insertar datos

1. Creo una db de prueba con `CREATE DATABASE` [Refe](https://www.mysqltutorial.org/mysql-create-database/)
2. Creo una tabla con id y un par de campos [Refe](https://www.mysqltutorial.org/mysql-insert-statement.aspx)
3. Me dió error porque tengo que definir que alguno de sus campos sea PRIMARY KEY, por ejemplo un id ascendente: `CREATE TABLE tablita (... id INT AUTO_INCREMENT ..., PRIMARY KEY (id) );`
4. Funcionó, hice un par de entries, todo ok.
5. Probé reemplazar con `REPLACE` [Refe](https://www.mysqltutorial.org/mysql-replace.aspx), reemplazó el campo que le dije bien pero **me pisó el campo que no especifiqué con un NULL**. Si voy a usar este comando tengo que revisar el comportamiento pero ahora quiero resolver solamente el script de consulta e insert.
NOTA: Una posibilidad es usar `UPDATE` en lugar de `REPLACE`
*** 
## El script de consulta en Bash

1. Voy a empezar con bash.  Se pueden ejecutar instrucciones de mysql con el parámetro `--execute`. 
2. Me detuve un rato en el script de consulta para hacerlo interesante,  no solamente usando [WHERE](https://www.w3schools.com/mysql/mysql_where.asp) sino también el operador [LIKE](https://www.w3schools.com/mysql/trymysql.asp?filename=trysql_op_like).

## El script de consulta en Python

1. Antes de hacer el script para ingresar o modificar datos en la base, me pareció mejor hacer el script de consulta también en Python.
2. Creé un venv para el programita.
3. Con [esta](https://www.w3schools.com/python/python_mysql_select.asp) referencia fue fácil hacer una consulta pero...
4. Me demoré porque quise implementar lo aprendido de *argparse*, me constó un poco resolver cómo invocar los argumentos porque ninguna de las formas que aparecen [acá](https://docs.python.org/3/library/argparse.html) y [acá](https://www.datacamp.com/community/tutorials/argument-parsing-in-python) resultaron.  Finalmente lo resolví usando `namespace.key`.  Funciona bien, si no se ingresan argumentos muestra toda la tabla ya que asigna valores por defecto a los argumentos.

***
## Repo train
Creé este repositorio como me sugirió Dave, una especie de *training blog*.

