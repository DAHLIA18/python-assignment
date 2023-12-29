import unittest

def reverse_list(lst):
    return lst[::-1]  # Reversing the list using list slicing

class TestReverseList(unittest.TestCase):

    def test_reverse_list_empty(self):
        result = reverse_list([])
        self.assertEqual(result, [])  # Empty list should remain unchanged when reversed

    def test_reverse_list_numbers(self):
        result = reverse_list([1, 2, 3, 4, 5])
        self.assertEqual(result, [5, 4, 3, 2, 1])  # Reversing a list of numbers

    def test_reverse_list_strings(self):
        result = reverse_list(['apple', 'banana', 'orange'])
        self.assertEqual(result, ['orange', 'banana', 'apple'])  # Reversing a list of strings

    def test_reverse_list_mixed_types(self):
        result = reverse_list([1, 'two', 3.0, [4, 5]])
        self.assertEqual(result, [[4, 5], 3.0, 'two', 1])  # Reversing a list with mixed types

    def test_reverse_list_large_list(self):
        result = reverse_list(list(range(1000)))
        self.assertEqual(result, list(range(999, -1, -1)))  # Reversing a large list

if __name__ == '__main__':
    unittest.main()
