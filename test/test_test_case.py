import sys,os
sys.path.insert(0,os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))

print(sys.path[0])
import iperione
    
class Test_TestCase(iperione.TestCase):
    def setUp(self):
	self.expectedsPath = os.path.join(os.path.dirname(__file__), 'content')
	self.resultsPath = os.path.join(os.path.dirname(__file__), 'content')
	self.inputPath = os.path.join(os.path.dirname(__file__), 'content')
        
    def test_equal_audio_files(self):
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_1sec_44100_16bits.wav")

if __name__ == "__main__":
    iperione.main()
