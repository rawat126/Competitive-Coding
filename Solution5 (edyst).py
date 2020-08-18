from functools import reduce

sum_ = lambda li : reduce(lambda x,y:x+y,li)

def fun(charges,limit,final_cost):
    l = len(charges)
    pop = charges.pop
    for i in range(limit):
        pop([l-i])
        

    return final_cost+sum_(charges)
    
cities = int(input())
charges = input()
limit = int(input())

if(charges.count('-1') >limit):
    print(-1)

else:
    charges = list(map(int,charges.split()))
    last = charges.pop()
    if last==-1:
        print(-1)
    else:
        final_cost = charges.pop(0)+last
        charges = sorted(charges)
        i=0
        while charges[i]==-1:
            charges.pop(0)
            i = i+1
            limit = limit-1

        print(fun(charges,limit,final_cost))




