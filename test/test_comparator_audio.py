import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import iperione
from iperione.comparator_audio import ComparatorAudio

class Test_Comparator_audio(iperione.TestCase):
	def setUp(self):
		self.comparator = ComparatorAudio()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_same_file(self):
		self.comparator.setExpected(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.comparator.setResult(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.comparator.run()
		self.assertTrue(self.comparator.areEqual())

	def test_different_duration_files(self):
		self.comparator.setExpected(self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav")
		self.comparator.setResult(self.contentPath + "/sine_440Hz_2sec_44100_16bits.wav")
		self.comparator.run()
                self.assertFalse(self.comparator.areEqual())

if __name__ == "__main__":
    unittest.main()
