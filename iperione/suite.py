from test_case import TestCase

class Suite:
	def __init__(self):
		self.name = ""
		self.outputsPath = ""
		self.expectedsPath = ""
		self.testCases = []

	def addTest(self, name, expected, output, command=""):
		self.testCases.append(TestCase(name, expected, output, command))
	
	def addTestCase(self, testCase):
		self.testCases.append(testCase)

	def run(self):
		for testCase in self.testCases:
			testCase.outputPath = self.outputsPath
			testCase.expectedPath = self.expectedsPath
			testCase.run()


		
