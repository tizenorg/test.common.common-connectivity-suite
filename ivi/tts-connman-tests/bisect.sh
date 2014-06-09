#!/bin/bash

# Usage: bisect <good commit> <test case>
git bisect start
git bisect good $1
git bisect bad master

while [ 1 ]; do
make clean
pkill -9 connmand
./bootstrap-configure
make -j 9 || { echo make failed; git bisect reset; exit 1; }
src/connmand

$2

if [ $? -eq 0 ]; then
	git bisect good |head -n 1 |grep "bad"
	if [ $? -eq 0 ]; then
		git bisect reset
		echo culprit commit found
		exit 0
	fi
else
	git bisect bad |head -n 1 |grep "bad"
	if [ $? -eq 0 ]; then
		git bisect reset
		echo culprit commit found
		exit 0
	fi
fi
done
	
