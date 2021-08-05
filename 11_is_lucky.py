# https://stackoverflow.com/questions/4789601/split-a-string-into-2-in-python/4789617
# https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

""" Task descrition:
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.
"""


def is_lucky(n):

    number_list = []

    for digit in str(n):
        number_list.append(int(digit))

    firstpart = number_list[: int(len(number_list) / 2)]
    secondpart = number_list[int(len(number_list) / 2) :]

    if sum(firstpart) == sum(secondpart):
        return True
    else:
        return False


user_input = int(input("Add ticket number: "))
print(is_lucky(user_input))
