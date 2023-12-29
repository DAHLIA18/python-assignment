import unittest

def find_largest_element(lst):
    if not lst:  
        return None
    
    largest = lst[0]  
    
    for element in lst:
        if element > largest:
            largest = element
    
    return largest

class TestFindLargestElement(unittest.TestCase):

    def test_find_largest_element_empty_list(self):
        result = find_largest_element([])
        self.assertIsNone(result)

    def test_find_largest_element_positive_numbers(self):
        result = find_largest_element([5, 3, 9, 12, 4])
        self.assertEqual(result, 12)

    def test_find_largest_element_negative_numbers(self):
        result = find_largest_element([-5, -3, -9, -12, -4])
        self.assertEqual(result, -3)

    def test_find_largest_element_float_numbers(self):
        result = find_largest_element([3.5, 2.0, 6.7, 4.2])
        self.assertEqual(result, 6.7)

    def test_find_largest_element_duplicate_numbers(self):
        result = find_largest_element([4, 4, 4, 4])
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
