# print("Hello world")
# num= int(input("enter a number "))
# # if age>=18:
# #     print("You can Vote" )
# # else:
# #      print("You cannot Vote" )


# star

# for i in range(2,num):
#     if i>1:
#         if num % i ==0:
#             print("print is not prime")
#             break
#         else:
#             print("print is prime")
#     else:
#         print("this number cannot be taken")
# for i in range(10,1,-1):
#     print(i) 



# num= int(input("enter number"))
# for i in range (5):
#     for j in range (5-i):
#          print(" ")
#          print("*",end=" ")
    # for j in range(i):
    #      print("*",end=" ")
    # print("\n")   

# s="preethi"
# _=123
# print("Ece".isupper())
# s="hello ece"
# print(s[-1:-3:-1])
# l=[1,2,3]
# l1=l
# l2=l.copy()
# l1.append(4)
# print(l)
# print(l1)
# print(l2)
# l=[1,2,3,34,23]
# l.clear()
# print(l)
# d={}
# d[0]="hello"
# d[1]="reddy"
# d[1]="pree"
# print(d)


# l=[1,2,3,1,2]
# print(10<<2)


# Day-2

#  read 3 int from user find the greatest nymber 

# num1=int(input("Enter th first number"))
# num2=int(input("Enter th second number"))
# num3=int(input("Enter th thrid number"))

# if(num1>num2):
#     if(num1>num3):
#         print("The greatest number is ",num1)
# elif (num2>num1):
#     if(num2>num3):
#         print("The greatest number is ",num2)
# else:
#     print("The greatest number is ",num3)

# OTHER WAY TO FIND 
# print(max(num1,num2,num3))

# WRITE A PROGRAM TO READ AN INTERGER FROM THE USER IE N PRINT NUMBER FROM 1 TO N 
# n= int(input("enter the number: "))
# for i in range(0,n,2):
#     print(i)

#PATTERNS 
# 1 
# 4 1
# 9 4 1
# 16 9 4 1
# 25 16 9 4 1
# 36 25 16 9 4 1
# for i in range(n+1):
#     for j in range(i+1,0,-1):
#             print(j*j,end=" ")
#     print("\n")
#         *           
#       *   *         
#     *   *   *       
#   *   *   *   *     
# *   *   *   *   *   
# *   *   *   *   *   
#   *   *   *   *     
#     *   *   *       
#       *   *         
#         *    
# for i in range(n):
#     for j in range(n-(i+1)):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*  ",end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print("*  ",end=" ")
#     print()
# for i in range(n-1):
#     for j in range(n-(i+1)):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(2*(n-i)-1):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-(i+1)):
#         print(" ",end=" ")
#     for k in range(2*i+1,0,-1):
#         print("*",end=" ")
#     print() 

# WA FUNCTION THT WILL TAKE 2 PARAMETERS AND RETURN THE SUM  OF THOSE TO PARAMETER CALL THE FUNCTION
# def sum(a,b):
#     return a+b
# add=sum(2,3)
# print(add)
# WAP THT WILL PRINT 1 TO N BY USING RECURSION 
# WAP T0FIND FACTORIAL OF A GIVE NUMBER USING RECURSION SING RECURSIO

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# result=factorial(7)
# print(result)    


# WAP TO PRINT FABANOCII SERIES IN RECURSION 
# def fab(n):
#     if n<=0:
#         return "input positive numbers"
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# print(fab(10))    

# DAY 3
# class car():
#     def __init__(self,brand,cost):
#         self.brand=brand
#         self.cost=cost
#     def detail(self):
#         print(self.brand,self.cost)

# o=car("toyota",1000000)
# o.detail()


# INHERITANCE
# SINGLE IN HERITANCE
# class parent():
#     def __init__(self):
#         print("im parent init")

#     def f1(self):
#         print("im f1")
#     def f2(self):
#         print("f2")
# class child(parent):
#     def __init__(self):
#         print("im child init")
#     def f3(self):
#         print("im f3")
#     def f4(self):
#         print("im f4")

