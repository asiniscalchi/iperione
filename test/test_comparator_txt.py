import sys,os
import iperione
from iperione.comparator_txt import ComparatorTxt

class Test_Comparator_txt(iperione.TestCase):
    def setUp(self):
        self.comparator = ComparatorTxt()
        self.contentPath = os.path.dirname(__file__) + "/content"

    def test_equal_files(self):
        self.comparator.setExpected(self.contentPath + "/dummy.txt")
        self.comparator.setResult(self.contentPath + "/dummy.txt")
        self.comparator.run()
        self.assertTrue(self.comparator.areEqual())

    def test_different_files(self):
        self.comparator.setExpected(self.contentPath + "/dummy.txt")
        self.comparator.setResult(self.contentPath + "/dummy2.txt")
        self.comparator.run()
        self.assertFalse(self.comparator.areEqual())

if __name__ == "__main__":
    iperione.main()
