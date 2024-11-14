#!/usr/bin/bash

# This is the Function Library for the Extra Example bash script.

help() {
    echo 'Thank you for running the ExtraExample script.

    USAGE
    ./ExtraExample [option] [PATH]

    OPTIONS
    -h  --help    | prints help documentation
    -v  --version | prints ExtraExample version
    -f  --file    | execute analysis for a file at [PATH] '
    exit 1
}

version(){
    echo "ExtraExample
    Why would you think this thing has a version?
    Seriously, do you think that I have nothing better to do 
    than come up with new and updated versions of examples 
    like this one? Come on, you know better than that!
    Ok, I guess this is version 1 or something like that. 
    I'm not actually keeping track, but I'm not likely to 
    make a new or better version of this by the time we're 
    done.       ~Rich"
    exit 1
}

