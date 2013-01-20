import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest, iperione

class TestIperione(unittest.TestCase):
	def test_execute(self):
		suite = iperione.Suite()

		content_path = os.path.dirname(__file__) + "/content/"
		suite.expectedsPath = content_path
		suite.outputsPath = content_path

		suite.addTest("test_same_dile", "dummy.txt", "dummy.txt")
		suite.addTest("test_different_files", "dummy.txt", "dummy2.txt")
		suite.addTest("test_different_audio_files", "sine_440Hz_1sec_44100_16bits.wav", "sine_440Hz_2sec_44100_16bits.wav")

		testCase = iperione.TestCase()
		testCase.command = "python " + content_path + "copyfile.py " + content_path +"dummy.txt " + content_path + "dummy_result.txt"
                testCase.output = "dummy_result.txt"
                testCase.expected = "dummy.txt"

		suite.addTestCase(testCase)

		suite.run()

if __name__ == "__main__":
    unittest.main()	
