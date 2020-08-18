T = int(input())

def final(p,c,f,d,P,C,F):
    i = len(d)-2
    while(i>=0):
        p = p+d[i][0]
        c = c+d[i][1]
        f = f+d[i][2]

        if(p>P or c>C or f>F):
            p = p-d[i][0]
            c = c-d[i][1]
            f = f-d[i][2]
            i = i-1
            if(i==-1):
                return p,c,f

        elif(p==P or c==C or f==F):
            i=0
            #
        elif(p<P and c<C and f<F):
            pass

        return p,c,f

def fun(P,C,F,d):
    p=0;c=0;f=0
    i=0
    le = len(d)
    
    while True:
        p = p+d[i][0]  
        c = c+d[i][1]  
        f = f+d[i][2]  
        i = i+1

        if(i==le and (p<P) and (c<C) and (f<F)):
            i=le-1

        elif(p>P or c>C or f>F):
            p = p-d[i-1][0]
            c = c-d[i-1][1]
            f = f-d[i-1][2]

            p,c,f = final(p,c,f,d,P,C,F)
            break

        elif(p==P or c==C or f==F):
            break

    left_protien = str(P-p)
    left_carbs = str(C-c)
    left_fats = str(F-f)

    return left_protien+' '+left_carbs+' '+left_fats


def sort(d):
    dics = sorted(d.values(),key = sum)
    return dics


def quantity(limits):
    limits = limits.split()
    i=0
    while i<3:
        if limits[i][-1]=='P':
            P = limits[i][0:-1]
        elif limits[i][-1]=="C":
            C = limits[i][0:-1]
        elif limits[i][-1]=="F":
            F = limits[i][0:-1]

        i = i+1

    return int(P),int(C),int(F)

s = ""
for i in range(T):
    limits = input()
    P,C,F = quantity(limits)
    items = input().split("|")
    d = {}
    for j in range(len(items)):
        d[j] = quantity(items[j])

    d = sort(d)
    
    vals = fun(P,C,F,d)
    s = s+vals+"\n"
    
print(s)
