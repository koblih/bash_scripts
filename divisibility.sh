#! /bin/bash


divisibility(){

	read -p "Please enter a number:  " number

	for i in {2,3,5}
	do
		if [ $(( number % ${i} )) == 0 ]; then
			echo "The number ${number} is divisible by ${i}"
		fi
	done

}

divisibility

