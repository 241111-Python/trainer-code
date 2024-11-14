#!/usr/bin/bash

# I'll be wrapping all functionality in functions, just for familiarity and organizations sake.

# main will be my root method, I'll be passing it the parameters generated from the cli
main(){
    echo "ExtraExample Running..."
# This will test to make sure that the function library file is where it needs to be, or otherwise exits the script.
    LIB="./FunctionLibrary.sh"
    if [ -e $LIB ]
    then
        source ./FunctionLibrary.sh
    else
        echo "Library Not Found"
        exit 1
    fi

# This puts together the options I want to allow from the cli input
    OPTIONS=$(getopt -o hvf: -l help,version,file: -- "$@" 2>/dev/null)

# If the options provided from cli are incompatable, run the help function
    if [ $? -ne 0 ]
    then
        help
    fi

# Set the supplied options flags, then clear the options variable
    eval set -- $OPTIONS
    unset OPTIONS

# Use a while loop to direct the user to the correct function based on the flag provided
    while true
    do
        case "$1" in
            -h|--help) HELP=1; help ;;
            -v|--version) VER=1; version ;;
            -f|--file) FILE="$2"; shift ;;
            --) shift ; break ;;
            *) HELP=1; help ;;
        esac
        shift
    done

    echo "$FILE"
# Exit the script gracefully, with a "completed successfully" exit code.
    echo "ExtraExample complete."
    exit 0
}

main "$@"