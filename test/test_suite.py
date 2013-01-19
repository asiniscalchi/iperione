import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest
from iperione import TestCase, Suite

class Test_Suite(unittest.TestCase):
	def setUp(self):
		self.suite = Suite()

	def test_default(self):
		self.assertEqual("", self.suite.name)

	def test_add_test(self):
		self.suite.addTest(TestCase())
