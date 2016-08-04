#!/usr/bin/python

import sys
import hashlib

with open('.ssakey') as keyf:
	key = keyf.read().strip()

while True:
	sys.stdout.flush()
	l = sys.stdin.readline()
	if not l:
		break
	if l[:4] != "get ":
		print "400 unknown command"
		continue

	address = l[4:].strip().lower()

	x = address.find('-')
	y = address.find('@')

	if x > 0 and y > x:
		name = address[:x]
		theirsha = address[x+1:y]

		oursha = hashlib.sha1("%s-%s-%s\n" % (key,name,key)).hexdigest()[:6]

		if theirsha == oursha:
			print "200 OK"
		else:
			print "200 reject"
	else:
		print "200 reject"
