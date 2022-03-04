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


def is_one_away_combined(string_one: str = "", string_two: str = "") -> bool:
    # if the absolute difference between the lengths of the strings is more than 1,
    # they are definitely more than one edit away
    if abs(len(string_one) - len(string_two)) > 1:
        return False
    if len(string_one) > len(string_two):
        long_string = string_one
        short_string = string_two
    else:
        long_string = string_two
        short_string = string_one
    index_long = 0
    index_short = 0
    found_difference = False
    while index_long < len(long_string) and index_short < len(short_string):
        if long_string[index_long] != short_string[index_short]:
            if found_difference:
                return False
            found_difference = True
            if len(long_string) == len(short_string):
                index_short += 1
        else:
            index_short += 1
        index_long += 1
    return True


class TestOneAway(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data_sets = [
            (("pale", "ple"), True),
            (("pales", "pale"), True),
            (("pale", "bale"), True),
            (("pale", "bake"), False)
        ]
        cls.methods = [
            'is_one_away',
            'is_one_away_combined',
        ]

    def test_use_cases(self):
        for method in self.methods:
            for data_set in self.data_sets:
                assert globals()[method](data_set[0][0], data_set[0][1]) == data_set[1]


if __name__ == '__main__':
    unittest.main()
