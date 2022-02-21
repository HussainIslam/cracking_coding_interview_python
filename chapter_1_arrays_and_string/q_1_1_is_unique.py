"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
structures?
"""
import unittest


def check_unique_characters_without_additional_data_structure(target_string: str = "") -> bool:
    length = len(target_string)
    for i in range(length):
        for j in range(i + 1, length):
            if target_string[i] == target_string[j]:
                return False
    return True


def check_unique_characters(target_string: str) -> bool:
    # Assumes the characters set is ASCII and total number of unique characters is 128
    # Alternatively, we can assume Extended ASCII and 256 unique characters
    if len(target_string) > 128:
        return False
    character_set = [False] * 128
    for character in target_string:
        ascii_code = ord(character)
        if character_set[ascii_code]:
            return False
        character_set[ascii_code] = True
    return True


class TestUniqueCharacters(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(check_unique_characters_without_additional_data_structure("test")), bool)

    def test_unique_character_false_case(self):
        self.assertEqual(check_unique_characters_without_additional_data_structure("test"), False)

    def test_unique_character_true_case(self):
        self.assertEqual(check_unique_characters_without_additional_data_structure("another"), True)

    def test_unique_character_empty_string(self):
        self.assertEqual(check_unique_characters_without_additional_data_structure(""), True)

    def test_unique_character_no_string(self):
        self.assertEqual(check_unique_characters_without_additional_data_structure(), True)


if __name__ == '__main__':
    unittest.main()
    