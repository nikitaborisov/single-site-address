import hashlib

KEYFILE=".ssakey"
with open(KEYFILE) as keyf:
	key = keyf.read().strip()

def hash(name):
	hashstr = "%s-%s-%s\n" % (key,name,key)
	return hashlib.sha1(hashstr.encode()).hexdigest()[:6]

if __name__ == "__main__":
	import sys

	if len(sys.argv) > 1:
		for arg in sys.argv[1:]:
			print("{}-{}".format(arg,hash(arg)))
	else:
		print("Taking input from stdin...")
		for l in sys.stdin:	# FIXME: this buffers in python2
			name = l.strip()
			print("{}-{}".format(name,hash(name)))
