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
# Sample Output 6x=int(input())
y=int(input())
while y>0:
    if x<y:
        x,y=y,x
    # else also u can use
    elif x>=y: 
        t=x-y
        x=y
        y=t
print(x)  