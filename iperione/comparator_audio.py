import os, sys, difflib
import wavefile_audiolab

from comparator import Comparator
from scikits.audiolab import Sndfile
class ComparatorAudio(Comparator):
	def __init__(self):
		self.diff_nSamples = 0

	def run(self):
		self.sndfile_expected = Sndfile(self.expected)
		self.sndfile_result = Sndfile(self.result)
		if self.sndfile_result.nframes != self.sndfile_expected.nframes:
			self.diff = "delta samples = " + str(self.sndfile_result.nframes - self.sndfile_expected.nframes)
		else:
			self.diff = None
	
	def areEqual(self):
		if self.diff != None:
			return False
		return True		
	

