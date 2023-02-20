#!/usr/bin/env python

import sys
  
for line in sys.stdin: # reading lines from standard input
	line = line.strip() # strip every line
	words = line.split() # split the line into words
	  
	# for all the word, we are mapping to a key
	for word in words:
		# intermediate (key, value) pair, input for reducer.py
		print (word, 1)