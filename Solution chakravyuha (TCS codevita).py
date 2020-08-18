
def fun(start,end,val,arr,coors):
    global out
    end = end-1

    if(start==end):
        arr[start][end]=str(val)
        if(val%11==0):
            coors.append((start,end))
        return arr,coors
        
    for i in range(start,end+1):
        arr[start][i]=str(val)
        if(val%11==0):
            coors.append((start,i))
        val = val+1
            
    for i in range(start+1, end+1):
        arr[i][end] = str(val)
        if(val%11==0):
            coors.append((i,end))
        val = val+1
        

    for i in range(end-1,start-1,-1):
        arr[end][i] = str(val)
        if(val%11==0):
            coors.append((end,i))
        val = val+1

    for i in range(end-1, start,-1):
        arr[i][start] = str(val)
        if(val%11==0):
            coors.append(i,start)
        val = val+1

    if (end-start==1):
        return arr,coors
        
    out,coors = fun(start =start+1, end =end, val=val, arr= arr, coors = coors)
    return out,coors
        
    


global out
coors = [(0,0)]
out = 0

N = int(input())
arr = [['_' for col in range(N)] for i in range(N)]

arr,coors = fun(start=0,end = N,val = 1,arr=arr,coors = coors)
print("".join([" ".join(i)+'\n' for i in arr]))
print('Total Power points : ',len(coors))
for i in coors:
    print(i)
    



'''
        [
            [1, 2, 3, 4, 5],
            [16,17,18,19,6],
            [15,24,25,20,7],
            [14,23,22,21,8],
            [13,12,11,10,9]
        ]

'''
