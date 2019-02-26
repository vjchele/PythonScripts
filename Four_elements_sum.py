'''
Find four elements a, b, c and d in an array such that a+b = c+d
Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c and d are distinct elements. If there are multiple answers, then print any of them.

Example:

Input:   {3, 4, 7, 1, 2, 9, 8}
Output:  (3, 8) and (4, 7)
Explanation: 3+8 = 4+7

Input:   {3, 4, 7, 1, 12, 9};
Output:  (4, 12) and (7, 9)
Explanation: 4+12 = 7+9

Input:  {65, 30, 7, 90, 1, 9, 8};
Output:  No pairs found
Expected Time Complexity: O(n2)
'''
l = [3,4,7,1,2,9,8]

sum_dict = {}

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] in sum_dict:
            print(sum_dict[l[i] + l[j]], (l[i],l[j]))
            break
        sum_dict[l[i] + l[j]] = (l[i],l[j])

    