# MUTIPLE LEVEL
# class parent():
#     def __init__(self):
#         print("im parent init")

#     def f1(self):
#         print("im f1")
#     def f2(self):
#         print("f2")
# class child(parent):
#     def __init__(self):
#         print("im child init")
#     def f3(self):
#         print("im f3")
#     def f4(self):
#         print("im f4")
# class grandparent(child):
#     def __init__(self):
#         print("im child init")
#     def f3(self):
#         print("im f3")
#     def f4(self):
#         print("im f4")

# MUTIPLE
# class parent():
#     def __init__(self):
#         print("im parent init")
#     def f1(self):
#         print("im f1")
#     def f2(self):
#         print("f2")
# class child():
#     def __init__(self):
#         print("im child init")
#     def f3(self):
#         print("im f3")
#     def f4(self):
#         print("im f4")
# class grandparent(parent,child):
#     def __init__(self):
#         print("im child init")
#     def f3(self):
#         print("im f3")
#     def f4(self):
#         print("im f4")

# POLYMEORPHISM
# class poly:
# def add(a,b):
#     return a+b
# def add(a,b,c):
#     return a+b+c
# def add(a):
#     return a
# o=poly()
# print(add(1,2,3))

# def count_spaces(S: str):
#     return S.count(' ')

# S = "hello D I M U "
# space_count = count_spaces(S)
# print('no is spaces in heart are',space_count)

# 50-CODES

# 1st code
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

# n=int(input())
# l=list(map(int,input().split()))
# result=0
# position=0
# for i in l:
#     position+=i
#     if position==0:
#         result+=1
# print(result)
# 2nd code
# 3 Chocolate jar
# 3) Chocolate jar

# You are given an integer array of size N, representing jars of chocolates. Three students A, B, and C respectively, 
# will pick chocolates one by one from each chocolate jar, till the jar is empty, 
# and then repeat the same with the rest of the jars. Your task is to fine 
# and return an integer value representing the total number of chocolates that student A will have, 
# after all the chocolates have been picked from all the jars.
# Note:Once a jar is done A will start taking the chocolates from the new jar.
# Input Format:
# Input1:An integer array representing the quantity of chocolates in each jar.
# Input2:An integer value N representing the number of jars.

# CODE
# n=int(input())
# l=list(map(int,input().split()))
# a=0
# for i in l:
#     if i%3==0:
#         a+=i//3
#     if i%3>0:
#         a+=i//3+1
# print(a)
# 3rd code 
# Diwali Contest
# Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8 PM and will run until midnight (12 AM) 
# i.e., for 4 hours. He also needs to travel to the party venue within this time which takes him P minutes. 
# The contest comprises of N problems that are arranged in order of difficulty, with problem 1 being the simplest and
# problem N being the most difficult. Max is aware that he will require 5*i minutes to solve the ith problem. Your task is help Max find 
# and return an integer value, representing the number of problems
# Max can solve and reach the party venue within the given time frame of 4 hours.
# Note: Max will leave his home at exactly 8 PM to reach the party venue.
# Input Format:
# input1: An integer value N, representing the total number of problems.
# input2: An integer value P, Representing the time to travel in minutes from his home to the party venue.
# Example:
# Input:
# 6 180
# Output:4
# Explanation:
# The amount of time left to solve the problems is 4*60- 180-60 mins.
# 1st Problem-5 mins, Time 60-5-55 mins
# 2nd Problem-10 mins, Time left =55-10-45 mins
# 3rd Problem 15 mins, Time left45-15-30 mins
# 4th Problem 20 mins, Time left = 30-20-10 mins

# 
# n=int(input())
# p=int(input())
# time=240
# time=time-p
# x=1
# res=0
# while time>0 :
#     if x*5<time:
#         time-=x*5
#         x+=1
#         res+=1
#     else:
#         break
# print(res) 

