import sys, os, subprocess 
import iperione
    
class Test_TestCase(iperione.TestCase):
    def setUp(self):
	self.expectedPath = os.path.join(os.path.dirname(__file__), 'content')
	self.resultPath = os.path.join(os.path.dirname(__file__), 'content')
	self.inputPath = os.path.join(os.path.dirname(__file__), 'content')
	self.commandPath = os.path.join(os.path.dirname(__file__), 'content')
        
    def test_same_files(self):
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_1sec_44100_16bits.wav")

    def test_different_files(self):
	self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_2sec_44100_16bits.wav")
    
    def test_copied_file(self):
        command = "python %s/copyfile.py %s/sine_440Hz_1sec_44100_16bits.wav %s/sine_440Hz_1sec_44100_16bits_copy.wav" % (self.commandPath, self.inputPath, self.resultPath) 
        self.execute(command)
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_1sec_44100_16bits_copy.wav")

if __name__ == "__main__":
    iperione.main()
