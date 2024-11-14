#!/usr/bin/bash

# Read a funciton from a different file
source ./script_source.sh

hello_world

FILE="./../SourceData/samplearrays.csv"

# Reading the first line of the data file, and printing it to terminal
echo "read the first line of the data file: "
read -r csv_data < "$FILE"
echo "$csv_data"

# Read the first line of the data file, and separate the individual values into entries of an array
echo "reading the first line as an array:"
IFS=, read -ra csv_array < "$FILE"
for value in "${csv_array[@]}"
do
	echo "$value"
done

# Read the first line of data from the csv_array created in the last block
echo "reading the first line as an array:"
IFS=, read -ra csv_array <<< "$csv_data"
for value in "${csv_array[@]}"; do
	echo "$value"
done

# Build a function to add the elements of the array
function sum() {
# lets assume that this sum function will be passed an array of values to add up

	local array=("$@")
	local SUM=0

	for value in "${array[@]}"
	do
#		SUM+=$value
		SUM=$((SUM+value))
	done
	echo "$SUM"
}

ARRAY_SUM=$(sum "${csv_array[@]}")
echo "passing the first set of values to a function to calculate the sum of the values:"
echo "$ARRAY_SUM"

