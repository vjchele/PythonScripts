l = [1,2,3,4,5,6]

d = 3

def ReverseArray(l, s, n):
    if (n-s) <= 2:
        print('s is {} and n is {} '.format(s,n))
        l[s],l[n-1] = l[n-1], l[s]
    else:
        for i in range(s,(s + n)//2):
            l[i],l[n-(1+i)] = l[n-(1+i)], l[i]
    
       
ReverseArray(l,0,len(l))
ReverseArray(l,0,len(l)-d)
ReverseArray(l,len(l)-d,len(l))

'''
for i in range(len(l)//2):
    l[i],l[len(l)-1-i] = l[len(l) -1 -i], l[i]
    
'''
for i in range(len(l)):
    print(l[i])




