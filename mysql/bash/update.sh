#!/bin/bash

# script para updatear tabla de empleados

# IMPORTANTE:
# 0. IMPLEMENTACIÓN DE PARSEO DE ARGUMENTOS
# 1. ESTE TEST USA UNA VARIABLE DE ENV (VER .env)
# 2. NO PERMITE ACTUALIZAR DATOS SIN WHERE PARA EVITAR DESASTRES


# Parsear argumentos
# https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash#13359121
for i in "$@"
do
case $i in
    s:*|set:*)
    SETPAR="${i#*:}"
    ;;

    w:*|where:*)
    WHERE="${i#*:}"
    ;;
    
    *)
            # unknown option
    echo "EXAMPLE"
    echo -e "\tupdate set:\"email='gabochi@github.com'\" where:\"lastName='vinazza'\""
	exit
    ;;
esac
done


#echo "USE ${TEST_DATABASE}; UPDATE employees SET ${SETPAR} WHERE ${WHERE};"
mysql -u root --execute="USE ${TEST_DATABASE}; UPDATE employees SET ${SETPAR} WHERE ${WHERE};"

[ $? == 0 ] && mysql -u root --execute="USE ${TEST_DATABASE}; SELECT * FROM employees WHERE ${WHERE};"
