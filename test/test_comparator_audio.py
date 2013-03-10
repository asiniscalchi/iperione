import sys,  os,  iperione
from test_comparator import  Test_Comparator
from iperione.comparator_audio import ComparatorAudio

class Test_Comparator_audio(iperione.TestCase,  Test_Comparator):
    __test__ = True
    
    def setUp(self):
        self.comparator = ComparatorAudio()
        self.contentPath = os.path.join(os.path.dirname(__file__),  'content')
        self.file1 = os.path.join(self.contentPath,  'sine_440Hz_1sec_44100_16bits.wav')
        self.file2 = os.path.join(self.contentPath,  'square_440Hz_1sec_44100_16bits.wav')
        self.diffPath = os.path.join(self.contentPath,  'diff_result.wav')
        self.diffPathExpected = os.path.join(self.contentPath,  'diff.wav')
        
    def test_different_duration_files(self):
        self.comparator.setExpected(self.file1)
        self.comparator.setResult(self.file2)
        self.comparator.run()
        self.assertFalse(self.comparator == None)

if __name__ == "__main__":
    iperione.main()
