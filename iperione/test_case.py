import os, subprocess, uuid
import unittest
from comparator_audio import ComparatorAudio

main = unittest.main

class TestCase(unittest.TestCase):
	def __init__(self, methodName='runTest'):
		unittest.TestCase.__init__(self, methodName)
		self.expectedPath = str()
		self.resultPath = str()
		self.diffPath = str()

    	def execute(self, command, shell=False):
    		subprocess.call(command, shell=shell)

	def assertAudioFileEqual(self,  expected, result, msg=None):
		comparator = ComparatorAudio()

		expectedPath = os.path.join(self.expectedPath, expected)
		comparator.setExpected(expectedPath)

		resultPath = os.path.join(self.resultPath, result)
		comparator.setResult(resultPath)

		comparator.run()

		if comparator.diff:
			differing = "Files are different:\n"
			for line in comparator.diff:
				differing += line
			msg = self._formatMessage(msg, differing)
			raise self.failureException(msg)

	def getUniqueFilename(self):
		return str(uuid.uuid4())

