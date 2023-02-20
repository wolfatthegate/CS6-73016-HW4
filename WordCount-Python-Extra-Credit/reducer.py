#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
word = None
current_count = 0
current_word = None
  
for line in sys.stdin: # read lines from STDIN or file

	line = line.strip() # remove spaces from head and tail
	# splitting the data on the basis of tab we have provided in mapper.py

	word, count = line.split(' ', 1)
    # count current_word
	if current_word == word:
		current_count += count
	else:
		if current_word:
			print(current_word, current_count)
		current_count = count
		current_word = word
  
# count the last word if applies.
if current_word == word:
	print(current_word, current_count)