# 4th code
# 5) Dog
# Age Max has a dog, which is an integer N years old. Now he wants the age of his dog in human years. 
# The internet says that 1 dog year equals to 7 human years. Your task is to find 
# and return an integer value representing the age of Max's dog in human years.
# Input Format: input1:An integer value N representing the age of Max's dog
# Output Format: Return an integer value representing the age of Max's dog in human years
# Example:
# Input:4
# Output:28

# n=int(input())
# human=n*7
# print(human)

# 5th code
# 7) Space Counter
# You have been given the task of making the content on a social media platform more user-friendly. 
# Your task is to find and return an integer value representing the count of the number of spaces in a given string S.
# Input:A string S
# Output: Return an integer value representing the count of the number of spaces in a given string S.
# Example:
# Input:
# Hello World Hey
# CODE

# S = " Hello World Hey"
# space_count = S.count(' ')
# print(space_count)

# 6th code
# 9) Math test
# Alice has a mathematics test for which she is underprepared.
# She has to do at least one question correctly to pass the test. 
# He decides to do a question which needs her to find the smallest prime number which is larger than a given integer N. 
# Your task is to find and return an integer value representing the smallest prime number larger than N.
# Input Format:
# input1: An integer value N
# Output Format: Return an integer value representing the smallest prime number larger than N.
# Sample Input:6
# Sample Output 7

# CODE

# n=int(input())
# while True:
#     n=n+1
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         print(n)
#         break


# DAY2
# 7th code
# 1) Advance sup array problem
# You are competing in a basketball contest. In this contest the score for each successful shot depends on both 
# the distance from the basket and the player's position. 
# The ball is shot N times, successfully. You are given an array A containing the distance of a player from basket for N shots. 
# The index of array represents the position of the player. 
# Score is calculated by multiplying the position with the distance from the basket. 
# Your task is to find and return an integer value, representing the maximum possible 
# score you can achieve by choosing a contiguous subarray of size K from the given array.
# Note: A subarray is a contiguous part of array.
# Assume 1 based indexing.
# * The array contains both negative and positive values.
# * Assume the player is standing on a cartesian plane
# Input Format -
# input1:An integer value N representing the number of shots made by the player -
# input2 : An interger K representing the size of subarray
# input3: An array of intergers

# # Input
# N = int(input())
# K = int(input())
# l = list(map(int,input().split())) 
# max=0
# for i in range(len(l)-K+1):
#     temp=l[i:i+K]
#     s,k=0,1
#     for j in temp:
#         s+=(k*j)
#         k+=1
#     if s>max: max=s 
# print(max)

# 8th code
# ELECTION
# You are the head of the election committee in your village. Each Political party is associated with a unique number and 
# the votes are represented as an integer array A. where each element contains the party number voted for by the villagers. 
# For a party to win, they must have a majority of votes. our task is to find and 
# return an integer value denoting the winning party's number. Return -1 if there is no party with a majority.
# Note: If only one vote is there he is the winner.
# Input Format:
# Input1: An integer value representing the number the number of voters
# Input2: An integer array A representing the votes of the voters, 
# output Format: Return an integer value denoting the winniese party's number Retiro-1.there is no party with a

# Input values
# n=int(input())
# l=list(map(int,input().split()))
# d={}
# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
# lis=list(d.items())
# lis.sort(reverse=True,key= lambda x:x[1])
# if len(lis)==1:
#     print(lis[0][0])
# else:
#     if lis[0][1]==lis[1][1]:
#         print(-1)
#     else:
#         print(lis[0][0])

# 9th code
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

# S = input()
# d = {}
# for i in S:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# # print(d)
# max = max(d.values())
# min = len(S) - max

# print(min)

# 10th code
# 11) Encode The Number
# You work in the message encoding department of a national security agency.
# Every message that is sent from or received in your office is encoded. 
# You have an integer N, and each digit of N is squared and the squares are concatenated together to encode the original number. 
# Your task is to find and return an integer value representing the encoded value of the number.
# input1: An integer value N representing the number to be encoded.
# Output:Return an integer value representing the encoded value of the number.
# Sample Input:


