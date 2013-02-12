import sys,os
import iperione
from iperione.fileidentifier import FileIdentifier

class Test_FileIdentifier(iperione.TestCase):
	def setUp(self):
		self.fileIdentifier = FileIdentifier()

	def test_no_existent_file(self):
		mime = self.fileIdentifier.mime("noExistent")
		self.assertEqual(None, mime)
		
	def test_txt_file(self):
		mime = self.fileIdentifier.mime("./dummy.txt")
		self.assertEqual("text/plain", mime)

	def test_wav_file(self):
		mime = self.fileIdentifier.mime("./dummy.wav")
		self.assertEqual("audio/x-wav", mime)

if __name__ == "__main__":
    unittest.main()

