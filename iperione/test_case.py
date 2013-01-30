from fileidentifier import FileIdentifier 
from comparator import Comparator
from comparator_txt import Comparator_txt
from comparator_audio import Comparator_audio

import subprocess
import unittest

main = unittest.main

class TestCase(unittest.TestCase):
	def assertFileEqual(first, second, msg=None):
		print "Hello World"

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
