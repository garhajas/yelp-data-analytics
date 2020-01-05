#!/usr/bin/python3

import sys
import re
import csv

#table = []

in_file = csv.reader(sys.stdin)
next(in_file)
for row in in_file:
	bid = row[0] 
	checkins = row[3]
	days = row[1]
	print(bid + ',' + days + ' : ' + checkins)
	
