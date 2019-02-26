'''
Ugly Numbers
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.

Examples:

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832

'''


num_dict = {1:1,2:2,3:3, 5:5} #setting the dictionary


try:
    n=int(input('Please the number n:'))
except ValueError:
    print("Not a number")


counter =1
ugly_number = 1
while (counter < n):
    if (num_dict.get(ugly_number/2,'') !='') or (num_dict.get(ugly_number/3,'') != '') or (num_dict.get(ugly_number/5,'') != '') :
        num_dict[ugly_number] = ugly_number
        counter+=1
        if (counter >= n): break
    ugly_number+=1
        

print("The {}th ugly number is {}".format(n, ugly_number))



