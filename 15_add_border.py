# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
def add_border(matrix):

    new_rectangular = []
    first_line_stars = []
    last_line_stars = []

    list_items = len(matrix[0])

    for i in range(list_items + 2):
        first_line_stars.append("*")

        if i + 1 == list_items + 2:
            new_rectangular.append("".join(first_line_stars))

    for n in range(len(matrix)):
        mid_line_chars = "".join(["*", matrix[n], "*"])
        new_rectangular.append(mid_line_chars)
        mid_line_chars = ""

    for m in range(list_items + 2):
        last_line_stars.append("*")

        if m + 1 == list_items + 2:
            new_rectangular.append("".join(last_line_stars))

    return new_rectangular


input_user = ["abc", "ded"]
print(add_border(input_user))
