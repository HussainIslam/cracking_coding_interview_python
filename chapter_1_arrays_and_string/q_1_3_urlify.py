"""
Write a method to replace all space in string with '%20'. You may assume that the string has sufficient space at the
end to hold the additional characters, and that you are given the 'true' length of the string. (Note: if implementing
in Java, please a character array so that you can perform this operation in place)
"""
import unittest


def urlify(url: str = "") -> str:
    if len(url) > 0:
        return ''.join(["%20" if character == " " else character for character in list(url)])
    return url


class TestURLify(unittest.TestCase):

    def test_return_type(self):
        self.assertEqual(type(urlify("test")), str)

    def test_no_parameter(self):
        self.assertEqual(urlify(), "")

    def test_use_cases(self):
        self.assertEqual(urlify("this  is  test"), "this%20%20is%20%20test")
        self.assertEqual(urlify("this is test"), "this%20is%20test")
        self.assertEqual(urlify("a "), "a%20")
        self.assertEqual(urlify(" abc"), "%20abc")


if __name__ == '__main__':
    unittest.main()
