import sys, os, subprocess, tempfile 
import iperione
    
class Test_TestCase(iperione.TestCase):
    def setUp(self):
        self.setExpectedPath(os.path.join(os.path.dirname(__file__), 'content'))
        self.setResultPath(os.path.join(os.path.dirname(__file__), 'content'))
        self.inputPath = os.path.join(os.path.dirname(__file__), 'content')
        self.commandPath = os.path.join(os.path.dirname(__file__), 'content')
        
    def test_audio_same_files(self):
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_1sec_44100_16bits.wav")

    def test_audio_different_files_duration(self):
        self.assertRaises(AssertionError,  self.assertAudioFileEqual,  "sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_2sec_44100_16bits.wav")

    def test_audio_different_audio_file(self):
        self.assertRaises(AssertionError,  self.assertAudioFileEqual,  "sine_440Hz_1sec_44100_16bits.wav",  "square_440Hz_1sec_44100_16bits.wav")
        
    def test_txt_same_file(self):
        self.assertTxtFileEqual("dummy.txt",  "dummy.txt")
        
    def test_txt_different_file(self):
        self.assertRaises(AssertionError,  self.assertTxtFileEqual,  "dummy.txt",  "dummy2.txt")

if __name__ == "__main__":
    iperione.main()
