"""
Implement a method to perform basic string compression using counts of repeated characters.
For example, the string aabccccaaa would become a2b1c5a3. If the "compressed" string would not become
smaller than the original string, your method should return the original string. You can assume
string has only uppercase and lowercase letters (a-z).
"""
import unittest


def string_compression(string: str = "") -> str:
    if len(string) > 2:
        sequence_counter = 1
        previous_character = None
        compressed_string = ""
        for index, character in enumerate(string.lower()):
            if previous_character != character:
                if index != 0 or len(string) - 1 == index:
                    compressed_string += f'{previous_character}{sequence_counter}'
                previous_character = character
                sequence_counter = 1
            else:
                sequence_counter += 1
            if index == len(string) - 1:
                compressed_string += f'{previous_character}{sequence_counter}'
        return compressed_string if len(compressed_string) < len(string) else string
    return string


class TestStringCompression(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(type(string_compression()), str)

    def test_use_cases(self):
        self.assertEqual(string_compression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(string_compression("aa"), "aa")
        self.assertEqual(string_compression("aabb"), "aabb")
        self.assertEqual(string_compression("aaabb"), "a3b2")


if __name__ == '__main__':
    unittest.main()