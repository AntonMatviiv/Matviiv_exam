import unittest
from main import *

class TestFunctions(unittest.TestCase):

    def test_count_elements(self):
        self.assertEqual(count_elements([]), 0)
        self.assertEqual(count_elements([1]), 1)
        self.assertEqual(count_elements([1, 2, 3]), 3)
        self.assertEqual(count_elements(['a', 'b', 'c', 'd']), 4)

if __name__ == '__main__':
    unittest.main()
