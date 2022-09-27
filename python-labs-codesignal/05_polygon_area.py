# Explanation: https://stackoverflow.com/questions/49270277/find-area-of-n-interesting-polygon
# Math method:
#> import math

#> def shapeArea(n):
#>    return math.pow(n, 2) + math.pow(n - 1, 2)


def shape_area(n):
    
    if not (n < 0):
        calc_area = (n * n)+((n-1)*(n-1))
        return calc_area

input_user = int(input('Add n as integer:'))
print(shape_area(input_user))