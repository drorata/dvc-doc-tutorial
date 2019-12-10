#!/bin/bash

FILE=$1
N=$2

if [ -z $N ]; then
    cat $1
else
    head -n $N $1
fi
