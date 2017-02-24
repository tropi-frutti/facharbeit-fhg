'''
Created on 24.02.2017

@author: steinorb
'''
import unittest.mock
import read_arduino
import globvar


class Test(unittest.TestCase):


    @unittest.mock.patch('read_arduino.serial')
    def testCorrectResult(self, mock_serial):
        """
        Checks the correct parsing of the result
        """
        target = unittest.mock.MagicMock()
        target.readline.return_value = b'123 456 789 876 543 0 333 1023'
        mock_serial.Serial.return_value = target
        read_arduino.read()
        self.assertEqual(123, globvar.measure0)

    @unittest.mock.patch('read_arduino.serial')
    def testCorruptedResult(self, mock_serial):
        """
        Checks that an exception is raised when garbaged data is read
        """
        target = unittest.mock.MagicMock()
        target.readline.return_value = b'123 4\x136 789 876 543 0 333 1023'
        mock_serial.Serial.return_value = target
        with self.assertRaises(ValueError):
            read_arduino.read()

if __name__ == "__main__":
    unittest.main()