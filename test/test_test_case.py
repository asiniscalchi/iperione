import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest
from iperione import TestCase

class Test_TestCase(unittest.TestCase):
	def setUp(self):
		self.testCase = TestCase()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_default(self):
		self.assertEqual("", self.testCase.command)
		self.assertEqual("", self.testCase.output)
		self.assertEqual("", self.testCase.expected)
		self.assertEqual("", self.testCase.name)
		self.assertEqual("", self.testCase.expectedPath)
		self.assertEqual("", self.testCase.outputPath)
		self.assertEqual(None, self.testCase.diff)
		self.assertRaises(IOError, self.testCase.run)
		self.assertFalse(self.testCase.areEqual())

	def test_expected_unexistent(self):
		self.testCase.expected = "unexistent.wav"
		self.assertRaises(IOError, self.testCase.run)
		self.assertFalse(self.testCase.areEqual())

	def test_result_unexistent(self):
		self.testCase.result = "unexistent.wav"
                self.assertRaises(IOError, self.testCase.run)
		self.assertFalse(self.testCase.areEqual())

	def test_txt_same_unexistent_file(self):
		self.testCase.output = "unexistent.txt"
		self.testCase.expected = "unexistent.txt"
		self.assertRaises(IOError, self.testCase.run)
		self.assertFalse(self.testCase.areEqual())

	def test_txt_same_files(self):
		self.testCase.output = self.contentPath + "/dummy.txt"
		self.testCase.expected = self.contentPath + "/dummy.txt"
		self.testCase.run()
		self.assertTrue(self.testCase.areEqual())

	def test_txt_different_files(self):
		self.testCase.output = self.contentPath + "/dummy.txt"
		self.testCase.expected = self.contentPath + "/dummy2.txt"
		self.testCase.run()
		self.assertFalse(self.testCase.areEqual())

	def test_audio_same_files(self):
		self.testCase.output = self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav"
                self.testCase.expected = self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav"
                self.testCase.run()
                self.assertTrue(self.testCase.areEqual())

	def test_audio_same_files(self):
		self.testCase.output = self.contentPath + "/sine_440Hz_1sec_44100_16bits.wav"
                self.testCase.expected = self.contentPath + "/sine_440Hz_2sec_44100_16bits.wav"
                self.testCase.run()
                self.assertFalse(self.testCase.areEqual())

	def test_run_copy_file(self):
		self.testCase.command = "python " + self.contentPath + "/copyfile.py " + self.contentPath +"/dummy.txt " + self.contentPath + "/dummy_result.txt"
		self.testCase.output = self.contentPath + "/dummy_result.txt"
		self.testCase.expected = self.contentPath + "/dummy.txt"
		self.testCase.run()
		self.assertTrue(self.testCase.areEqual())

	def test_run_copy_file_using_paths(self):
		self.testCase.expectedPath = self.contentPath + '/'
		self.testCase.outputPath = self.contentPath + '/'
		self.testCase.command = "python " + self.contentPath + "/copyfile.py " + self.contentPath +"/dummy.txt " + self.contentPath + "/dummy_result.txt"
		self.testCase.output = "dummy_result.txt"
		self.testCase.expected = "dummy.txt"
		self.testCase.run()
		self.assertTrue(self.testCase.areEqual())

	def test_set_in_construction(self):
		testCase = TestCase(expected=self.contentPath + "/dummy.txt", output=self.contentPath + "/dummy.txt")
		testCase.run()

if __name__ == "__main__":
    unittest.main()
