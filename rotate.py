import random

input = [ random.randint(1,50) for i in range(10)]

k = 2



print('initial list')

for i in range(len(input)):
    print(input[i])

print('-----------------------------')

while k >0:
    current = input[0]
    for i in range(len(input)-1,-1,-1):
        current,input[i] = input[i],current
    k-=1


print('after rotating')
print('-----------------------------')

for i in range(len(input)):
    print(input[i])    
