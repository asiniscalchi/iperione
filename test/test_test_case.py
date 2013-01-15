import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest, iperione

class Test_TestCase(unittest.TestCase):
	def setUp(self):
		self.testCase = iperione.TestCase()

	def test_default(self):
		self.assertEqual("", self.testCase.command)
		self.assertEqual("", self.testCase.output)
		self.assertEqual("", self.testCase.expected)
		self.assertEqual("", self.testCase.name)

	def test_run_copy_file(self):
		self.testCase.command = "python ./copyfile.py dummy.txt dummy_result.txt"
		self.testCase.output = "dummy_result.txt"
		self.testCase.expected = "dummy.txt"
		self.testCase.run()
		self.assertTrue(self.testCase.areEqual())
		
