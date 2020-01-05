#!/usr/bin/python

import sys
import csv
import re
#words = []
for row in sys.stdin:
	row = re.sub(r'^\W+|\W+$', '', row)
	row = re.sub(r'[0-9]+', '', row) # to only keep words, get rid of numbers
	words = re.split(r'\W+',row)
	ngram = zip(*[words[i:] for i in range(3)]) # to create the ngram by using zip method
	for ng in ngram:
		print(' '.join(ng).lower() + '\t1')

# Refrences used
#https://www.eecs.yorku.ca/~papaggel/courses/eecs4415/docs/tutorials/tut5-mapreduce.pdf
#http://www.albertauyeung.com/post/generating-ngrams-python/