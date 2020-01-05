#!/usr/bin/python3
import sys
import re

previous = None
sum = 0

for line in sys.stdin:
        line = line.strip()
        line = re.sub(r'^\W+|\W+$', '', line)
        key, value = line.split(':')
        if key != previous:
                if previous is not None:
                        print(str(previous) + ', ' + str(sum))
                previous = key
                sum = 0;
        sum = sum + int(value)

print(str(previous) + '\t' + str(sum) )