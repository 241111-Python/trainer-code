#!/usr/bin/bash
 
 # This is my Program.
 # It generates data ever time it runs, and logs that data to the ./Data.txt file

 RAND=$(( $RANDOM % 10 ))
 echo $RAND >> ./Data.txt
 exit 0