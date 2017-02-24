'''
Created on 24.02.2017

@author: steinorb
'''
import unittest.mock
import waehlen
import builtins


class WaehlenTest(unittest.TestCase):


    @unittest.mock.patch('builtins.input')
    def testAuswahl(self, mock_input):
        mock_input.return_value = "1"
        auswahl = waehlen.auswahl()
        self.assertEqual(auswahl, 1)


if __name__ == "__main__":
    unittest.main()