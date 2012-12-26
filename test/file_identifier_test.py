import unittest
#from iperione import fileidentifier

class FileIdentifierTest(unittest.TestCase):
	def test_creation(self):
		fileIdentifier = FileIdentifier()

suite = unittest.TestLoader().loadTestsFromTestCase(FileIdentifierTest)
unittest.TextTestRunner(verbosity=2).run(suite)
