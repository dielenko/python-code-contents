def adjacent_elements_product(x):
    y = []
    
    if len(x) > 2:
    
        for i in range(0, len(x)):
            print('Print loop element i: ', x[i])  
            
            if i + 2 == len(x):
                break

            for m in range(i + 1, i + 2):
                print('Print loop element m: ', x[m])  

                first_pair = x[i] * x[m]
                print('Print first_pair: ', first_pair)

                second_pair = x[i + 1] * x[m + 1]
                print('Print second_pair: ', second_pair)

                if first_pair >= second_pair:
                    y.append(first_pair)
                elif first_pair < second_pair:
                    y.append(second_pair)

        y.sort()
        return y[-1]
    else:
        return (x[0] * x[1])

input_user = [1, 0, 1, 0, 1000]
print(adjacent_elements_product(input_user))