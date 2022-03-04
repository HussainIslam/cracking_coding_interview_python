"""
There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Given two strings, write a function to check if they are one edit (or zero) away.
Example:
    Pale, Ple: True
    pales, pale: True
    pale, bale: True
    pale, bake: False
"""
import unittest


def is_one_away(string_one: str = "", string_two: str = "") -> bool:
    if len(string_one) == len(string_two):
        return is_one_replace_away(string_one, string_two)
    elif len(string_one) + 1 == len(string_two):
        return is_one_insert_away(string_one, string_two)
    elif len(string_one) - 1 == len(string_two):
        return is_one_insert_away(string_two, string_one)
    return False


def is_one_replace_away(string_one: str, string_two: str) -> bool:
    found_difference = False
    for index in range(len(string_one)):
        if string_one[index] != string_two[index]:
            if found_difference:
                return False
            found_difference = True
    return True


def is_one_insert_away(string_one: str, string_two: str) -> bool:
    index_one = 0
    index_two = 0
    while index_one < len(string_one) and index_two < len(string_two):
        if string_one[index_one] != string_two[index_two]:
            if index_one != index_two:
                return False
            index_two += 1
        else:
            index_one += 1
            index_two += 1
    return True


class TestOneAway(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(is_one_away()), bool)

    def test_use_cases(self):
        self.assertTrue(is_one_away("pale", "ple"))
        self.assertTrue(is_one_away("pales", "pale"))
        self.assertTrue(is_one_away("pale", "bale"))
        self.assertFalse(is_one_away("pale", "bake"))


if __name__ == '__main__':
    unittest.main()
