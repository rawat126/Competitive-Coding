import random
def fun(arr,row,col):
    global count
    #row_prev,col_prev = row,col
    le = len(arr)

    print(row,col)
    if row==le-1 and col==le-1:
        return arr

    if row+1 >= le and col+1 < le:
            
        if(arr[row][col+1]=='0'):
            pos = arr[row][col]
            arr = fun(arr,row,col+1)
            count = count+1
            
        else:
            arr[row][col] == "x"
            count = count-1
            #pos = arr[row_prev][col_prev]
            #return None

    elif col+1 >= le and row+1 < le:
        
        if(arr[row+1][col]=='0'):
            pos = arr[row+1][col]
            arr = fun(arr,row+1,col)
            count = count+1
            
        else:
            arr[row][col] == "x"
            count = count-1
            #pos = arr[row_prev][col_prev]
            #return None
    
    else:
        if(arr[row+1][col+1]=='0'):
            pos = arr[row+1][col+1]
            arr = fun(arr,row+1,col+1)
            count = count+1
            
        elif(arr[row+1][col]=='0'):
            pos = arr[row+1][col]
            arr = fun(arr,row+1,col)
            count = count+1
            
        elif(arr[row][col+1]=='0'):
            pos = arr[row][col]
            arr = fun(arr,row,col+1)
            count = count+1
            
        else:
            arr[row][col] == "x"
            count = count-1
            #pos = arr[row_prev][col_prev]
            #return None

    return arr
    
global count
count = 0
T = int(input())
for i in range(T):
    row,col = tuple(map(int,input().split()))

    arr = [['0' for c in range(col)] for r in range(row)]

    for i in range(row):
        for j in range(col):
            val = random.randint(1,10)
            if val<=5:
                arr[i][j] = '1'

    arr[0][0] = arr[row-1][col-1] = '0'

    print(arr)
    '''arr = [
            ['0','1','1'],
            ['1','0','1'],
            ['0','0','0']
        ]'''
    
    print('\nPath : ')
    fun(arr,0,0)
    input()
    print('Shortest Distace : ',count)
    
    
