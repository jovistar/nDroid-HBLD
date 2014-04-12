#!/usr/bin/python

import os
import getopt
import util
from statd import Statd
from hbld import Hbld
import sys

def get_apk_list(apkDir):
	apkList = []

	dirs = os.walk(apkDir)
	for root, dirss, files in dirs:
		for oneFile in files:
			if oneFile[-4:] == '.apk':
				apkList.append('%s/%s' % (apkDir, oneFile))
	
	return apkList

def insert_apk_item(hbld, apkList, stat, flag, m, k):
	for apk in apkList:
		print 'Inserting %s' % apk
		md5Val = util.gen_md5_file(apk)
		vals = get_hash_val(md5Val, m, k)
		print vals
		hbld.insert_item(vals)

	if flag == 'p':
		stat.set_ms(hbld.get_size())
	if flag == 'n':
		stat.set_bs(hbld.get_size())

def query_apk_item(hbld, mApkList, bApkList, stat, flag, m, k):
	for apk in mApkList:
		print 'Querying %s' % apk
		md5Val = util.gen_md5_file(apk)
		vals = get_hash_val(md5Val, m, k)
		result = hbld.query_item(vals)

		if result == True:
			if flag == 'm':
				stat.inc_tp()
			elif flag == 'b':
				stat.inc_fn()

	for apk in bApkList:
		print 'Querying %s' % apk
		md5Val = util.gen_md5_file(apk)
		vals = get_hash_val(md5Val, m, k)
		result = hbld.query_item(vals)

		if result == True:
			if flag == 'm':
				stat.inc_fp()
			elif flag == 'b':
				stat.inc_tn()

def get_hash_val(md5Val, m, k):
	hashVals = []

	if k not in [1, 2, 4, 8, 16, 32]:
		return hashVals

	start = 0
	stop = 32 / k

	for i in range(0, k):
		hashVal = util.cal_md5_val(util.gen_md5_str(md5Val[start:stop]))
		hashVals.append(hashVal % m)
		start = stop
		stop = stop + 32 / k

	return hashVals


def main_loop(m, k):
	mHbld = Hbld(m)
	bHbld = Hbld(m)

	stat = Statd(m, k)

	mApkList = get_apk_list('mal')
	stat.set_p(len(mApkList))
	bApkList = get_apk_list('ben')
	stat.set_n(len(bApkList))

	insert_apk_item(mHbld, mApkList, stat, 'p', m, k)
	insert_apk_item(bHbld, bApkList, stat, 'n', m, k)

	query_apk_item(mHbld, mApkList, bApkList, stat, 'm', m, k)
	query_apk_item(bHbld, mApkList, bApkList, stat, 'b', m, k)

	stat.write_result()
	stat.print_result()

if __name__ == '__main__':
	opts, args = getopt.getopt(sys.argv[1:], 'm:k:')

	m = 4096
	k = 4

	for opt, arg in opts:
		if opt in ('-m'):
			m = int(arg)
		if opt in ('-k'):
			k = int(arg)

	main_loop(m, k)

