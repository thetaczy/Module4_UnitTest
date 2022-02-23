""" TACAL MARTIN LANCE  """
import unittest

def multiply(x,y):

    return x*y

class TestMultiply(unittest.TestCase):

    def test(self):

        self.assertEqual(multiply(3,2),5)

if __name__ == '__main__':
    unittest.main()

    