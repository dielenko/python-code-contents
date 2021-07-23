def century_from_year(x):
    if x <= 100:
        return 1
    elif x % 100 == 0:
        even_year = x // 100
        return even_year
    else:
        odd_year = x // 100 + 1
        return odd_year

user_input = int(input('Add year: '))
print(century_from_year(1905))