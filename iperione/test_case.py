import os, subprocess
import unittest
from comparator_audio import Comparator_audio

main = unittest.main

class TestCase(unittest.TestCase):
	def __init__(self, methodName='runTest'):
		unittest.TestCase.__init__(self, methodName)
		self.expectedsPath = ""
		self.resultsPath = ""
		self.diffPath = ""

	def assertAudioFileEqual(self,  first, second, msg=None):
		comparator = Comparator_audio()

		expected = os.path.join(self.expectedsPath, first)
		comparator.setExpected(expected)

		result = os.path.join(self.resultsPath, second)
		comparator.setResult(result)

		comparator.run()

		if not comparator.areEqual():
			differing = "Files are different:\n"
			for line in comparator.diff:
				differing += line

			msg = self._formatMessage(msg, differing)
			raise self.failureException(msg)


	"""
        def __init__(self, name="", expected="", output="", command=""):
            self.name = name
            self.command = command
            self.output = output
            self.expected = expected
            self.outputPath = ''
            self.expectedPath = ''
            self.diff = None
    
        def run(self):
            fileIdentifier = FileIdentifier()
    
            output = self.outputPath + self.output
            expected = self.expectedPath + self.expected
    
            mime_output = fileIdentifier.mime(output)
            mime_expected = fileIdentifier.mime(expected)
            comparator = self._getComparatorFromMime(mime_output)
    
            subprocess.call(self.command, shell=True)
    
            comparator.setExpected(expected)
            comparator.setResult(output)
            comparator.run()
    
            self.diff = comparator.diff
    
            self._print()
    
        def areEqual(self):
            if self.diff is None:
                return False
            if self.diff:
                return False
            return True
    
        def _getComparatorFromMime(self, mime):
            if mime == "text/plain":
                return Comparator_txt()
            elif mime == "audio/x-wav":
                return Comparator_audio()
            return Comparator()
    
        def _print(self):
            for line in self.diff:
                print line
    """
