import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from iperione.fileidentifier import FileIdentifier
import unittest

class Test_FileIdentifier(unittest.TestCase):
	def setUp(self):
		self.fileIdentifier = FileIdentifier()

	def test_no_existent_file(self):
		mime = self.fileIdentifier.mime("noExistent")
		self.assertEqual(None, mime[0])
		
	def test_txt_file(self):
		mime = self.fileIdentifier.mime("./dummy.txt")
		self.assertEqual("text/plain", mime[0])

	def test_wav_file(self):
		mime = self.fileIdentifier.mime("./dummy.wav")
		self.assertEqual("audio/x-wav", mime[0])

suite = unittest.TestLoader().loadTestsFromTestCase(Test_FileIdentifier)
unittest.TextTestRunner(verbosity=2).run(suite)
