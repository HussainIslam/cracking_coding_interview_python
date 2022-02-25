"""
Write a method to replace all space in string with '%20'. You may assume that the string has sufficient space at the
end to hold the additional characters, and that you are given the 'true' length of the string. (Note: if implementing
in Java, please a character array so that you can perform this operation in place)
"""
import unittest


def urlify(url: str = "") -> str:
    return ''.join(["%20" if character == " " else character for character in url])


def urlify_reverse(url: str = "") -> str:
    encoded_url = ["%20"] * len(url)
    for index, character in enumerate(url):
        encoded_url[len(url) - index - 1] = "%20" if url[len(url) - index - 1] == " " else url[len(url) - index - 1]
    return ''.join(encoded_url)


class TestURLify(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.methods = [
            'urlify',
            'urlify_reverse',
        ]
        cls.data_sets = [
            ("this  is  test", "this%20%20is%20%20test"),
            ("this is test", "this%20is%20test"),
            ("a ", "a%20"),
            (" abc", "%20abc")
        ]

    def test_use_cases(self):
        for method in self.methods:
            print(f'-------------- TESTING: {method} --------------')
            for data_set in self.data_sets:
                print(f'Test: {data_set[0]}, {data_set[1]}')
                self.assertEqual(data_set[1], globals()[method](data_set[0]))


if __name__ == '__main__':
    unittest.main()
