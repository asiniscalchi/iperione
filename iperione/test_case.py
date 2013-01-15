from fileidentifier import FileIdentifier 

class TestCase:
	def __init__(self):
		self.name = ""
		self.command = ""
		self.output = ""
		self.expected = ""

	def run(self):
		fileIdentifier = FileIdentifier()
		mime_output = fileIdentifier.mime(self.output)
		mime_expected = fileIdentifier.mime(self.expected)
		if mime_output != mime_expected:
			return True
		return False

	def areEqual(self):
		return False
		

