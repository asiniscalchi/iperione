import os

class Comparator:
	def setFile1(self, url):
		if not os.path.exists(url):
			raise IOError(url + " doesn't exist")
		self.file1 = url

	def setFile2(self, url):
		if not os.path.exists(url):
			raise IOError(url + " doesn't exist")
		self.file2 = url

