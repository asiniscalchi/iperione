
class Suite:
	def __init__(self):
		self.name = ""
		self.inputPath = None
		self.outputPath = None
		self.expectedPath = None
		self.testCases = []

	def addTest(self, testCase):
		self.testCases.append(testCase)

	def run(self):
		for testCase in self.testCases:
			if self.inputPath:
				testCase.inputPath = self.inputPath
			testCase.run()


		