# N = input()
# string=''
# for i in N:
#     string+=str(int(i)*int(i))
# print(string)

# 11th code
# 8) Minimum Array sum

# Paul is given an array A of length N. He must perform the following Operations on the array sequentially:
# Choose any two integers from the array and calculate their average.
# If an element is less than the average, update it to 0. 
# However, if the element is greater than or equal to the average, he need not update it.
# Your task is to help Paul find and return an integer value, 
# representing the minimum possible sum of all the elements in the array by performing the above operations.
# Note: An exact average should be calculated, even if it results in a decimal.
# Input Format:
# input1: An integer value N, representing the size of the array A.
# input2: An integer array A.
# Output Format:
# Return an integer value, representing the minimum possible sum of all the elements in the array by
# Sample Input
# 5
# 12345
# Sample Output:5

# n=int(input())
# l=list(map(int,input().split()))
# l.sort()
# avg=(l[-1]+l[-2])/2
# res=0
# for i in l:
#     if i>avg:
#         res+=i
# print(res)

# DAY3
# 12th CODE
# 13) Minimum Number of Key Presses

# George has a setup which includes a special keyboard and a monitor, that initially displays 0. 
# The special keyboard has 11 numeric keys (0,1,2,3,4,5,6,7,8,9,00).
# If he presses 00, the previously displayed value will be multiplied by 100.
# Whereas, if he presses any other numeric key, the previously displayed value will be firstly multiplied by 10 
# and then the number on the key will be added to it
# You are given a numeric string S. Your task is to help George find and return an integer value, 
# representing the minimum number of key presses to reach the number.
# Input Specification:
# input: A numeric string s. representing the final number,
# Output Specification:
# Return an integer value, representing the minimum number of key presses to reach the number.
# Sample Input:100
# Sample Output:2

# s=input()
# i,res=0,0
# while i<len(s):
#     if(i+1)<len(s) and s[i]=='0' and s[i+1]=='0':
#         i+=2
#     else:
#         i+=1
#     res+=1
# print(res)

# 13th CODE
# 12) Arduino
# Tom is an Arduino Programmer. He has designed a program to run his robocar on a horizontal number line. 
# Initially, the car is parked at: 0.
# Given an array A of N integers which can be A. B. C... the robocar runs as follows as per the designed program
# First the robocar moves A units in specified direction(right in case the integer is positive and left if the integer is negative).
# Then robocar first moves A units and then B units in a specified direction.
# In the next step, the robocar moves A units. B units, and then C units in a specified direction.
# This process keeps on repeating as per the number of integers in the sequence..
# Your task is to find and retum an integer value, 
# representing the farthest coordinate reached by the robocar from the beginning to the end of the process.
# Sample Input:
# 1-234
# Sample Output:6

# n=list(map(int,input().split()))
# res=0
# s=0
# for i in range(len(n)):
#     s+=n[i]
#     if abs(s)>res:
#         res=abs(s)
# print(res)

# 14TH CODE
# 14) Special String

# Alice has a string A consisting of lowercase English letters. 
# Her friend gives her another string S and asks her to modify string A and replace its characters with the characters present in string S.
# But, to achieve the above task, Alice must follow the below steps:
# 1. Choose a character from string S that has the minimum ASCII distance from the
# ith character in string A
# Replace the ith character in string A with the chosen character in string S
# Your task is to find and return an integer value, representing minimum total ASCII distance that is required to modify string A 
# to the characters in string S. Return O, if all the characters in string S are already present in string A
# Sample Input:
# abcd
# xyz
# Sample Output:86

# A = input()
# S = input()
# total=0
# for i in A:
#     mn=100;d=0
#     for j in S:
#         d =abs(ord(i)-ord(j))
#         if d<mn:
#             mn=d
#             total+=mn
# print(total)

