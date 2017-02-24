'''
Created on 24.02.2017

@author: steinorb
'''
import unittest.mock
import read_arduino
import globvar

class Test(unittest.TestCase):

    def setUp(self):
        globvar.measure0 = 0

    @unittest.mock.patch('read_arduino.serial.Serial')
    def testCorrectResult(self, mock_Serial):
        """
        Checks the correct parsing of the result
        """
        target = unittest.mock.MagicMock()
        mock_Serial.return_value = target
        target.readline.side_effect = [b'123 456 789 876 543 0 333 1023']
        read_arduino.read()
        self.assertEqual(123, globvar.measure0)

    @unittest.mock.patch('read_arduino.serial.Serial')
    def testCorruptedResult(self, mock_Serial):
        """
        Checks that a measurement is retried when garbaged data is read
        """
        target = unittest.mock.MagicMock()
        mock_Serial.return_value = target
        target.readline.side_effect = [b'123 4\x136 789 876 543 0 333 1023', b'321 456 789 876 543 0 333 1023']
        read_arduino.read()
        self.assertEqual(321, globvar.measure0)
            
    @unittest.mock.patch('read_arduino.serial.Serial')
    def testNoEndlessLoop(self, mock_Serial):
        """
        The read must not yield into an endless loop. After several retries a ValueError will be thrown
        """
        target = unittest.mock.MagicMock()
        mock_Serial.return_value = target
        target.readline.return_value = b'123 456'  # a shortened result should give a retry
        with self.assertRaises(ValueError):    # a value error should be raised after several tries
            read_arduino.read()

if __name__ == "__main__":
    unittest.main()