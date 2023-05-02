import unittest
from square_shann.square_formula import square_formula


class TestSquareFormula(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(square_formula(2, 3), 25)
        self.assertEqual(square_formula(4, 1), 25)

    def test_negative_numbers(self):
        self.assertEqual(square_formula(-4, -2), 36)
        self.assertEqual(square_formula(-3, -3), 36)

    def test_mixed_numbers(self):
        self.assertEqual(square_formula(3, -1), 4)
        self.assertEqual(square_formula(-5, 2), 9)

    def test_zero(self):
        self.assertEqual(square_formula(0, 5), 25)
        self.assertEqual(square_formula(0, -5), 25)
        self.assertEqual(square_formula(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
