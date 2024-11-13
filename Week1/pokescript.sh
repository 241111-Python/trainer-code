#!/usr/bin/bash

while IFS=, read ID NAME TYPE1 TYPE2
do 
    echo $NAME
done <"./../SourceData/pokemon.csv"