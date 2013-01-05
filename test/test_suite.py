import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest, iperione

class Test_Suite(unittest.TestCase):
	def setUp(self):
		self.suite = iperione.Suite()

	def test_set_name(self):
		self.suite.name = "Suite"

