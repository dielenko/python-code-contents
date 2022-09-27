def make_array_consecutive2(x):
    
    count = 0

    x.sort()
    
    for a in range(0, len(x)):
        iterate = 1
        
        if a + 1 >= len(x):
            break
        
        for b in range(a + 1, a + 2):
            
            if not ((x[a] + 1) == x[b]):
                
                while True:
                    
                    if ((x[a] + iterate) == x[b]):
                        break
                    iterate += 1
                    count += 1

    return(count)

input_user = [6, 2, 3, 8]
input(make_array_consecutive2(input_user))