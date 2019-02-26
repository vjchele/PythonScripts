import base64
import hashlib
s = "AADEFGABEF"
longest = ''

'''
for i in range(len(s)):
    sub = ''
    temp_dict = {}
    for j in range(i, len(s)):
        if temp_dict.get(s[j],'') == '':
            temp_dict[s[j]] = s[j]
            sub += s[j]
            if len(sub) > len(longest):
                longest = sub
            continue
        break
'''

i, j =0,0
temp_dict = {}
tstr = s[i]

while (j < len(s)):
    if (temp_dict.get(s[j],'') == ''):
        temp_dict[s[j]] = s[j]
        tstr += s[j]
        j+=1
    else:
        temp_dict = {}
        if (len(tstr) > len(longest)):
            longest = tstr
        tstr = ''
        i = j
        j+=1
        
        
if (len(tstr) > len(longest)):
    longest = tstr  

print(longest)








    
