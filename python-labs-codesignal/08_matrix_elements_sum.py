# https://chrisaor.github.io/algorithm/2018/01/30/Algorithm_MatrixElementsSum.html
# https://stackoverflow.com/questions/58015774/remove-is-removing-elements-from-both-variables-lists-which-i-set-equal-to
# https://www.codementor.io/@arch/variable-references-in-python-u9z8j2gk0
def matrix_elements_sum(r_matrix):
    sum_matrix = 0

    haunted_room = []
    for i in range(0, len(r_matrix)):
        for j in range(len(r_matrix[0])):
            if r_matrix[i][j] == 0:
                haunted_room.append(j)
        for k in range(len(r_matrix[0])):

            if k not in haunted_room:
                sum_matrix += r_matrix[i][k]

    return sum_matrix


input_user = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]
print(matrix_elements_sum(input_user))
