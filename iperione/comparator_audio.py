import os, sys, difflib
import wavefile_audiolab

from comparator import Comparator
from scikits.audiolab import Sndfile

class Comparator_audio(Comparator):
	def _specializedCompare(self):
		self.sndfile_expected = Sndfile(self.expected)
		self.sndfile_result = Sndfile(self.result)
		if self.sndfile_result.nframes != self.sndfile_expected.nframes:
			self.diff = "ciaociao"
		else:
			self.diff = None
	
	def areEqual(self):
		if self.diff != None:
			return False

		return True		
	

