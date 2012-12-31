import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.comparator import Comparator
import unittest

class Test_Comparator(unittest.TestCase):
	def setUp(self):
		self.comparator = Comparator()

	def test_set_no_existent_file(self):
		self.assertRaises(IOError, self.comparator.setFile1, ("noExistent"))
		self.assertRaises(IOError, self.comparator.setFile2, ("noExistent"))
		
#suite = unittest.TestLoader().loadTestsFromTestCase(Test_Comparator)
#unittest.TextTestRunner(verbosity=2).run(suite)
