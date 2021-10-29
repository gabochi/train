#!/bin/bash

# inserta.sh MySql script

# To show the columns from a table use the following command:
# COMANDO="USE classicmodels; DESC offices;"

# Count number of rows to set officeCode value
officeCode=$(mysql -u root --execute="USE ${TRAIN_DATABASE}; SELECT COUNT(*) FROM offices" | grep -o '[0-9]*')
((officeCode++))

# Build first part of the insert command
COMANDO="USE ${TRAIN_DATABASE}; INSERT INTO offices(officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory) VALUES "


echo "officeCode: $officeCode"
read -p "city: " -ei "CABA" city
read -p "phone: " -ei "+59 11 67672626" phone
read -p "addressLine1: " -ei "Cachimayo 1516" addressLine1
read -p "addressLine2: " -ei "None" addressLine2
read -p "state: " -ei "Buenos Aires" state
read -p "country: " -ei "Argentina" country
read -p "postalCode: " -ei "1437" postalCode
read -p "territory: " -ei "pobre" territory

# Build last part of the insert command
COMANDO="$COMANDO('$officeCode','$city','$phone','$addressLine1','$addressLine2','$state','$country','$postalCode','$territory')"
#echo $COMANDO

# Run the command.
mysql -u root --execute="$COMANDO"

# Check exit code, if no error show insert
[ $? == 0 ] && mysql -u root --execute="USE ${TRAIN_DATABASE}; SELECT * FROM offices WHERE officeCode=$officeCode"

