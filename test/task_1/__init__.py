import unittest
from task_1 import fill_spiral_matrix
from .fixtures import fixtures


class FillSpiralMatrixTest(unittest.TestCase):
    def test_n_1(self):
        self.assertEqual(fill_spiral_matrix(1), fixtures['1'])

    def test_n_2(self):
        self.assertEqual(fill_spiral_matrix(2), fixtures['2'])

    def test_n_5(self):
        self.assertEqual(fill_spiral_matrix(5), fixtures['5'])

    def test_n_6(self):
        self.assertEqual(fill_spiral_matrix(6), fixtures['6'])

    def test_n_10(self):
        self.assertEqual(fill_spiral_matrix(10), fixtures['10'])

    def test_n_20(self):
        self.assertEqual(fill_spiral_matrix(20), fixtures['20'])

    def test_n_1000(self):
        self.assertEqual(fill_spiral_matrix(1000), fixtures['1000'])

if __name__ == '__main__':
    unittest.main()