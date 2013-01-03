import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.comparator_wav import Comparator_wav
import unittest

class Test_Comparator_wav(unittest.TestCase):
	def setUp(self):
		self.comparator = Comparator_wav()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_equal_files(self):
		self.comparator.setExpected(self.contentPath + "/sine_1sec.wav")
		self.comparator.setResult(self.contentPath + "/sine_1sec.wav")
		self.assertTrue(self.comparator.areEqual())

	def test_different_files(self):
		self.comparator.setExpected(self.contentPath + "/sine_1sec.wav")
		self.comparator.setResult(self.contentPath + "/sine_2sec.wav")
                self.assertFalse(self.comparator.areEqual())
		
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Comparator_wav)
unittest.TextTestRunner(verbosity=2).run(suite)