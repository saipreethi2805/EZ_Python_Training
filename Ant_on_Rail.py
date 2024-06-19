# 2) Ant on Rail
# There is a ant on your balcony.lt wants to leave the rail so sometimes it moves right 
# and sometimes it moves left until it gets exhausted.Givenlan integer array A of size N which consists of integer 1 
# and -1 only representing ant's moves. Where 1 means ant moved unit distance towards the right side and -1 means it moved 
# unit distance towards the left Your task is to find and 
# return the integer value representing how many times the ant reaches back to original starting position.
# Note:
# • Assume 1-based indexing
# • Assume that the railing extends infinitely on the either sides
# Input Format:
# input1: An integer value N representing the number of moves made by the ant.
# input2: An integer array A consisting of the ant's moves towards either side

# CODE

n=int(input())
l=list(map(int,input().split()))
result=0
position=0
for i in l:
    position+=i
    if position==0:
        result+=1
print(result)