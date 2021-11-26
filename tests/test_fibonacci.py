import unittest
import math
from src.utils import fibonacci

class TestUtils(unittest.TestCase):

    def test_fib10(self):
        number = fibonacci(10)
        self.assertEqual(number, 55)
    
    def test_fibNeg(self):
        number = fibonacci(-10)
        self.assertEqual(number, math.inf)
    

if __name__ == '__main__':
    unittest.main()