#! /bin/bash

files=$(ls)

no_files=0

for file in ${files}
do
	if [[ ${file} == *.txt ]]; then
		no_files=$(( no_files + 1 ))
	fi
done

echo "There are ${no_files} txt files in your pwd."

