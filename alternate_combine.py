import unittest

def alternate_combine(list1, list2):
    combined = []
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        combined.append(list1[i])
        combined.append(list2[i])
    combined.extend(list1[min_len:] if len(list1) > len(list2) else list2[min_len:])
    return combined

class TestAlternateCombine(unittest.TestCase):
    def test_alternate_combine(self):
       
        self.assertEqual(alternate_combine([1, 2, 3], ['a', 'b', 'c']), [1, 'a', 2, 'b', 3, 'c'])
        
       
        self.assertEqual(alternate_combine([1, 2, 3, 4], ['a', 'b', 'c']), [1, 'a', 2, 'b', 3, 'c', 4])
        
       
        self.assertEqual(alternate_combine([1, 2], ['a', 'b', 'c', 'd']), [1, 'a', 2, 'b', 'c', 'd'])

if __name__ == '__main__':
    unittest.main()
