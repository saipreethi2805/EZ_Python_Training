# 10) Magic String

# Eva has a string S containing lowercase English letters. 
# She wants to transform this string into a Magic String, where all the characters in the string are the same.
# To do so, she can replace any letter in the string with another letter present in that string. 6
# Your task is to help Eva find and return an integer value, representing the minimum number of steps required to form a Magic String. 
# Return O, if S is already a Magic String.
# Input Specification:
# input1: A string 5, containing lowercase English letters.
# Output Specification:Input Specification:
# Sample Input:
# aaabbbccdddd
# Sample Output:8h

S = input()
d = {}
for i in S:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
# print(d)
max = max(d.values())
min = len(S) - max

print(min)