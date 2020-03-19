#! /bin/bash

echo "Please select what files you want to rename"
echo "press j to rename jpg files"
echo "press t to rename txt files"
read extension

case ${extension} in
	j)
		echo "You chose jpg"
		;;
	t)
		echo "You chose txt"
		;;
	*)
		echo "That is not an allowed extension"
		;;
esac

read -p "Please provide a new prefix for the selected file(s)" prefix

if [ ${extension} == "j" ]; then
	extension="jpg"
else 
	extension="txt"
fi

files=$(ls)

for file in ${files}
do
	if [[ ${file} == *${extension} ]]; then
		mv ${file} ${prefix}${file}
		echo ${file}
	fi
done
