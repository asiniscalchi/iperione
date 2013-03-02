from numpy import allclose
from comparator import Comparator
from scikits.audiolab import Sndfile

class ComparatorAudio(Comparator):
	def __init__(self):
		self.diff = None

	def run(self):
		expected = Sndfile(self.expected)
		result = Sndfile(self.result)

		if not self._isFormatEqual(expected, result):
			self.diff = str(result) + str(expected)
			return
		if not self._isContentClose(expected, result):
			self.diff = "Content is different"
			return
		self.diff = None

	def _isContentClose(self, expected, result):
		index = 0
                frameSize = 1024
                while index < result.nframes:
                        frameSize = min(result.nframes - index ,frameSize)
                        resultFrame = result.read_frames(frameSize)
                        expectedFrame = expected.read_frames(frameSize)
                        if not allclose(resultFrame, expectedFrame):
                                return False
                        index += frameSize
		return True

	def _isFormatEqual(self, expected, result):
		if (result.channels != expected.channels 
			or result.encoding != expected.encoding
			or result.endianness != expected.endianness 
			or result.file_format != expected.file_format
			or result.format != expected.format 
			or result.nframes != expected.nframes 
			or result.samplerate != expected.samplerate):
			return False
		return True

