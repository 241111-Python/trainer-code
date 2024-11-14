#!/usr/bin/bash

# This is my Analyzer.
# When run, it performs an analysis of the Data.txt file.

SUM=0

function add(){
    VAL=$1
    SUM=$((SUM+VAL))
}

while IFS=\n read -r val1
do
    add $val1
done < ./Data.txt

echo $SUM >> ./Statistics.txt
    