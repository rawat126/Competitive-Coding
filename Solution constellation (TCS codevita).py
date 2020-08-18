def fun(val):
    if (val == ['*', '.', '*', '*', '.', '*', '*', '*', '*']):
        return "U"
    elif(val == ['*', '*', '*', '*', '.', '*', '*', '*', '*']):
        return "O"
    elif(val == ['*', '*', '*', '.', '*', '.', '*', '*', '*']):
        return "I"
    elif(val == ['*', '*', '*', '*', '*', '*', '*', '*', '*']):
        return "E"
    elif(val == ['.', '*', '.', '*', '*', '*', '*', '.', '*']):
        return "A"

rows = 3
cols = int(input())

l1 = list(input())
l2 = list(input())
l3 = list(input())
i = 0
j = 3

s = ""
while (i<cols):
    while((l1[i] ==l2[i]==l3[i]=='#') or (l1[i] ==l2[i]==l3[i]=='.')):      
        if(l1[i]=="#"):
            s = s+"#"
        i = i+1
        j = j+1
        
    val = l1[i:j]+l2[i:j]+l3[i:j]
    alpha = fun(val)
    s = s+alpha
    k = j
    
    if(j>=cols-1):
        break
     
    while((l1[k] ==l2[k]==l3[k]=='#') or (l1[k] ==l2[k]==l3[k]=='.')):      
        if(l1[k]=="#"):
            s = s+"#"
        i = i+1
        k = k+1

    else:
        i = i+3
        j = i+3

print(s)
