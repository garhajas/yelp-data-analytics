#!/usr/bin/python3

# Jaskaran
import sys
import re
def printfunc():
	print("hello")


previous = None
sum = 0
str_out = ''
# We are usign a string to k
for line in sys.stdin:
	key, value = line.split('\t')
	if key != previous:
		if previous is not None:
			str_out = str_out.replace("\n","")
			print('\n')
			print(str(previous) + ": " + str(str_out[:-2]) , end='')
			#print(str(sum) + '\t' + previous)
		previous = key
		str_out = ''
	str_out = str((str_out + value + ', '))
	#print(str_out)
	#str_out.append(value)
	#print(previous + ':\t' + str_out, end='')
	#sum = sum + int(value)
print('\n')
str_out = str_out.replace("\n","")
print(str(previous) + ": " +  str(str_out[:-2]) , end='')
print('')