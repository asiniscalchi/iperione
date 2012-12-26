import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.fileidentifier import FileIdentifier
import unittest

class Test_FileIdentifier(unittest.TestCase):
	def test_creation(self):
		fileIdentifier = FileIdentifier()

suite = unittest.TestLoader().loadTestsFromTestCase(Test_FileIdentifier)
unittest.TextTestRunner(verbosity=2).run(suite)
