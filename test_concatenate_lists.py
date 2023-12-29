import unittest

def concatenate_lists(list1, list2):
    return list1 + list2

class TestConcatenateLists(unittest.TestCase):
    def test_concatenate_lists(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(concatenate_lists(list1, list2), expected_result)

if __name__ == '__main__':
    unittest.main()
