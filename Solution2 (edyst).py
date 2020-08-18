import time
def fun(str1):
    password = ""
    l = len(str1)
    while '-1' in str1:
        ind = str1.index('-1')
        val1,val2 = int(str1[ind-1]),int(str1[ind+1])
        
        if (val1%2==0 and val2%2==0) or (val1%2!=0 and val2%2!=0):
            #str1 = str1[0:ind]+str(abs(val1-val2))+str1[ind+1:]
            str1[ind] = str(abs(val1-val2))
        else:
            str1[ind] = str((val1+val2)//2)
    
    for i in range(1,l):
        if str1[i]=='1'or i==l-1:
            password = password+str1[i]
        else:
            password = password+str(int(str1[i])-1)
    
    return password
        
    

T = int(input())
start = time.time()
s = ""
for i in range(T):
    str1 = input().split()
    s = s+fun(str1)+"\n"
print(s)

print(time.time()-start +0.3)



