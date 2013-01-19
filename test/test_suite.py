import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest
from iperione import TestCase, Suite

class Test_Suite(unittest.TestCase):
	def setUp(self):
		self.suite = Suite()
		self.contentPath = os.path.dirname(__file__) + "/content"

	def test_default(self):
		self.assertEqual("", self.suite.name)
		self.assertEqual(None, self.suite.inputPath)
		self.assertEqual(None, self.suite.expectedPath)
		self.assertEqual(None, self.suite.outputPath)

	def test_add_test(self):
		self.suite.addTest(TestCase())

	def test_run(self):
		self.suite.run()
		self.suite.addTest(TestCase(expected=self.contentPath + "/dummy.txt", output=self.contentPath + "/dummy.txt"))
		self.suite.run()	
