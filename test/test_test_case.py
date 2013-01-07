import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest, iperione

class Test_TestCase(unittest.TestCase):
	def setUp(self):
		self.testCase = iperione.TestCase()

	def test_run_copy_file(self):
		self.testCase.command = "python ./copyfile.py dummy.txt dummy_result.txt"
		
