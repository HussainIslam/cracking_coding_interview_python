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
    if abs(len(string_one) - len(string_two)) > 1:
        return False
    if len(set(string_one) - set(string_two)) > 1:
        return False
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
