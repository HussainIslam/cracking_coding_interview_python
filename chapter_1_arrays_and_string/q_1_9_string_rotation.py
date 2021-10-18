"""
Assume you have a method isSubstring which checks if one is a substring of another. Give two strings
s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (eg "waterbottle"
is a rotation of "erbottlewat")
"""
import unittest


def is_substring(string_one: str = "", string_two: str = "") -> bool:
    string_one_counter = 0
    for string_two_counter, character in enumerate(string_two):
        while string_one[string_one_counter] == string_two[string_two_counter]:
            string_two_counter = string_two_counter + 1 if string_two_counter < len(string_two) - 1 else 0
            if string_one_counter < len(string_one) - 1:
                string_one_counter += 1
            else:
                return True
    return False


class TestIsSubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.one_letter = "a"
        self.one_letter_rotated = "a"
        self.two_letter = "ab"
        self.two_letter_rotated = "ba"
        self.use_case_one = "waterbottle"
        self.use_case_one_rotated_one = "erbottlewat"
        self.use_case_one_rotated_two = "bottlewater"
        self.use_case_one_rotated_three = "lewaterbott"
        self.use_case_one_wrong_one = "bttleowater"
        self.use_case_one_wrong_two = "obottle"

    def test_return_type(self):
        self.assertEqual(bool, type(is_substring()))

    def test_one_letter(self):
        self.assertTrue(is_substring(self.one_letter, self.one_letter_rotated))

    def test_two_letter(self):
        self.assertTrue(is_substring(self.two_letter, self.two_letter_rotated))

    def test_use_case_one(self):
        self.assertTrue(is_substring(self.use_case_one, self.use_case_one_rotated_one))

    def test_use_case_two(self):
        self.assertTrue(is_substring(self.use_case_one, self.use_case_one_rotated_two))

    def test_use_case_three(self):
        self.assertTrue(is_substring(self.use_case_one, self.use_case_one_rotated_three))

    def test_use_case_four(self):
        self.assertFalse(is_substring(self.use_case_one, self.use_case_one_wrong_one))

    def test_use_case_five(self):
        self.assertFalse(is_substring(self.use_case_one, self.use_case_one_wrong_two))


if __name__ == '__main__':
    unittest.main()