# 15) Finding commas
# Liam works as a data analyst for a company that stores massive amounts of numerical data.
# He has been tasked with determining how many commas are used when writing numbers in the range of 1 to N (inclusive) in a specific format
# In this format, 
# if numbers are more than four digits long, commas are used to separate the numbers into groups of three, 
# starting from the right for the representation of the number. 
# Your task is to help Liam find and return an integer value,
# representing the total number of commas used when writing each integer in the range of 1 to N
# Input Specification:
# Input: An integer value N. representing the number range.
# Output Specification:I
# Return an integer value, representing total number of commas used when writing each integer in the range of 1 to N.
# Sample Input: 5000
# Sample Output: 4001

# n= int(input())
# commas = 1
# res=0
# cur=1000
# while cur<=n:
#     next=cur*1000
#     nums=min(n-cur+1,next-cur)
#     res+=nums*commas
#     cur=next
#     commas+=1
# print(res)

# 16) Toss and score
# You are playing a game of Toss and Score in the Hillwood City Mall with your friends. The game consists of the following rules:
# Toss an unbiased coin multiple times.
# For each heads you get 2 points and for each tails you lose 1 point.
# The game ends as soon as you get 3 heads in a row, or you toss the coin throughout the length of string S.
# You have been given a string 5 consisting of letters H (for heads) and T (for tails) denoting the sequence results you get on the tass of coin N times.
#  Your task is to find and return an integer value representing the final score you get once the game ends.
# Note: The final score can be negative too.
# Input Specification:
# Input1: A string s. representing the sequence of results you get on the toss of coin N times.
# Sample Input:
# HHHTT
# Output:6
# s=input()
# SC=0
# HC=0
# for i in s:
#     if i=='h':
#         SC+=2
#         HC+=1
#         if HC==3:
#             break
#     else:
#         SC-=1
#         HC=0
# print(SC)

# 17th CODE
# 17) Best Grade

# Andrew has a string N consisting of lowercase English letters representing respective grades of N students in his class.
# His grade is at Pth index. He can swap any two adjacent grades.
# Your task is to help Andrew find and return a string value, 
# representing maximized grade by bringing lexicographically smallest character on the Pth index after doing at most K swaps I

# Sample Input:abcdefg
# 3
# 2
# Sample Output:
# a

# n=input()
# p=int(input())
# k=int(input())
# start=max(0,p-k-1)
# end=min(len(n),p+k)
# print(min(list(n[start:end])))

# 18) Vowel Repetition Problem
# Given a string s print the most frequent vowel that is present in the string as a output.
# Input Format:
# A single line containing the string s.
# The input will be read from the STDIN by the candidate
# Output Format:
# Print a single character which represents the most frequent vowel in the given string.
# Example:
# Input:
# helloworld
# Output:
# O

# 1st app
# s = input().lower()
# v='aeiou'
# mx=0
# vowel=''
# for i in v:
#     if s.count(i)>mx:
#         mx=s.count(i)
#         vowel=i
# print(vowel)

# 2nd app
# s = input().lower()
# v = {'a': 0,'e': 0,'i': 0,'o': 0,'u': 0}
# for i in s:
#     if i in v:
#         v[i] += 1
# for i in v:
#     if v[i]==max(v.values()):
#         print(i)
#         break
# 19) Number of combinations leading to a product
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
# n=int(input())
# l=list(map(int,input().split()))
# t=int(input())
# res=0
# k=l.sort()
# for k,i,j in k:
#     p=i*j*k
#     if p==t:
#         res+=1
#     elif p<t:
#         i+=1
#     else:
#         j-=1
# print(res)   

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
# DAY 4
# 20) Equilibrium
# You are given an array A of N integers. An equilibrium position is a position where the sum of all integers on its left is equal 
# to the sum of all integers on its right in the array A. Print the index of the equilibrium position.
# Note: For any given array there is only a single equilibrium position, if no equilibrium position is found then 
# print "NOT FOUND" without quotes.
# The array is 1 indexed.
# Input Format:
# The input consists of two lines:
# The first line contains an integer denoting N.
# The second line contains N space-separated integers denoting the elements of the array A.
# Input will be read from the STDIN by the candidate
# Output Format:
# Print the index of the equilibrium position. If no index is found, print "NOT FOUND
# Sample Input
# 5
# {-7, 1, 5, 2, -4, 3, 0}
# Sample Output:3

