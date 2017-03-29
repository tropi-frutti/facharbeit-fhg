'''
Created on 24.02.2017

@author: steinorb
'''
import unittest.mock
import waehlen


class WaehlenTest(unittest.TestCase):


    @unittest.mock.patch('builtins.input') # mock the builtin input() method
    def testAuswahl(self, mock_input):
        mock_input.return_value = "1"
        auswahl = waehlen.auswahl()
        self.assertEqual(auswahl, 1)

    @unittest.mock.patch('builtins.input') # mock the builtin input() method
    def testAbstandwdhInt(self, mock_input):
        mock_input.return_value = "1"
        auswahl = waehlen.abstandwdh()
        self.assertEqual(auswahl, 1)

    @unittest.mock.patch('builtins.input') # mock the builtin input() method
    def testAbstandwdhFloat(self, mock_input):
        mock_input.return_value = "0.5"
        auswahl = waehlen.abstandwdh()
        self.assertEqual(auswahl, 0.5)

if __name__ == "__main__":
    unittest.main()