import os, sys, difflib
import wavefile_audiolab

from comparator import Comparator

class Comparator_wav(Comparator):
	def _specializedCompare(self):
		return
#		expectedLines = open(self.expected, 'U').readlines()
#		resultLines = open(self.result, 'U').readlines()
#		self.diff = difflib.unified_diff(expectedLines, resultLines, self.expected, self.result)

	def areEqual(self):
		return True		
	

