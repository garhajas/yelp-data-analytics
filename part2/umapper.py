#!/usr/bin/python

import sys
import csv
import re

for row in sys.stdin:
	row = re.sub(r'^\W+|\W+$', '', row)
	#row = re.sub(r'^[0-9]+$', '', row) # to only keep words, get rid of numbers
	#row = " ".join(filter(lambda x:x[0]!= r'^[0-9]+', row.split()))
	words = re.split(r'\W+',row)
	for word in words:
		print(word.lower() + '\t1')
