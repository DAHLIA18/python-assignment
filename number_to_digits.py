import unittest

def number_to_digits(number):
    return [int(digit) for digit in str(number)]

class TestNumberToDigits(unittest.TestCase):
    def test_number_to_digits(self):
     
        self.assertEqual(number_to_digits(12345), [1, 2, 3, 4, 5])
        
       
        self.assertEqual(number_to_digits(0), [0])
        
        
        self.assertEqual(number_to_digits(-9876), [9, 8, 7, 6])

if __name__ == '__main__':
    unittest.main()
