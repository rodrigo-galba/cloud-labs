import unittest
from model import operations


class TestSum(unittest.TestCase):

    def test_sum_operation(self):
        self.assertEqual(operations.sum_models(1, 2), 3, "should be equal")
        self.assertEqual(operations.sum_models(3, 4), 7, "should be equal")
        self.assertEqual(operations.sum_models(5, 6), 11, "should be equal")


if __name__ == '__main__':
    unittest.main()
