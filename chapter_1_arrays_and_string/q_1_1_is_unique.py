"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""


def checK_unique_chacters_in_string(target_string: str):
    character_set = set()
    for character in list(target_string):
        if character in character_set:
            return False
        else:
            character_set.add(character)
    return True


print(checK_unique_chacters_in_string("test"))
print(checK_unique_chacters_in_string("tag"))
print(checK_unique_chacters_in_string("trouble"))


