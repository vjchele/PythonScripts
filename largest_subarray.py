'''
Largest subarray having sum greater than k
Given an array of integers and a value k, find length of largest subarray having sum greater than k.

Examples:

Input : arr[] = {-2, 1, 6, -3}, k = 5
Output : 2
Largest subarray with sum greater than
5 is  {1, 6}.

Input : arr[] = {2, -3, 3, 2, 0, -1}, k = 3
Output : 5
Largest subarray with sum greater than
3 is {2, -3, 3, 2, 0}.
'''

#arr = [-2,1,6,-3]
arr = [2,-3,3,2,0,-1]

k = 3

max_curr = -1000
max_global = -1
low_index = 0
high_index = 0

for i in range(len(arr)):
    
    max_curr = max(arr[i], max_curr + arr[i])
    print(max_curr)
    
    
    if (max_curr >= k) and (max_curr > max_global):
        max_global = max_curr
        #high_index = i
        #break
      

print("current global max is {}. Indices are {}, {}".format(max_global,low_index, high_index))
