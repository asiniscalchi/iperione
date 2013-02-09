import sys, os, subprocess 
sys.path.insert(0,os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))

import iperione
    
class Test_TestCase(iperione.TestCase):
    def setUp(self):
	self.expectedsPath = os.path.join(os.path.dirname(__file__), 'content')
	self.resultsPath = os.path.join(os.path.dirname(__file__), 'content')
	self.inputPath = os.path.join(os.path.dirname(__file__), 'content')
        
    def test_same_files(self):
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_1sec_44100_16bits.wav")
    
    def test_copied_file(self):
        command = "python " + self.resultsPath + "/copyfile.py " + self.inputPath +"/sine_440Hz_1sec_44100_16bits.wav " + self.resultsPath + "/sine_440Hz_1sec_44100_16bits_copy.wav"
        self.execute(command)
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_1sec_44100_16bits_copy.wav")

if __name__ == "__main__":
    iperione.main()
