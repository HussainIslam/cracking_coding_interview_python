"""
Given two strings, write a method to decide if one is a permutation of the other
"""
import unittest
from collections import Counter


def check_permutation_insensitive(string_one: str = "", string_two: str = "") -> bool:
    # This is case and whitespace insensitive
    # Pre-processing
    string_one = ''.join(sorted(string_one.replace(" ", "").lower()))
    string_two = ''.join(sorted(string_two.replace(" ", "").lower()))
    return string_one == string_two


def check_permutation_sensitive(string_one: str = "", string_two: str = "") -> bool:
    # This is case and whitespace sensitive
    if len(string_one) != len(string_two):
        return False
    return sorted(string_one) == sorted(string_two)


def check_permutation_character_count_sensitive(string_one: str = "", string_two: str = "") -> bool:
    # This is case and whitespace sensitive
    if len(string_one) != len(string_two):
        return False
    grand_total = 0
    for index in range(len(string_one)):
        grand_total += ord(string_one[index])
        grand_total -= ord(string_two[index])
    return True if grand_total == 0 else False


def check_permutation_using_counter_sensitive(string_one: str = "", string_two: str = "") -> bool:
    # This is case and whitespace sensitive
    if len(string_one) != len(string_two):
        return False
    return Counter(string_one) == Counter(string_two)


class TestCheckPermutation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.true_data_sets_sensitive = [
            ("empty", "tyemp"),
            ("abcd", "dcba"),
            ("Doll", "lloD"),
            ("White", "hWite"),
            ("This is a long line", "This is a long line"),
        ]
        cls.false_data_sets_sensitive = [
            ("emtpy", "mpty"),
            ("done", "one"),
            ("This is a long line", "This is a long   line"),
            ("This is a long long line", "ThiS is a long Long line"),
        ]
        cls.true_data_sets_insensitive = [
            ("ABCD", "abcd"),
            ("asdf", "ASDF"),
            ("Line", "linE"),
            ("This is a long line", "this is a longline"),
            ("This is a long line", "thiS is a    long    line"),
        ]
        cls.false_data_sets_insensitive = [
            ('abcd', 'line'),
            ("abcd", "bcd"),
            ("this is a long line", "this is a long line with space"),
            ("Rabbit", "R@bbit"),
            ("Rabbit", "Rabit"),
        ]
        cls.methods = [
            'check_permutation_insensitive',
            'check_permutation_sensitive',
            'check_permutation_character_count_sensitive',
            'check_permutation_using_counter_sensitive',
        ]

    def test_check_permutation(self):
        for method in self.methods:
            print(f"------------------ TESTING: {method} ------------------")
            print("------------------ Testing whether True ------------------")
            if "insensitive" in method:
                true_data_set = self.true_data_sets_insensitive
                false_data_set = self.false_data_sets_insensitive
            else:
                true_data_set = self.true_data_sets_sensitive
                false_data_set = self.false_data_sets_sensitive
            for data_set in true_data_set:
                print(f"Test: '{data_set[0]}' with '{data_set[1]}")
                self.assertTrue(globals()[method](data_set[0], data_set[1]))
            print("------------------ Testing whether False ------------------")
            for data_set in false_data_set:
                print(f"Test: '{data_set[0]}' with '{data_set[1]}")
                self.assertFalse(globals()[method](data_set[0], data_set[1]))


if __name__ == '__main__':
    unittest.main()

