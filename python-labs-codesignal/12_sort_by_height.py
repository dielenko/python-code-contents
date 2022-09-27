# https://www.programiz.com/python-programming/methods/list/sort
# https://thispointer.com/python-how-to-insert-an-element-at-specific-index-in-list/
# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

"""
Some people are standing in a row in a park. 
There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!

Example
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]
"""


def sort_by_height(people):

    sort_list = []
    tree_list = []

    for item in range(len(people)):
        if people[item] == -1:
            tree_list.append(item)
        else:
            sort_list.append(people[item])

    sort_list.sort()
    for tree in range(len(tree_list)):
        sort_list.insert(tree_list[tree], -1)

    return sort_list


input_user = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sort_by_height(input_user))
