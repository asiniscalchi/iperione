import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.comparator_wav import Comparator_wav
import unittest

class Test_Comparator_wav(unittest.TestCase):
	def setUp(self):
		self.comparator = Comparator_wav()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_same_file(self):
		self.comparator.setExpected(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.comparator.setResult(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.assertTrue(self.comparator.areEqual())

	def test_different_duration_files(self):
		self.comparator.setExpected(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.comparator.setResult(self.contentPath + "/sine_440Hz_2sec_44100_16bits.wav")
                self.assertFalse(self.comparator.areEqual())
		
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Comparator_wav)
unittest.TextTestRunner(verbosity=2).run(suite)
