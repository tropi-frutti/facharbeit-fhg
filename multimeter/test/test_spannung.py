'''
Created on 24.02.2017

@author: steinorb
'''
import unittest
import spannung
import globvar


class SpannungTest(unittest.TestCase):


    @unittest.mock.patch('read_arduino.read')
    def testName(self, mock_read):
        globvar.measure0 = 500
        result = spannung.spannung()
        self.assertAlmostEqual(result, 2.4437928)

if __name__ == "__main__":
    unittest.main()