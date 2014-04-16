#!/usr/bin/python

import hashlib
import os

def gen_md5_file(path):
	#m = hashlib.md5()
	#fileHandle = open(path, 'rb')
	#m.update(fileHandle.read())
	#fileHandle.close()
	#return m.hexdigest()
	items = path.split('/', 1)
	result = items[1].split('.', 1)
	return result[0]

def gen_md5_str(strVal):
	m = hashlib.md5()
	m.update(strVal)
	return m.hexdigest()

def cal_md5_val(md5Val):
	result = 1

	for c in md5Val:
		if c == '0':
			result = result + 0
		if c == '1':
			result = result * 1
		if c == '2':
			result = result + 2
		if c == '3':
			result = result * 3
		if c == '4':
			result = result + 4
		if c == '5':
			result = result * 5
		if c == '6':
			result = result + 6
		if c == '7':
			result = result * 7
		if c == '8':
			result = result + 8
		if c == '9':
			result = result * 9
		if c == 'a':
			result = result + 10
		if c == 'b':
			result = result * 11
		if c == 'c':
			result = result + 12
		if c == 'd':
			result = result * 13
		if c == 'e':
			result = result + 14
		if c == 'f':
			result = result * 15
	return result
