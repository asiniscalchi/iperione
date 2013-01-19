import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest
from iperione import TestCase, Suite

class Test_Suite(unittest.TestCase):
	def setUp(self):
		self.suite = Suite()
		self.contentPath = os.path.dirname(__file__) + "/content/"

	def test_default(self):
		self.assertEqual("", self.suite.name)
		self.assertEqual("", self.suite.expectedsPath)
		self.assertEqual("", self.suite.outputsPath)

	def test_run(self):
		self.suite.outputsPath = self.contentPath
		self.suite.expectedsPath = self.contentPath
		self.suite.addTest("1", "dummy.txt", "dummy.txt")
		self.suite.addTest("2", "dummy.txt", "dummy2.txt")
		self.suite.addTest("3", "sine_440Hz_1sec_44100_16bits.wav", "sine_440Hz_1sec_44100_16bits.wav")
		self.suite.addTest("4", "sine_440Hz_1sec_44100_16bits.wav", "sine_440Hz_2sec_44100_16bits.wav")
		self.suite.run()	
