#! /bin/bash

read -p "Type your password: " passwd
if [ $passwd == "pass" ]; then
	echo "Correct"
else
	echo "Incorrect"
	exit
fi

			
