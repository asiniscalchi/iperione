import sys,os
from iperione.comparator import Comparator

class Test_Comparator(object):
    def __init__(self):
        self.__test__ = False
        
    def setUp(self):
        self.comparator = Comparator()
        self.contentPath = os.path.dirname(__file__) + "/content"

    def test_set_no_existent_file(self):
        self.assertRaises(IOError, self.comparator.setExpected, ("noExistent"))
        self.assertRaises(IOError, self.comparator.setResult, ("noExistent"))

    def test_set_existent_file(self):
        self.comparator.setExpected(self.contentPath + "/dummy.wav")
        self.comparator.setResult(self.contentPath + "/dummy.wav")
    
if __name__ == "__main__":
    iperione.main()
