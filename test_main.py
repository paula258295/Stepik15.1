import unittest
from main import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-2, -7), -9)
        self.assertEqual(add_numbers(10, -3), 7)

if __name__ == '__main__':
    unittest.main()
