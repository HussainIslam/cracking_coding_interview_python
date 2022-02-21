"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
structures?
"""
import sys
import unittest
import logging


def check_unique_characters_without_additional_data_structure(target_string: str = "") -> bool:
    length = len(target_string)
    for i in range(length):
        for j in range(i + 1, length):
            if target_string[i] == target_string[j]:
                return False
    return True


def check_unique_characters(target_string: str = "") -> bool:
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


def check_unique_characters_bitwise_operator(target_string: str = "") -> bool:
    # This assumes only lower case letters
    checker = 0
    for character in target_string:
        position = ord(character) - ord('a')
        # Bitwise shifts 1 by the position number, then bitwise ANDs with checker and then checks whether true
        if (checker & (1 << position)) > 0:
            return False
        # Bitwise shifts 1 by the position number, then Bitwise OR assigns to checker
        checker |= (1 << position)
    return True


class TestUniqueCharacters(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data_sets = [
            ("test", False),
            ("another", True),
            ("", True),
        ]
        cls.methods = [
            'check_unique_characters_without_additional_data_structure',
            'check_unique_characters',
            'check_unique_characters_bitwise_operator'
        ]

    def test_return_type(self):
        self.assertEqual(type(check_unique_characters_without_additional_data_structure("test")), bool)

    def test_unique_character(self):
        log = logging.getLogger("TestUniqueCharacters")
        for method in self.methods:
            log.debug(f"------------------ TESTING: {method} ------------------")
            for data in self.data_sets:
                log.debug(f"Test: '{data[0]}' with {data[1]}")
                self.assertEqual(globals()[method](data[0]), data[1])


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout)
    logging.getLogger("TestUniqueCharacters").setLevel(logging.DEBUG)
    unittest.main()
    