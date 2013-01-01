import os

class Comparator:
	def setExpected(self, url):
		if not os.path.exists(url):
			raise IOError(url + " doesn't exist")
		self.expected = url

	def setObtained(self, url):
		if not os.path.exists(url):
			raise IOError(url + " doesn't exist")
		self.result = url

