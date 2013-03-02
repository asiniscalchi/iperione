import os, sys, difflib
import wavefile_audiolab

from comparator import Comparator
from scikits.audiolab import Sndfile
from diffaudio import differences

class ComparatorAudio(Comparator):
	def __init__(self):
		self.diff = str()

	def run(self):
		expected = Sndfile(self.expected)
		result = Sndfile(self.result)
#		self.differ()
		if (result.channels != expected.channels 
			or result.encoding != expected.encoding
			or result.endianness != expected.endianness 
			or result.file_format != expected.file_format
			or result.format != expected.format 
			or result.nframes != expected.nframes 
			or result.samplerate != expected.samplerate):
			self.diff += str(result) + str(expected)
		else:
			self.diff = None
	
	def areEqual(self):
		if self.diff != None:
			return False
		return True		

	def differ(self):
		self.diff = differences(self.expected, self.result, "diff")

                if self.diff:
                        print(" Failed")
                       # os.system('cp %s %s' % (output, badResultName(base,extension)) )
                       # failures.append("Output '%s':\n%s"%(base, '\n'.join(['\t- %s'%item for item in difference])))
                       # testcase.appendFailure("Output '%s':\n%s"%(base, '\n'.join(['\t- %s'%item for item in difference])))
	

