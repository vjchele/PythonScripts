import random

input = [random.randint(1, 100) for i in range(100)]

def print_list(input):
    for i in range(len(input)):
        print(input[i])

print("input array before sorting...")
print_list(input)


for i in range(len(input)-1,0,-1):
    for j in range(0,i):
        if input[j] > input[j+1]:
            input[j],input[j+1] = input[j+1],input[j]
        

print("input array after sorting...")
print_list(input)


