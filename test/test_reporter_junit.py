import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import unittest
from iperione.reporter import Reporter

class Test_Reporter(unittest.TestCase):
	def setUp(self):
		self.reporter = Reporter()	
