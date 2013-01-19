from fileidentifier import FileIdentifier 
from comparator import Comparator
from comparator_txt import Comparator_txt
from comparator_audio import Comparator_audio

import subprocess

class TestCase:
	def __init__(self):
		self.name = ""
		self.command = ""
		self.output = ""
		self.expected = ""
		self.diff = None

	def run(self):
		fileIdentifier = FileIdentifier()
		mime_output = fileIdentifier.mime(self.output)
		mime_expected = fileIdentifier.mime(self.expected)
		comparator = self._getComparatorFromMime(mime_output)

		subprocess.call(self.command, shell=True)

		comparator.setExpected(self.expected)
		comparator.setResult(self.output)
		comparator.run()

		self.diff = comparator.diff

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

