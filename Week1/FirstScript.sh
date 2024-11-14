#!/usr/bin/bash 

# hash-bang or shebang - tells the system to use a specific interpreter/language

# we can use the hash character to denote a comment
# anything we do from terminal, we can do in a script!

echo "Hello World!"

# Bash is an interpreted language - there is no compiling, just execution
# Partial runs are a thing - executing a scipt up to a line that won't work
# Commands are executed sequentially - line by line - in a bash script

#mkdir ./NewDir
#touch ./NewDir/Newfile.txt
#echo "this is some new content" >> ./NewDir/Newfile.txt

# Looping

# c-like
for (( i = 0 ; i < 100; i++ )); do
	echo "$i" > ./NewDir/Newfile.txt
done
echo "$i"

# while
count=0
while (( count < 3 )); do
	echo "true"
	count=$count+1
done

# range
for i in {1..5}; do
	echo "range $i"
done
echo "$i"


# Conditionals

# if conditionals must result in a true (1) or a false (0)
# true/false
# > ~ -gt
# < ~ -lt
# == ~ -eq / ==
# <= ~ -le
# >= ~ -ge
# != ~ -ne / !=
# && ~ &&
# || ~ ||
# empty string ~ -z STRING
# NOT empty string ~ -n STRING

if [[ 1 -ne 1 ]]; then
	echo "One is itself"
elif [[ 5 -eq $i ]]; then
	echo "$i is 5"
else 
	echo "I hope this doens't run!"
fi


# Case/Switch 
# the conditional value does not need to be boolean.

#case "$1" in
#	echo "case 1"
#esac


# Reading Input
echo -n "please give an input: "
read -r res
echo "$res"