#double hashing[merging 2 differnt hashings together]
x=[20,34,45,70,56,81,104,37,46,39]
hashList=[False for _ in range(11)]

for k in x:
    i=0
    while True:
        a=k%11
        b=8-(k%8)
        c=(a+i*b)%11
        if hashList[c]==False:
            hashList[c]=k
            break
        else:
            i+=1
print(hashList)