import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.comparator_audio import Comparator_audio
import unittest

class Test_Comparator_audio(unittest.TestCase):
	def setUp(self):
		self.comparator = Comparator_audio()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_same_file(self):
		self.comparator.setExpected(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.comparator.setResult(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.assertTrue(self.comparator.areEqual)

	def test_different_duration_files(self):
		self.comparator.setExpected(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.comparator.setResult(self.contentPath + "/sine_440Hz_2sec_44100_16bits.wav")
                self.assertFalse(self.comparator.areEqual)
		self.assertEqual(self.comparator.diff_nSamples, 44100)
		
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Comparator_audio)
unittest.TextTestRunner(verbosity=2).run(suite)
