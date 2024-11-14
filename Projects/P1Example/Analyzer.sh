#!/usr/bin/bash

# This is my Analyzer.
# When run, it performs an analysis of the Data.txt file.
source ./Library.sh
SUM=0

while IFS=\n read -r val1
do
    add $val1
done < ./Data.txt

echo $SUM >> ./Statistics.txt
    