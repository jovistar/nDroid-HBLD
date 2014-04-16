#!/usr/bin/python

import math

class Hbld():
	def __init__(self, m, c):
		self.header = 0
		self.slices = []
		self.m = m
		self.c = c
		self.conflictNum = 0

	def add_slice(self):
		newSlice = []
		newSlice.append(0)
		newSlice.append(self.m)

		unitNum = self.m / 32
		for i in range(0, unitNum):
			newSlice.append(0)

		self.slices.append(newSlice)
		self.header = self.header + 1

	def get_available_slice(self):
		if self.header == 0:
			self.add_slice()
		
		total = float(self.slices[-1][1])
		used = float(self.slices[-1][0])
		if ( used / total ) >= float(0.5):
			self.add_slice()
		if self.conflictNum > self.c:
			self.conflictNum = 0
			self.add_slice()

	def get_size(self):
		size = 32
		for i in range(0, len(self.slices)):
			size = size + len(self.slices[i]) * 32

		return size

	def get_bit(self, unit, offset):
		result = ( unit & ( 0x01 << offset) ) >> offset
		if result == 1:
			return True
		return False
		
	def set_bit(self, unit, offset):
		unit = ( unit | ( 0x01 << offset) )
		return unit

	def get_unit_no(self, val):
		return int(math.floor(val / 32) + 2)

	def get_unit_offset(self, val):
		return val % 32

	def insert_item(self, vals):
		self.get_available_slice()
		for val in vals:
			val = val % self.m
			
			unitNo = self.get_unit_no(val)
			unitOffset = self.get_unit_offset(val)

			if not self.get_bit(self.slices[-1][unitNo], unitOffset):
				self.slices[-1][unitNo] = self.set_bit(self.slices[-1][unitNo], unitOffset)
				self.slices[-1][0] = self.slices[-1][0] + 1
			else:
				self.conflictNum = self.conflictNum + 1

	def query_item(self, vals):
		for i in range(0, len(self.slices)):
			setNum = len(vals)
			for val in vals:
				val = val % self.m

				unitNo = self.get_unit_no(val)
				unitOffset = self.get_unit_offset(val)

				if self.get_bit(self.slices[i][unitNo], unitOffset):
					setNum = setNum - 1
			
			if setNum == 0:
				return True

		return False
