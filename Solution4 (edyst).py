def fun(sets):
    l = len(sets)
    s = sets[0]
    for i in range(1,l):
        
        if(i==l-1):
            if(len(sets[i])>len(sets[i-1])):
                s = s+sets[i][0]+sets[i][-1]
        
        elif len(sets[i])<len(sets[i+1]):
            s = s+sets[i][0]+sets[i][-1]

        elif len(sets[i])>=len(sets[i+1]):
            s = s+sets[i][0]+sets[i][-1]
            break     

    return s
                

T = int(input())
s1 = ""
for i in range(T):
    str1 = input()
    sets = []
    append = sets.append
    end = str1.endswith

    i=0;j=0

    while True:
        k = i+j+1
        sub = str1[i:k]
        append(sub)
        i = k
        j = j+1

        if end(sub):
            break

    s1 = s1+fun(sets)+'\n'

print(s1)

