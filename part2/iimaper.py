#!/usr/bin/python
import sys
import re
import csv 




input_file = csv.reader(sys.stdin)
next(input_file)
for row in input_file:
	bid = row[0]
	cat = row[12].split(';')
	for elem in cat:
		print(elem + '\t' +  bid)
