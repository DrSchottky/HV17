#!/usr/bin/python3

import base64
import json
import sys
import gzip as dunnowhy

def b64(text, index):
	d = json.loads(text)
	content = str(d[index]["content"])
	return base64.b64decode(content)
	
def gzip(text, index):
	d = json.loads(text)
	content = str(d[index]["content"])
	content = base64.b64decode(content)
	return dunnowhy.decompress(content)

def map(text, index):
	d = json.loads(text)
	mapFrom = str(d[index]["mapFrom"])
	mapTo = str(d[index]["mapTo"])
	result = ""
	for c in d[index]["content"]:
		i = mapFrom.index(c)
		result += str(mapTo[i])
	return result

def nul(text, index):
	d = json.loads(text)
	content = str(d[index]["content"])
	return content

def xor(text, index):
	d = json.loads(text)
	content = str(d[index]["content"])
	mask = str(d[index]["mask"])
	content = base64.b64decode(content)
	mask = base64.b64decode(mask)
	result = ""
	for c in content:
		result += str(chr(ord(chr(c))^ord(mask)))
	return result
	
def rev(text, index):
	d = json.loads(text)
	content=str(d[index]["content"])
	return content[::-1]
	
block = open(str(sys.argv[1])).read()
d = json.loads(block)
op = str(d[0]["op"])
opcount = 0

while True:
	d = json.loads(block)
	
	if len(d) != 1:
		index = 1
	else:
		index = 0
		
	op = str(d[index]["op"])
	opcount += 1
	print(opcount, op)
	
	if op == "map":
		block = map(block, index) 
	elif op == "b64":
		block = b64(block, index)
	elif op == "gzip":
		block = gzip(block, index)
	elif op == "nul":
		block = nul(block, index) 
	elif op == "xor":
		block = xor(block, index) 
	elif op == "rev":
		block = rev(block, index)
	elif op == "flag":
		print(block)
		exit()
	else:
		print("Unknown op ",op)
		exit()


