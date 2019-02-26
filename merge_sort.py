
l1 = [1,1,1,2,3,12,14,18]
l2 = [1,5,6]

l3 = []

i = 0
j = 0

while (i < len(l1) and j<len(l2)):
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1

while(i < len(l1)):
    l3.append(l1[i])
    i+=1

while(j < len(l2)):
    l3.append(l2[j])
    j+=1



for i in range(len(l3)):
    print(l3[i])
    
    
