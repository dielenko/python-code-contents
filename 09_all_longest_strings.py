def all_longest_strings(input_list):
    longest_strings = []

    max_element = max(input_list, key=len)

    for f_str in range(len(input_list)):

        if len(input_list[f_str]) == len(max_element):
            longest_strings.append(input_list[f_str])

    return longest_strings


input_user = ["aba", "aa", "ad", "vcd", "aba"]
print(all_longest_strings(input_user))
