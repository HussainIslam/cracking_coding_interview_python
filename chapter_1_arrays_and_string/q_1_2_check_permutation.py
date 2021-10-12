"""
Given two strings, write a method to decide if one is a permutation of the other
"""
import unittest


def check_permutation(string_one: str = "", string_two: str = "") -> bool:
    # Pre-processing
    string_one = ''.join(sorted(string_one.replace(" ", "").lower()))
    string_two = ''.join(sorted(string_two.replace(" ", "").lower()))
    return string_one == string_two


class TestCheckPermutation(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(check_permutation("test", "est")), bool)

    def test_no_parameter(self):
        self.assertTrue(check_permutation())

    def test_first_parameter(self):
        self.assertFalse(check_permutation(string_one="test"))

    def test_second_parameter(self):
        self.assertFalse(check_permutation(string_two="test"))

    def test_different_use_cases(self):
        self.assertTrue(check_permutation("empty", "tyemp"))
        self.assertTrue(check_permutation("abcd", "dcba"))
        self.assertFalse(check_permutation("abcd", "bcd"))
        self.assertTrue(check_permutation("This is a long line", "this   is a long line"))
        self.assertFalse(check_permutation("this is a long line", "this is a long line with space"))
        self.assertTrue(check_permutation("Rabbit", "rabbit"))
        self.assertFalse(check_permutation("Rabbit", "R@bbit"))
        self.assertFalse(check_permutation("Rabbit", "Rabit"))


if __name__ == '__main__':
    unittest.main()

