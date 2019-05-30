#/usr/bin/python

import urllib
from bs4 import BeautifulSoup, SoupStrainer
import requests

kw_file = "auto_suggest_input.txt"
url = "http://google.com/complete/search?output=toolbar&q="

try:
	with open(kw_file, 'r') as fp:
		keywords = fp.read().splitlines()
		
except IOError:
	print(f"File not found in the desired location: {kw_file}") 

try:
	with open('auto_suggest_result.txt', 'w') as fp:				
		
		count = 1

		for kw in keywords:
			query = urllib.parse.quote(kw)

			res = requests.get(url + query)
			content = res.text

			print (kw)
			# count += 1
			
			strainer = SoupStrainer("suggestion")
			soup = BeautifulSoup( content, parse_only = strainer)
			# features="html.parser"

			for s in [s['data'] for s in soup]:
				fp.write( s + "\n" )

except IOError:
	print("Could not write to file")
