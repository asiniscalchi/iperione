import os, sys, difflib
from comparator import Comparator

class Comparator_txt(Comparator):
	def run(self):
		expectedLines = open(self.expected, 'U').readlines()
		resultLines = open(self.result, 'U').readlines()
		self.diff = difflib.unified_diff(expectedLines, resultLines, self.expected, self.result)

	def areEqual(self):
		if len(list(self.diff)) == 0:
			return True
		return False		
	

