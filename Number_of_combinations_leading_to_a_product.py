# Number of combinations leading to a product
# Problem Statement:
# You are given an array arr and a product m. Your task is to find the number of possible unique triplets whose product of elements is m.
# Input Format:
# The first line contains the integer, n
# The second line contains space seperated integers of the array, arr
# The third line contains the product m.
# The input will be read from the STDIN by the candidate
# Output Format:
# The output consists of a single integer, i.e. the count of unique triplets having product m.
# The output will be matched to the candidate's output printed on the STDOUT
# Example:
# Input:7
# 5 3 20 10 142
# 60
# Output:3
# Explanation:
# Product m:60
# Possible triplets for product m: (5,4,3), (20,3,1), (10,3,2)
# The count of unique triplets is 3. 

# n = int(input())  
# l = list(map(int, input().split()))  
# m = int(input())  
# l.sort()
# count = 0
# for i in range(n):
#     k = i + 1
#     j = n - 1
#     while k < j:
#         p = l[i] * l[k] * l[j]
#         if p == m:
#             count += 1
#             k += 1
#             j -= 1
#         elif p < m:
#             k += 1
#         else:
#             j -= 1
# print(count)