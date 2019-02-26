input = "123"

result = units = 0



for i in range(len(input)-1, -1,-1):
    
    result = result + ((10**units) * int(input[i]))
    units+=1

print(result)


    
    
