# Simple and possibly redundant URL/URI defanger.  
# Can take a file as an argument, otherwise treats all 
# text to the left of first whitespace as a string argument.
# youtube.com/snoozesecurity

import re
import sys
import os.path

def defang(url):
		newurl =  re.sub('[.]', '[.]', url)
		newurl = newurl.replace("http", "hxxp", 1)
		return newurl

if len(sys.argv) > 1:

	defanged = []

	if os.path.isfile(sys.argv[1]) == True:
		with open(sys.argv[1]) as f:
			for line in f:
					defanged.append(defang(line))
		for p in defanged: print p.rstrip("\n\r")

	elif "." in sys.argv[1] or "http" in sys.argv[1]: 
		print 'Defanged as string:', defang(sys.argv[1])

	elif sys.argv[1]:
		print 'Not defanged:', defang(sys.argv[1])

else:
	print 'Needs input, either /path/to/file or URL.'

