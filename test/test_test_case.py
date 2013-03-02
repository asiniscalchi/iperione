import sys, os, subprocess, tempfile 
import iperione
    
class Test_TestCase(iperione.TestCase):
    def setUp(self):
	self.expectedPath = os.path.join(os.path.dirname(__file__), 'content')
	self.resultPath = os.path.join(os.path.dirname(__file__), 'content')
	self.inputPath = os.path.join(os.path.dirname(__file__), 'content')
	self.commandPath = os.path.join(os.path.dirname(__file__), 'content')
        
    def test_same_files(self):
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_1sec_44100_16bits.wav")

    def test_different_files_duration(self):
        self.assertRaises(AssertionError,  self.assertAudioFileEqual,  "sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_2sec_44100_16bits.wav")

    def test_different_audio_file(self):
	self.assertRaises(AssertionError,  self.assertAudioFileEqual,  "sine_440Hz_1sec_44100_16bits.wav",  "square_440Hz_1sec_44100_16bits.wav")

    def test_copied_file(self):
	result = tempfile.NamedTemporaryFile().name
	command = [sys.executable, os.path.join(self.commandPath, "copyfile.py"), os.path.join(self.inputPath, "sine_440Hz_1sec_44100_16bits.wav"), os.path.join(self.resultPath, result)]
        self.execute(command)
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  result)

if __name__ == "__main__":
    iperione.main()
