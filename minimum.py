import random

#l = [random.randint(5,100) for i in range(10)]
l = [5,5,1,6,7,2]



print(l)
l[0],l[1] = min(l[0],l[1]), max(l[0],l[1])


for i in range(2,len(l)):
    l[0] = min(l[0],l[i])
    if l[i] > l[0]:
        l[1] =min(l[1],l[i])
    
   
        
print(l[0],l[1])
