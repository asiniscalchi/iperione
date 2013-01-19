
class Suite:
	def __init__(self):
		self.name = ""
		self.testCases = []

	def addTest(self, testCase):
		self.testCases.append(testCase)

	def run(self):
		for testCase in self.testCases:
			testCase.run()


		
