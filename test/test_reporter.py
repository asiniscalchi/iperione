import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest
from iperione.reporter_junit import Reporter_junit

class Test_Reporter_junit(unittest.TestCase):
	def setUp(self):
		self.reporter = Reporter_junit()

	
