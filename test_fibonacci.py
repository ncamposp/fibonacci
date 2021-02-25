import unittest
import fibonacci

class TestFibonacci (unittest.TestCase):
  #
  def test_fibonacci(self):
    self.assertEqual(fibonacci.fibonacci(0), 0)
    self.assertEqual(fibonacci.fibonacci(1), 1)
    self.assertEqual(fibonacci.fibonacci(2), 1)
    self.assertEqual(fibonacci.fibonacci(3), 2)
    self.assertEqual(fibonacci.fibonacci(4), 3)
    self.assertEqual(fibonacci.fibonacci(5), 5)
    
if __name__ == '__main__':
  unittest.main()