# ar=list(map(int,input().split()))
# for i in range (len(ar)):
#     if sum(ar[:1]==sum(ar[i+1:])):
#         return i+1
# return -1
# preethi=9844435789
# print(preethi)  
# I am Preethi Im here to say few things about you im happy that 

# 21) sub array with max sum
# You are given a list of integers, and your task is to find the subarray with the maximum sum.
# Write a function or method to solve this problem efficiently and return the maximum sum.
# Input:
# n: the no of elements in the array
# nums (List of integers): A list of integers (1 <= len(nums) <= 10^5)
# Sample input:
# 8
# -1 2 3 10 -4 7 2 -5
# Sample output:
# 20
# Explanation:
# The max subarry sum is 20. The subarray is [2,3,10,-4,7,2]

# nums=list(map(int,input().split()))
# temp=0
# res=0
# for i in nums:
#     temp+=i
#     if temp<i:
#         temp=i
#     if res<temp:
#         res=temp
# print(res)

# 22) Pizza Party
# Angela has decided to throw a pizza party. she has ordered N number of pizzas to be served to her N number of friends. 
# In this way, she will be serving only one pizza to each friend.
# She now wants to invite fewer people to her party in order to provide more pizzas per person. But at the same time, 
# she wants to ensure that there are at least Y friends at her party.
# Your task is to help Angela find and return an integer value, 
# representing the sum of digits of the minimum number of friends that she can invite to the party, 
# ensuring that each person gets an equal number of pizzas
# Sample Input:
# 100 17
# Sample Output:2
# Explanation:
# N=100, Y=17
# For Y=20 each friend gets 5 pizzas. So sum of digits of 20 is 2.

# n=int(input())
# y= int(input())
# res=0
# for i in range(y,n+1):
#     if n%i==0:
#         while i:
#             res+=i%10
#             i=i//10
#         break
# print(res)

# 23) Reduce till zero
# Dev loves the number zero. Dev gives Andrew two integers X and Y and asks him to perform the steps below on X and Y.
# until the value of Y has been reduced to zero The below steps should be followed sequentially
# 1. If Xcx pa style="box-sizing: inherit;">
# 2. If Y=0. then return X
# 3. Otherwise, let TeX-Y.
# 4. Set Xey and then set Y-T
# 5. Repeat from step 1.
# Your task is to help Andrew find and return an integer value, representing the value of X,
# when the value of Y has been reduced to zero.
# Note: At least one of the X or Y will be a non-zero integer
# Input Specification:
# Input: An integer value X. representing the first number.
# Input: An integer value Y representing the second number
# Sample input:
# 48
# 18
# Sample Output 6

# x=int(input())
# y=int(input())
# while y>0:
#     if x<y:
#         x,y=y,x
#     # else also u can use
#     elif x>=y: 
#         t=x-y
#         x=y
#         y=t
# print(x)   

# 24) Nearest Corner
# Bruce is a newly hired employee at a company. The Office Management Department has given him a desk number, which is stored in string S. 
# He has also been handed a string array A. containing all the N office desk numbers.
# Array A also includes the symbol"-", which stands for the gap in the sitting arrangement. 
# Comer seats are those that are on either side of the gap. Your task is to help Bruce find and retum an integer value. 
# representing how far he is from the nearest corner seat. Return 0, if he is in the corner seat.
# Note:I
# There will always be at least one gap inthe string array A
# Desk number is always in a format of a number first followed by an English letter in uppercase
# Assume 0-based indexing
# Input Specification:
# A string S. representing Bruce's newly assigned desk number.
# Second line containing space seperated strings showing the seat positions and gaps
# Sample input:
# 3C
# 1A 2B-3C 4D
# Sample Output:
# 0
# I

