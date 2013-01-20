import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.comparator_txt import Comparator_txt
import unittest

class Test_Comparator_txt(unittest.TestCase):
	def setUp(self):
		self.comparator = Comparator_txt()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_equal_files(self):
		self.comparator.setExpected(self.contentPath + "/dummy.txt")
		self.comparator.setResult(self.contentPath + "/dummy.txt")
		self.comparator.run()
		self.assertTrue(self.comparator.areEqual())

	def test_different_files(self):
		self.comparator.setExpected(self.contentPath + "/dummy.txt")
                self.comparator.setResult(self.contentPath + "/dummy2.txt")
		self.comparator.run()
                self.assertFalse(self.comparator.areEqual())

if __name__ == "__main__":
    unittest.main()
