import unittest
from addition import add_numbers

class TestAddition(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)  # Test case 1
        self.assertEqual(add_numbers(-1, 1), 0)  # Test case 2
        self.assertEqual(add_numbers(0, 0), 0)  # Test case 3

if __name__ == '__main__':
    unittest.main()
