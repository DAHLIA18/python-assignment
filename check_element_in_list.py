import unittest

def check_element_in_list(lst, element):
    return element in lst

class TestCheckElementInList(unittest.TestCase):

    def test_check_element_in_list_empty(self):
        result = check_element_in_list([], 5)
        self.assertFalse(result)  # Empty list should not contain any element

    def test_check_element_in_list_numbers(self):
        result = check_element_in_list([1, 2, 3, 4, 5], 3)
        self.assertTrue(result)  # List contains the element '3'

    def test_check_element_in_list_strings(self):
        result = check_element_in_list(['apple', 'banana', 'orange'], 'pear')
        self.assertFalse(result)  # List does not contain the element 'pear'

    def test_check_element_in_list_mixed_types(self):
        result = check_element_in_list([1, 'two', 3.0, [4, 5]], [4, 5])
        self.assertTrue(result)  # List contains the element [4, 5]

    def test_check_element_in_list_large_list(self):
        result = check_element_in_list(list(range(1000)), 999)
        self.assertTrue(result)  # List contains the element 999

if __name__ == '__main__':
    unittest.main()
