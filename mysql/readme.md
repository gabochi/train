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
***

## Insertar
[refe](https://www.mysqltutorial.org/mysql-insert-statement.aspx)

## Insertar en bash
1. La tabla qye elegí no tiene valores por defecto, de manera que no puedo insertar columnas aisladas.  En principio hice que se ingresen uno por uno los campos, por defecto aparecen valores inventados que pueden editarse.
2. Usé `COUNT(*)` para poder saber qué valor correspondía en la primera columna que siempre es un id.  Luego un pequeño REGEX para obtener únicamente el número del output de mysql.  Para probar REGEX [](https://regex101.com/) está bueno.  Usé `grep -o` para que me muestre los matches únicamente y `[0-9]*` para matchear números.
3. Una vez que estaba fucionando ok, implementé el nombre de la base como variable de entorno como sugirió Dave.  `TRAIN_DATABASE=classicmodels ./inserta.sh` o `. .env` en el script.

## Update
[refe](https://www.mysqltutorial.org/mysql-update-data.aspx)

## Update en bash
1. Encontré un código muy simple para poder parsear argumentos en bash: [](https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash#13359121)
2. Para que sea un poco más lógico, pasé de la tabla de offices a employees como sugiere el ejemplo de la [referencia](https://www.mysqltutorial.org/mysql-update-data.aspx)
3. Es un poco molesto tener que usar comillas dobles y simples en los parámetros, tampoco tiene mucho sentido el script de update ya que es prácticamente igual al comando de mysql (sobre todo considerando que el WHERE es obligatorio para no hacer desastres).  Ejemplo: `update set:"email='gabochi@github.com'" where:"lastName='vinazza'"`. Si no se ponen todos los parámetros, sencillamente se rompe y no cambia nada.
__Reflexión:__ Me encanta hacer todo en bash, más ahora con este parser de argumentos.  Es más lento que en python pero mucho más directo ya que no tengo que usar ningún objeto, simplemente ejecutar el comando que quiera de mysql con --execute.  Pero precisamente por eso, aprendo más de mysql que de "cómo usar mysql con bash" porque básicamente es correr el comando directamente.  En Python por lo menos tengo que aprender cómo se usan los métodos del módulo mysql y todas esas cosas horribles.

## Insert en python
[refe](https://www.w3schools.com/python/python_mysql_select.asp)
1. Uso la tabla de employees, tengo que averiguar el número que correspondería al próximo empleado.  No se corresponde el número de filas con el de empleados y tampoco están todos los números así que hago un `SELECT MAX(employeeNumber)` para encontrar el valor más alto y sumarle uno al que voy a insertar.
2. Voy a ver si puedo asignar valores por defecto a todas las columnas restantes directamente desde mysql porque es muy molesto.
3. Leyendo otra vez [](https://www.mysqltutorial.org/mysql-insert-statement.aspx) me doy cuenta que NULL funciona como default, ¿por qué a mí no me funciona?  Hago un `DESCRIBE employees` y dice clarito NULL en default...

## Update en python
[refe](https://www.w3schools.com/python/python_mysql_update.asp)
1. Copié el código de referencia y hardcodié los datos para hacer una prueba
2. Me encuentro con que en esta compu sí tengo un password así que es una buena oportunidad para usar las variables de entorno como en bash
3.

***
## Dump and Restore
[refe1](https://phoenixnap.com/kb/how-to-backup-restore-a-mysql-database)
[refe2](https://www.mysqltutorial.org/mysql-drop-database/)
[refe3](https://www.mysqltutorial.org/mysql-create-database/)

1. Para hacer el dump: `sudo mysqldump -u [user] -p [database_name] > [filename].sql`
2. Después borré la base con `DROP DATABASE`.
3. Hacer el restore fue bastante simple también pero algo para recordar es que **hay que crear una base con el nombre de la base de la que queremos hacer restore antes de hacerlo**.  Yo lo hice así:
`mysql -u root -p --execute "create database classicmodels;" && mysql -u root -p classicmodels < dump.sql`

*NOTA*: En la desktop, al instalarlo, quedó el root de MySql con el password de mi usuario (gabochi).



