import time
num = eval(input())

#traditional approch
start1 = time.time()
for i in range(1,num+1):
    if(num%i == 0):
        print(i,end = '  ')
    else:
        pass
end1 = time.time()
print('\nET for tradational methord: ',end1-start1)

print("\n\n")



# optimised aproch
start2 = time.time()
factors = '1 '
s1 =  ""


for i in range(2,int(num**0.5)+1):
    if(num%i==0):
        factors = factors+str(i)+ ' '
        
        s1 = s1+str(num//i)+" "


print(factors,end = '')
print(*s1.split()[::-1],end = " ")
print(str(num))

end2 = time.time()

print('\nET for optimized approch: ',end2-start2)

