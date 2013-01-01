import os

class Comparator:
	def setExpected(self, url):
		if not os.path.exists(url):
			raise IOError(url + " doesn't exist")
		self.file1 = url

	def setObtained(self, url):
		if not os.path.exists(url):
			raise IOError(url + " doesn't exist")
		self.file2 = url

	def areEqual(self):
		return False

