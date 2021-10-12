"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""
import unittest


def check_unique_characters_in_string(target_string: str = "") -> bool:
    character_set = set()
    for character in list(target_string):
        if character in character_set:
            return False
        else:
            character_set.add(character)
    return True


class TestUniqueCharacters(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(check_unique_characters_in_string("test")), bool)

    def test_unique_character_false_case(self):
        self.assertEqual(check_unique_characters_in_string("test"), False)

    def test_unique_character_true_case(self):
        self.assertEqual(check_unique_characters_in_string("another"), True)

    def test_unique_character_empty_string(self):
        self.assertEqual(check_unique_characters_in_string(""), True)

    def test_unique_character_no_string(self):
        self.assertEqual(check_unique_characters_in_string(), True)


if __name__ == '__main__':
    unittest.main()
    