'''
Sieve of Eratosthenes
Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.

Example:

Input : n =10
Output : 2 3 5 7 

Input : n = 20 
Output: 2 3 5 7 11 13 17 19
'''
n = 100
l = [ i for i in range(2,n)]

l[0] = l[1] = 0

for i in range(2,n):
    for j in range(i*2,n,i):
        if l[j] == 0:
            break
        l[j] = 0




for i in l:
    if i!=0:
        print(i)
        


