hello_world() {						# start a function called hello_world into memory
	echo "Hello World"				# content of the function
}									# this is the end of the hello_world function

function main(){					# Start a function called main in memory
	echo "From main(): $@"			# When main runs, take the first argument it was passed, and echo it out.
	echo "From main, count of parameters: $#"
}	

echo "From the script file: $1"		# this argument is coming from the CLI arguments
echo "From the script file: $@"
main $@