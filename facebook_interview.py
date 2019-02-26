import string
l = [ str(i) for i in range(1,27)]

s = string.ascii_lowercase

value_dict = dict(zip(l,s))

input = '123'

first, second = '',''

for i in range(len(input)):
    for j in range(i +1,len(input)+1):
        if value_dict.get(input[i:j],'') != '':
            print(value_dict[input[i:j]])

   



    


