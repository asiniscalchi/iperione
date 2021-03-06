import sys, os,  iperione
from test_comparator import  Test_Comparator
from iperione.comparator_txt import ComparatorTxt

class Test_Comparator_txt(iperione.TestCase,  Test_Comparator):
    __test__ = True
    
    def setUp(self):
        self.comparator = ComparatorTxt()
        self.contentPath = os.path.join(os.path.dirname(__file__),  'content')
        self.file1 = os.path.join(self.contentPath,  'dummy.txt')
        self.file2 = os.path.join(self.contentPath,  'dummy2.txt')
        self.diffPath = os.path.join(self.contentPath,  'diff_result.txt')
        self.diffPathExpected = os.path.join(self.contentPath,  'diff.txt')

if __name__ == "__main__":
    iperione.main()
