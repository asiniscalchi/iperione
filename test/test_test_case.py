import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

import iperione
#import unittest
from iperione import TestCase # TODO remove
    
class Test_TestCase(iperione.TestCase):
    def setUp(self):
	self.expectedsPath = os.path.join(os.path.dirname(__file__), 'content')
	self.resultsPath = os.path.join(os.path.dirname(__file__), 'content')
        
    def test_equals(self):
        self.assertAudioFileEqual("sine_440Hz_1sec_44100_16bits.wav",  "sine_440Hz_1sec_44100_16bits.wav")
    
if __name__ == "__main__":
    iperione.main()
