import os

class Comparator:
	def setExpected(self, url):
		if not os.path.exists(url):
			raise IOError(url + " doesn't exist")
		self.expected = url
		self._compare()

	def setResult(self, url):
		if not os.path.exists(url):
			raise IOError(url + " doesn't exist")
		self.result = url
		self._compare()

	def _compare(self):
		try:
			self._specializedCompare()
		except AttributeError:
			return


