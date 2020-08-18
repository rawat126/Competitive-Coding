def isPrime(num):
    if(num==1):
        return False
    if(num==2):
        return True
    
    if(num>2):    
        for i in range(2,num):
            if(num%i == 0):
                return False
        else:
            return True

def fun(time,parts,hour_per_part):
    count = 0
    for i in range(hour_per_part):
        for j in range(parts):
            #print(time[j][i])
            if isPrime(time[j][i]):
                pass
            else:
                break
            
            #print('\n')
        else:
            count = count+1

    return count        

hours,parts = input().split()
hours,parts = int(hours),int(parts)

hour_per_part = hours//parts
time = []
val = 0

for i in range(1,parts+1):
    l = []
    for j in range(1,hour_per_part+1):
        val = val+1
        l.append(val)
    time.append(l)

#print(time)
print(fun(time,parts,hour_per_part))
        
