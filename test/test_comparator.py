import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.comparator import Comparator
import unittest

class Test_Comparator(unittest.TestCase):
	def setUp(self):
		self.comparator = Comparator()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_set_no_existent_file(self):
		self.assertRaises(IOError, self.comparator.setExpected, ("noExistent"))
		self.assertRaises(IOError, self.comparator.setResult, ("noExistent"))

	def test_set_existent_file(self):
		self.comparator.setExpected(self.contentPath + "/dummy.wav")
		self.comparator.setResult(self.contentPath + "/dummy.wav")
	
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Comparator)
unittest.TextTestRunner(verbosity=2).run(suite)
