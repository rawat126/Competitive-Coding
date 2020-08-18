from functools import reduce

op = lambda x : x//2
sum_ = lambda li: reduce(lambda x,y:x+y,li)

def fun(s,k):
    k1 = 0
    i = 0
    
    while True:
        if(k1==k):
            break

        if(s[i]>s[i+1]):
            s[i] = op(s[i])
            k1 = k1+1

        elif(s[i]<=s[i+1] ):
            i = i+1

        if(i == len(s)-1):
            while(s[i] == max(s)):
                k1 = k1+1
                s[i]=op(s[i])

                if(k1==k):
                    break

            i=0

        if s == [0]*len(s):
            return 0

    return sum_(s)

items,k = input().split()
items,k = int(items),int(k)

s = list(map(int,input().split()))

print(fun(s,k))
