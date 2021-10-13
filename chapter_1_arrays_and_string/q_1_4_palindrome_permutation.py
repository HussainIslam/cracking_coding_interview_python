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


def is_palindrome_permutation(input_string: str = "") -> bool:
    character_counter = {}
    input_string = input_string.replace(" ", "").lower()
    if len(input_string) > 1:
        for character in list(input_string):
            character_counter[character] = 1 if character not in character_counter.keys() else character_counter[character] + 1
        characters_without_pair = 0
        for character, frequency in character_counter.items():
            if frequency % 2 == 1:
                characters_without_pair += 1
        return characters_without_pair <= 1
    return False


class TestPalindromePermutation(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(is_palindrome_permutation()), bool)

    def test_use_cases(self):
        self.assertEqual(is_palindrome_permutation("Tact Coa"), True)
        self.assertEqual(is_palindrome_permutation("tattarrattat"), True)
        self.assertEqual(is_palindrome_permutation("nothing"), False)
        self.assertEqual(is_palindrome_permutation("aabcb"), True)
        self.assertEqual(is_palindrome_permutation("aabccb"), True)
        self.assertEqual(is_palindrome_permutation("abcbd"), False)
        self.assertEqual(is_palindrome_permutation("bc"), False)
        self.assertEqual(is_palindrome_permutation("abcAb"), True)
        self.assertEqual(is_palindrome_permutation("A"), False)
        self.assertEqual(is_palindrome_permutation("1221"), True)


if __name__ == '__main__':
    unittest.main()
