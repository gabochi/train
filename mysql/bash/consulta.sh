#!/bin/bash

# consulta.sh MySql script

# To show the columns from a table use the following command:
# COMANDO="USE classicmodels; DESC offices;"

# Build first part of the command.
COMANDO="USE classicmodels; SELECT * FROM employees"

# If no args, end the command.  Otherwise, complete the command.
[ -z $1 ] && COMANDO="$COMANDO;" || COMANDO="$COMANDO WHERE $1 LIKE '$2';"

# Run the command.
mysql -u root --execute="$COMANDO"

# Check exit code, if error show help.
[ $? == 0 ] && echo "Done ^_^" || echo "USAGE: ./consulta.sh [column likevalue] \
	EXAMPLE: ./consulta.sh phone %78% \
	No args show the entire table."
