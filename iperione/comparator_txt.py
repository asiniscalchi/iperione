import os, sys, difflib
from comparator import Comparator

class Comparator_txt(Comparator):
	def _specializedCompare(self):
		expectedLines = open(self.expected, 'U').readlines()
		resultLines = open(self.result, 'U').readlines()
		self.diff = list(difflib.unified_diff(expectedLines, resultLines, self.expected, self.result))

	def areEqual(self):
		if len(self.diff) == 0:
			return True
		return False		
	

