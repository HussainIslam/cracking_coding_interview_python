"""
Given two strings, write a method to decide if one is a permutation of the other
"""
import unittest


def check_permutation_case_whitespace_insensitive(string_one: str = "", string_two: str = "") -> bool:
    # Pre-processing
    string_one = ''.join(sorted(string_one.replace(" ", "").lower()))
    string_two = ''.join(sorted(string_two.replace(" ", "").lower()))
    return string_one == string_two


def check_permutation_case_whitespace_sensitive(string_one: str = "", string_two: str = "") -> bool:
    if len(string_one) != len(string_two):
        return False
    return sorted(string_one) == sorted(string_two)


def check_permutation_character_count(string_one: str = "", string_two: str = "") -> bool:
    if len(string_one) != len(string_two):
        return False
    letters = [0] * 128
    grand_total = 0
    for index in range(len(string_one)):
        grand_total += letters[ord(string_one[index])]
        grand_total -= letters[ord(string_two[index])]
    print(grand_total)
    return True if grand_total == 0 else False


class TestCheckPermutation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.true_data_sets = [
            ("empty", "tyemp"),
            ("abcd", "dcba"),
        ]
        cls.false_data_sets = [
            ('abcd', 'line'),
            ("abcd", "bcd"),
            ("this is a long line", "this is a long line with space"),
            ("This is a long line", "this   is a long line"),
            ("Rabbit", "R@bbit"),
            ("Rabbit", "Rabit"),
            ("Rabbit", "rabbit"),
        ]
        cls.methods = [
            'check_permutation_character_count',
            'check_permutation_case_whitespace_insensitive',
            'check_permutation_case_whitespace_sensitive',
        ]

    def test_check_permutation(self):
        for method in self.methods:
            print(f"------------------ TESTING: {method} ------------------")
            print("------------------ Testing whether True ------------------")
            for data_set in self.true_data_sets:
                print(f"Test: '{data_set[0]}' with '{data_set[1]}")
                self.assertTrue(globals()[method](data_set[0], data_set[1]))
            print("------------------ Testing whether False ------------------")
            for data_set in self.false_data_sets:
                print(f"Test: '{data_set[0]}' with '{data_set[1]}")
                self.assertFalse(globals()[method](data_set[0], data_set[1]))


if __name__ == '__main__':
    unittest.main()

