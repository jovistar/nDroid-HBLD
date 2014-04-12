#!/usr/bin/python

import os

class Statd():
	def __init__(self, m , k):
		self.m = m
		self.k = k
		self.ts = 0
		self.ms = 0
		self.bs = 0
		self.p = 0
		self.n = 0
		self.tp = 0
		self.fp = 0
		self.tn = 0
		self.fn = 0

	def set_ms(self, val):
		self.ms = val
		self.ts = self.ms + self.bs

	def set_bs(self, val):
		self.bs = val
		self.ts = self.ms + self.bs

	def set_p(self, val):
		self.p = val

	def set_n(self, val):
		self.n = val

	def inc_p(self):
		self.p = self.p + 1

	def inc_n(self):
		self.n = self.n + 1

	def inc_tp(self):
		self.tp = self.tp + 1

	def inc_fp(self):
		self.fp = self.fp + 1

	def inc_tn(self):
		self.tn = self.tn + 1

	def inc_fn(self):
		self.fn = self.fn + 1

	def print_result(self):
		print 'm:   %d' % self.m
		print 'k:   %d' % self.k
		print 'ts:  %d' % self.ts
		print 'ms:  %d' % self.ms
		print 'bs:  %d' % self.bs
		print 'p:   %d' % self.p
		print 'n:   %d' % self.n
		print 'tp:  %d' % self.tp
		print 'fp:  %d' % self.fp
		print 'tn:  %d' % self.tn
		print 'fn:  %d' % self.fn

	def write_result(self):
		fileHandle = open('result.txt', 'a+')

		fileHandle.write('%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n' % (self.m, self.k, self.ts, self.ms, self.bs, self.p, self.n, self.tp, self.fp, self.tn, self.fn))
		
		fileHandle.close()
