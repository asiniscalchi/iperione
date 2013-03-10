import sys,os
import iperione
from iperione.comparator_txt import ComparatorTxt
from test_comparator import  Test_Comparator

class Test_Comparator_txt(iperione.TestCase,  Test_Comparator):
    __test__ = True
    
    def setUp(self):
        self.comparator = ComparatorTxt()
        self.contentPath = os.path.dirname(__file__) + "/content"
        self.file1 = os.path.join(self.contentPath,  'dummy.txt')
        self.file2 = os.path.join(self.contentPath,  'dummy2.txt')

if __name__ == "__main__":
    iperione.main()
