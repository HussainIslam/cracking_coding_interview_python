"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
"""
import unittest


def zero_matrix(matrix: list = None) -> list:
    if matrix is None:
        matrix = []
    zero_rows = set()
    zero_columns = set()
    for r_index, row in enumerate(matrix):
        for c_index, cell in enumerate(row):
            if cell == 0:
                zero_rows.add(r_index)
                zero_columns.add(c_index)

    for r_index in zero_rows:
        for c_index, cell in enumerate(matrix[r_index]):
            matrix[r_index][c_index] = 0

    for c_index in zero_columns:
        for r_index, row in enumerate(matrix):
            matrix[r_index][c_index] = 0

    return matrix


class TestZeroMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.one_zero = [
            [11, 12, 13, 14],
            [21, 22, 23, 24],
            [31, 32, 33, 0]
        ]
        self.one_zero_outcome = [
            [11, 12, 13, 0],
            [21, 22, 23, 0],
            [0, 0, 0, 0]
        ]
        self.two_zero = [
            [11, 12, 13, 14],
            [21, 0, 23, 24],
            [31, 32, 33, 0]
        ]
        self.two_zero_outcome = [
            [11, 0, 13, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.all_zero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.all_zero_outcome = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.one_unit_matrix = [
            [11]
        ]
        self.one_unit_matrix_outcome = [
            [11]
        ]

    def test_one_unit(self):
        self.assertEqual(zero_matrix(self.one_unit_matrix), self.one_unit_matrix_outcome)

    def test_one_zero_matrix(self):
        self.assertEqual(zero_matrix(self.one_zero), self.one_zero_outcome)

    def test_two_zero_matrix(self):
        self.assertEqual(zero_matrix(self.two_zero), self.two_zero_outcome)

    def test_all_zero_matrix(self):
        self.assertEqual(zero_matrix(self.all_zero), self.all_zero_outcome)


if __name__ == '__main__':
    unittest.main()
