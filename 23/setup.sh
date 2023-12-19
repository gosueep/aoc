#!/bin/bash

if [ "$1" = "" ]; then
  echo "USAGE: ./setup.sh DAY"
  exit
fi

mkdir "$1"
cp template.py "$1/1.py"
touch "$1/2.py"
touch "$1/test.txt"
touch "$1/input.txt"