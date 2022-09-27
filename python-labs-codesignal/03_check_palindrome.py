def check_palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

input_user = input('Add expression: ')
print(check_palindrome(input_user))