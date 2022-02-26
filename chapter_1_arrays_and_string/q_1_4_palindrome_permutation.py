"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is s a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome doesn't need to be limited to just dictionary words.
You can ignore casing and non-letter characters.
Example:
    Input:  Tact Coa
    Output: True (permutation: taco cat, atco cta, etc
"""
import unittest
import string


def is_palindrome_permutation(input_string: str = "") -> bool:
    character_counter = {}
    input_string = input_string.replace(" ", "").lower()
    for character in list(input_string):
        character_counter[character] = 1 if character not in character_counter.keys() else character_counter[character] + 1
    characters_without_pair = 0
    for character, frequency in character_counter.items():
        if frequency % 2 == 1:
            characters_without_pair += 1
    return characters_without_pair <= 1


def is_palindrome_permutation_counter(input_string: str = "") -> bool:
    character_list = [0] * 26
    valid_characters = 0
    for character in input_string:
        if 65 <= ord(character) <= 90:
            character_list[ord(character) - 65] += 1
            valid_characters += 1
        if 97 <= ord(character) <= 122:
            character_list[ord(character) - 97] += 1
            valid_characters += 1
    odd_counter = 0
    for character_counter in character_list:
        if character_counter % 2:
            odd_counter += 1
            if odd_counter > 1:
                return False
    return True


class TestPalindromePermutation(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data_sets = [
            ("Tact Coa", True),
            ("tattarrattat", True),
            ("nothing", False),
            ("aabcb", True),
            ("aabccb", True),
            ("abcbd", False),
            ("bc", False),
            ("abcAb", True),
            ("A", True),
            ("1221", True),
            ("abcdef", False)
        ]
        cls.methods = [
            'is_palindrome_permutation',
            'is_palindrome_permutation_counter',
        ]

    def test_use_cases(self):
        for method in self.methods:
            print(f"--------------------- TESTING: {method} ---------------------")
            for data_set in self.data_sets:
                print(f"Test: {data_set[0]} == {data_set[1]}")
                assert globals()[method](data_set[0]) == data_set[1]


if __name__ == '__main__':
    unittest.main()
