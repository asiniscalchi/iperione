import os, sys, difflib
from numpy import allclose
from comparator import Comparator
from scikits.audiolab import Sndfile

class ComparatorAudio(Comparator):

	def run(self):
		expected = Sndfile(self.expected)
		result = Sndfile(self.result)

		if (not self.isFormatEqual(expected, result)):
			self.diff = str(result) + str(expected)
			return

		frameSize = 1024
		index = 0

		while(index < result.nframes):
			if (result.nframes - index) < frameSize:
				frameSize = result.nframes - index

			resultFrame = result.read_frames(frameSize)
			expectedFrame = expected.read_frames(frameSize)
			if (not allclose(resultFrame, expectedFrame)):
				self.diff = "Content is different"
				return;
			index += frameSize

		self.diff = None

	def isFormatEqual(self, expected, result):
		if (result.channels != expected.channels 
			or result.encoding != expected.encoding
			or result.endianness != expected.endianness 
			or result.file_format != expected.file_format
			or result.format != expected.format 
			or result.nframes != expected.nframes 
			or result.samplerate != expected.samplerate):
			return False
		return True

