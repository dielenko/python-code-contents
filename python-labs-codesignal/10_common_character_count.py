# https://stackoverflow.com/questions/44269409/count-common-characters-in-strings-python
from collections import Counter


def common_character_count(str1, str2):

    common_chars = Counter(str1) & Counter(str2)
    return sum(common_chars.values())


input_user_1 = input("Add first string: ")
input_user_2 = input("Add second string: ")
print(common_character_count(input_user_1, input_user_2))
