arr=list(map(int,input().split()))
min = None
for num in arr:
    if num > 0:
        if min is None or num < min:
            min = num
print("Smallest positive number:", min)
