# https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP
# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
# Given two arrays a and b, check whether they are similar.


def are_similar(list1, list2):

    count = 0
    list_a = []
    list_b = []

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
            list_a.append(list1[i])
            list_b.append(list2[i])

    if count == 0:
        return True

    elif count == 2:
        return set(list_a) == set(list_b)

    else:
        return False


input_user_a = [1, 2, 3]
input_user_b = [2, 1, 3]
print(are_similar(input_user_a, input_user_b))
