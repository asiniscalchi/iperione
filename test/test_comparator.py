import os,  uuid

class Test_Comparator(object):
    __test__ = False

    def test_set_no_existent_file(self):
        unexistentFile = str(uuid.uuid4())
        self.assertRaises(IOError, self.comparator.setExpected, unexistentFile)
        self.assertRaises(IOError, self.comparator.setResult, unexistentFile)

    def test_set_existent_file(self):
        self.comparator.setExpected(os.path.join(self.contentPath,  'dummy.wav'))
        self.comparator.setResult(os.path.join(self.contentPath,  'dummy.wav'))
        
    def test_same_file(self):
        self.comparator.setExpected(self.file1)
        self.comparator.setResult(self.file1)
        self.comparator.run()
        self.assertTrue(self.comparator.diff == None)
        
    def test_different_files(self):
        self.comparator.setExpected(self.file1)
        self.comparator.setResult(self.file2)
        self.comparator.run()
        self.assertFalse(self.comparator == None)
        
    def test_diff_creation(self):
        self.comparator.setExpected(self.file1)
        self.comparator.setResult(self.file2)
        self.comparator.setDiffPath(self.diffPath)
        self.comparator.run()
        self.assertTrue(os.path.exists(self.diffPath))
        self.comparator.setExpected(self.diffPath)
        self.comparator.setResult(self.diffPathExpected)
        self.comparator.run()
        self.assertTrue(self.comparator.diff == None)
        os.remove(self.diffPath)
    
if __name__ == "__main__":
    iperione.main()
