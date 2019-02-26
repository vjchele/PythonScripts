import random

input = [random.randint(1, 100) for i in range(10)]


def print_list(input):
    for i in range(len(input)):
        print(input[i])

def quick_sort(input,l,r):

    
    if l > r:
        return

      
    pivot = input[r]
    i,j = l,r
     
    while (i < j):
        if input[i] < pivot:
            i+=1
            continue
        if input[j] >= pivot:
            j-=1
            continue

        if(i < j):
            input[i],input[j] = input[j], input[i]

    input[j], input[r] = input[r], input[j]


    quick_sort(input, l, j-1)
    quick_sort(input, j+1, r)
    

print("input array before sorting...")
print_list(input)

quick_sort(input,0,len(input)-1)


        

print("input array after sorting...")
print_list(input)
