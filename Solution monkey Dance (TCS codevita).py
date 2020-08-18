t,n = int(input()),int(input())
for i in range(t):
    com = input().split()
    com1 = com.copy()
    count = 1
    def fun(o,n,com):
        l = [0]*n
        for i,j in zip(o,com):
            l[int(i)-1] = j
        return(l)

    com = fun(com1,n,com)
    while com != com1:
        com = fun(com1,n,com)
        count += 1
        
    print(count)
