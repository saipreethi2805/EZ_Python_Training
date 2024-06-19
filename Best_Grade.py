#Best Grade

# Andrew has a string N consisting of lowercase English letters representing respective grades of N students in his class.
# His grade is at Pth index. He can swap any two adjacent grades.
# Your task is to help Andrew find and return a string value, 
# representing maximized grade by bringing lexicographically smallest character on the Pth index after doing at most K swaps I

# Sample Input:abcdefg
# 3
# 2
# Sample Output:
# a

n=input()
p=int(input())
k=int(input())
start=max(0,p-k-1)
end=min(len(n),p+k)
print(min(list(n[start:end])))