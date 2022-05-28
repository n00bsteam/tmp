#!/usr/bin/python3

import sys, getopt
import random
import string
import hashlib


def randStr(chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', n=10):
	return ''.join(random.choice(chars) for _ in range(n))

def main(argv):
	m = '00'
	n = 10
	f = 'randomfile.txt'
	rand_str = randStr(n=n)
	hash_gen = hashlib.md5(rand_str.encode('utf-8')).hexdigest()
	try:
		opts, args = getopt.getopt(argv,"hm:n:f:",["sMD5=","number=","output="])
	except getopt.GetoptError:
		print('gen.py -m <MD5 starts "00"> -n <length or random string "10"> -f <output file name "randomfile.txt">')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('gen.py -m <MD5 starts "00"> -n <length or random string "10"> -f <output file name "randomfile.txt">')
			sys.exit()
		elif opt in ("-m", "--sMD5"):
			m = arg
		elif opt in ("-n", "--number"):
			n = int(arg)
		elif opt in ("-f", "--output"):
			f = arg
#	print('MD5 start "', m)
#	print('length is "', n)
#	print('output is "', f)
	counter = 1
	while hash_gen[0:2] != m:
		rand_str = randStr(n=n)
		hash_gen = hashlib.md5(rand_str.encode('utf-8')).hexdigest()
		counter += 1

	print('[+] Got in ' + str(counter) +  ' : ' + hash_gen + ' ' + rand_str)
	text_file = open(f, "w")
	n = text_file.write(rand_str)
	text_file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
