import os, subprocess, uuid
import unittest
from comparator_audio import ComparatorAudio
from comparator_txt import ComparatorTxt

main = unittest.main

class TestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName)
        self._expectedPath = str()
        self._resultPath = str()
        self._diffPath = str()

    def setExpectedPath(self, path):
        self._expectedPath = path

    def setResultPath(self, path):
        self._resultPath = path

    def getResultPath(self):
        return self._resultPath
        
    def getUniqueFilename(self):
        return str(uuid.uuid4())

    def execute(self, command, shell=False):
        subprocess.call(command, shell=shell)

    def assertAudioFileEqual(self,  expected, result, msg=None):
        comparator = ComparatorAudio()
        self._runComparator(comparator,  expected,  result)
        self._checkDiff(comparator,  msg)
            
    def assertTxtFileEqual(self,  expected,  result,  msg=None):
        comparator = ComparatorTxt()
        self._runComparator(comparator,  expected,  result)
        self._checkDiff(comparator,  msg)
        
    def _runComparator(self, comparator,  expected,  result):
        expectedPath = os.path.join(self._expectedPath, expected)
        comparator.setExpected(expectedPath)
        resultPath = os.path.join(self._resultPath, result)
        comparator.setResult(resultPath)
        comparator.run()
        
    def _checkDiff(self,  comparator,  msg=None):
        if comparator.diff:
            differing = "Files are different:\n"
            for line in comparator.diff:
                differing += line
            msg = self._formatMessage(msg, differing)
            raise self.failureException(msg)
        
