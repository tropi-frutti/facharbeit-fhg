'''
Created on 24.02.2017

@author: steinorb
'''
import unittest.mock
import waehlen


class WaehlenTest(unittest.TestCase):


    @unittest.mock.patch('__builtin__.input')
    def testAuswahl(self, mock_input):
        mock_input.return_value = "1"
        auswahl = waehlen.auswahl()
        self.assertEqual(auswahl, "1")


if __name__ == "__main__":
    unittest.main()