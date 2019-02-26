'''
Remove duplicates from unsorted array
Given an unsorted array of integers, Print the array after removing the duplicate elements from it. We need to print distinct array elements according to their first occurrence.

Examples:

Input : arr[] = { 1, 2, 5, 1, 7, 2, 4, 2}
Output : 1 2 5 7 4
Explanation : {1, 2} appear more than one time.
'''

arr = [1,2,5,1,7,2,4,2]
temp_dict = {}

for i in range(len(arr)):
    if temp_dict.get(arr[i],'') == '' :
        temp_dict[arr[i]] = True
        print(arr[i])

        
