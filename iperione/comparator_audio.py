import os, sys, difflib
import wavefile_audiolab

from comparator import Comparator
from scikits.audiolab import Sndfile

class Comparator_audio(Comparator):
	def __init__(self):
		self.areEqual = True
		self.diff_nSamples = 0

	def run(self):
		self.__init__()
		self.sndfile_expected = Sndfile(self.expected)
		self.sndfile_result = Sndfile(self.result)
		if self.sndfile_result.nframes != self.sndfile_expected.nframes:
			self.areEqual = False
			self.diff_nSamples = self.sndfile_result.nframes - self.sndfile_expected.nframes

