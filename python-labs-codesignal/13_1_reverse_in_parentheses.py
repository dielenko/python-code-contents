# https://chrisaor.github.io/algorithm/2018/03/13/Algorithm_ReverseParentheses.html


def reverseParentheses(s):
    def reverse(list1):
        list1 = list1[::-1]
        for i in range(len(list1)):
            if list1[i] == "(":
                list1[i] = ")"
            elif list1[i] == ")":
                list1[i] = "("
        return list1

    s_list = list(s)
    cnt = 0
    start = 0
    end = 0
    i = 0
    while i < len(s_list):
        if s_list[i] == "(":
            pass
            if cnt == 0:
                cnt += 1
                start = i
            else:
                cnt += 1
        elif s_list[i] == ")":
            cnt -= 1
            if cnt == 0:
                end = i
                s_list = (
                    s_list[:start]
                    + reverse(s_list[start + 1 : end])
                    + s_list[end + 1 :]
                )
        i += 1
    s = "".join(s_list)
    if "(" in s_list:
        return reverseParentheses(s)
    else:
        return s


input_user = "foo(bar(baz))blim"
print(reverseParentheses(input_user))
