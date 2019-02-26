def long_prefix(s1,s2):
    i = 0
    max_len = min(len(s1),len(s2))
    r = ''
    while (i < max_len):
        if s1[i] !=s2[i]:
            return r
        r = r + s1[i]
        i+=1

    return r


l = ["apple", "ape", "april"]

lprefix = ''
for i in range(1,len(l)):
    lprefix = long_prefix(l[i],l[i-1])
    if long_prefix == '':
        break

print(lprefix)
    
    
                  
                  
                  
