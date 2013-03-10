"""
Copyright (C) 2013 Alessandro Siniscalchi <asiniscalchi@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
"""

import os,  unittest
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

    def assertAudioFileEqual(self,  expected, result, msg=None):
        comparator = ComparatorAudio()
        self._runComparator(comparator,  expected,  result)
        self._analizeDiff(comparator,  msg)
            
    def assertTxtFileEqual(self,  expected,  result,  msg=None):
        comparator = ComparatorTxt()
        self._runComparator(comparator,  expected,  result)
        self._analizeDiff(comparator,  msg)
        
    def _runComparator(self, comparator,  expected,  result):
        expectedPath = os.path.join(self._expectedPath, expected)
        comparator.setExpected(expectedPath)
        resultPath = os.path.join(self._resultPath, result)
        comparator.setResult(resultPath)
        comparator.run()
        
    def _analizeDiff(self,  comparator,  msg=None):
        if comparator.diff:
            differing = "Files are different:\n"
            for line in comparator.diff:
                differing += line
            msg = self._formatMessage(msg, differing)
            raise self.failureException(msg)
        
