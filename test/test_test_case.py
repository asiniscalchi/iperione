import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest, iperione

class Test_TestCase(unittest.TestCase):
	def setUp(self):
		self.testCase = iperione.TestCase()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_default(self):
		self.assertEqual("", self.testCase.command)
		self.assertEqual("", self.testCase.output)
		self.assertEqual("", self.testCase.expected)
		self.assertEqual("", self.testCase.name)
		self.testCase.run()
		self.assertFalse(self.testCase.areEqual())

	def test_expected_unexistent(self):
		self.testCase.expected = "unexistent.wav"
		self.testCase.run()
		self.assertFalse(self.testCase.areEqual())

	def test_result_unexistent(self):
		self.testCase.result = "unexistent.wav"
                self.testCase.run()
                self.assertFalse(self.testCase.areEqual())

	def test_mime_result_expected_are_different(self):
		self.testCase.output = "unexistent.txt"
		self.testCase.expected = "unexistent.wav"
		self.testCase.run()
		self.assertFalse(self.testCase.areEqual())

	def test_mime_result_expected_are_the_same(self):
		self.testCase.output = "unexistent.txt"
		self.testCase.expected = "unexistent.txt"
		self.testCase.run()
		self.assertTrue(self.testCase.areEqual())

	def test_run_copy_file(self):
		self.testCase.command = "python " + self.contentPath + "/copyfile.py " + self.contentPath +"/dummy.txt " + self.contentPath + "/dummy_result.txt"
		self.testCase.output = "dummy_result.txt"
		self.testCase.expected = "dummy.txt"
		self.testCase.run()
		self.assertTrue(self.testCase.areEqual())
