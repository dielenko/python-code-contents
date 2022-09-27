## https://stackoverflow.com/questions/5357460/python-regex-matching-a-parenthesis-within-parenthesis
# https://blog.finxter.com/python-regex-to-return-string-between-parentheses/
# https://www.geeksforgeeks.org/python-string-replace/
# https://www.geeksforgeeks.org/python-list-remove/
# https://www.geeksforgeeks.org/join-function-python/
# https://thispointer.com/python-how-to-insert-an-element-at-specific-index-in-list/
# https://www.geeksforgeeks.org/remove-multiple-elements-from-a-list-in-python/
# https://www.programiz.com/python-programming/methods/string/find
# https://stackoverflow.com/questions/38999344/extract-string-within-parentheses-python
# https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

"""
    Write a function that reverses characters in (possibly nested) parentheses in the input string.

    Input strings will always be well-formed with matching ()s.

    - For inputString = "(bar)", the output should be
        reverseInParentheses(inputString) = "rab";
        
    - For inputString = "foo(bar)baz", the output should be
        reverseInParentheses(inputString) = "foorabbaz";
        
    - For inputString = "foo(bar)baz(blim)", the output should be
        reverseInParentheses(inputString) = "foorabbazmilb";
        
    - For inputString = "foo(bar(baz))blim", the output should be
        reverseInParentheses(inputString) = "foobazrabblim".
        
    Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

"""
import re


def reverse_in_parentheses(input_string):
    double = True

    p_strings = re.findall("\(.*?\(.*?\)\)", input_string)

    if len(p_strings) == 0:
        p_strings = re.findall("\(.*?\)", input_string)
        double = False

    for el in p_strings:
        # TODO: Not working for "foo(bar(baz))blim"
        if double == True:
            double_str = "".join(p_strings)
            cut_str = re.findall("\(.*?\)", double_str)
            cut_str = "".join(cut_str)
            middle_str = re.sub(("[()]"), "", cut_str)
            sub_str = middle_str[::-1]
            input_string = re.sub(("[()]"), "", input_string)
            el = re.sub(("[()]"), "", el)
            input_string = re.sub(el, sub_str, input_string)
        else:
            modified_str = re.sub(("[()]"), "", el)
            modified_str = "".join(reversed(modified_str))
            input_string = re.sub(el, modified_str, input_string)

    return re.sub(("[()]"), "", input_string)


input_user = input("Add the initial string: ")
print(reverse_in_parentheses(input_user))
