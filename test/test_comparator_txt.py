import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.comparator_txt import Comparator_txt
import unittest

class Test_Comparator_txt(unittest.TestCase):
	def setUp(self):
		self.comparator = Comparator_txt()
		self.path = os.path.dirname(__file__)

	def test_compare(self):
		self.comparator.setExpected(self.path + "/dummy.wav")
		self.comparator.setObtained(self.path + "/dummy.wav")
		self.assertTrue(self.comparator.areEqual())
		
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Comparator_txt)
unittest.TextTestRunner(verbosity=2).run(suite)
