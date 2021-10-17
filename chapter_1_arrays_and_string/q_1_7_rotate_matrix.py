"""
Given an image represented by NxN matrix, where each pixel in an image is represented by an integer,
write a method to rotate the image by 90 degrees. Can you do this in place?

The solution is inspired by https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
"""
import unittest


def rotate_matrix(matrix: list = None) -> list:
    if matrix is None:
        matrix = []
    max_dimension = len(matrix) - 1
    pivot_point = len(matrix) // 2
    for r_index in range(0, pivot_point):
        for c_index in range(r_index, max_dimension - r_index):
            temp = matrix[r_index][c_index]
            matrix[r_index][c_index] = matrix[max_dimension - c_index][r_index]
            matrix[max_dimension - c_index][r_index] = matrix[max_dimension - r_index][max_dimension - c_index]
            matrix[max_dimension - r_index][max_dimension - c_index] = matrix[c_index][max_dimension - r_index]
            matrix[c_index][max_dimension - r_index] = temp
    return matrix


class TestRotateImage(unittest.TestCase):
    def setUp(self) -> None:
        self.single_unit_matrix = [
            [11]
        ]
        self.single_unit_matrix_rotated = [
            [11]
        ]
        self.two_unit_matrix = [
            [11, 12],
            [21, 22]
        ]
        self.two_unit_matrix_rotated = [
            [21, 11],
            [22, 12]
        ]
        self.three_unit_matrix = [
            [11, 12, 13],
            [21, 22, 23],
            [31, 32, 33]
        ]
        self.three_unit_matrix_rotated = [
            [31, 21, 11],
            [32, 22, 12],
            [33, 23, 13]
        ]
        self.four_unit_matrix = [
            [11, 12, 13, 14],
            [21, 22, 23, 24],
            [31, 32, 33, 34],
            [41, 42, 43, 44]
        ]
        self.four_unit_matrix_rotated = [
            [41, 31, 21, 11],
            [42, 32, 22, 12],
            [43, 33, 23, 13],
            [44, 34, 24, 14]
        ]
        self.five_unit_matrix = [
            [11, 12, 13, 14, 15],
            [21, 22, 23, 24, 25],
            [31, 32, 33, 34, 35],
            [41, 42, 43, 44, 45],
            [51, 52, 53, 54, 55]
        ]
        self.five_unit_matrix_rotated = [
            [51, 41, 31, 21, 11],
            [52, 42, 32, 22, 12],
            [53, 43, 33, 23, 13],
            [54, 44, 34, 24, 14],
            [55, 45, 35, 25, 15]
        ]

    def test_single_unit_matrix(self):
        self.assertEqual(rotate_matrix(self.single_unit_matrix), self.single_unit_matrix_rotated)

    def test_two_unit_matrix(self):
        self.assertEqual(rotate_matrix(self.two_unit_matrix), self.two_unit_matrix_rotated)

    def test_three_unit_matrix(self):
        self.assertEqual(rotate_matrix(self.three_unit_matrix), self.three_unit_matrix_rotated)

    def test_four_unit_matrix(self):
        self.assertEqual(rotate_matrix(self.four_unit_matrix), self.four_unit_matrix_rotated)

    def test_five_unit_matrix(self):
        self.assertEqual(rotate_matrix(self.five_unit_matrix), self.five_unit_matrix_rotated)


if __name__ == '__main__':
    unittest.main()
