from fileidentifier import FileIdentifier 

import subprocess

class TestCase:
	def __init__(self):
		self.name = ""
		self.command = ""
		self.output = ""
		self.expected = ""
		self.diff = ""

	def run(self):
		fileIdentifier = FileIdentifier()
		mime_output = fileIdentifier.mime(self.output)
		mime_expected = fileIdentifier.mime(self.expected)

		if (mime_output == None) or (mime_expected == None):
			self.diff += self.output + " or " +  self.expected + " is not recognize"
			return

		if mime_output != mime_expected:
			self.diff += self.output + " " + self.expected + " differ in type"
			return
		subprocess.call(self.command, shell=True)

		

	def areEqual(self):
		if self.diff == "":
			return True
		return False

