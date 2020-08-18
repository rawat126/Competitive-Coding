def fun(matrix,row,col):
    row1,col1 = row-1,0
    row2,col2 = row-1,col-1
    first = matrix[row1][col1]
    last = matrix[row2][col2]
    all_first = []
    all_last = []
    append_first = all_first.append
    append_last = all_last.append
    
    alpha = {
    1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',
    9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',
    16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',
    23:'w',24:'x',25:'y',26:'z'
         }

    while first>26:
        first = first-26
    while last>26:
        last = last-26
    append_first(alpha[first])
    append_last(alpha[last])
    while first!=last:
        first,last = matrix[row1-1-1][col1+1], matrix[row2-1-1][col2-1]
        row1,col1 = row1-1-1,col1+1
        row2,col2 = row2-1-1,col2-1

        while first>26:
            first = first-26
        while last>26:
            last = last-26
        #print(first,last)
        
        append_first(alpha[first])
        append_last(alpha[last])

    all_last = all_last[0:len(all_last)-1]
    all_last.reverse()
    gens = all_first+all_last
    #print(gens)
    return gens#tuple(map(lambda x:alpha[x],gens))

    
T = int(input())
l = []
append = l.append
for i in range(T):    
    inp = input().split()
    row = int(inp.pop(0))
    col = int(inp.pop(0))
    matrix = []
    count = 0
    for i in range(row):
        l1 = []
        for j in range(col):
            l1.append(int(inp[count]))
            count = count+1            
        matrix.append(l1)

    append("".join(fun(matrix,row,col)))


print("\n".join(l))
            
#matrix = [[16,13,4],
#          [16,13,19],
#          [23,8,11]]

    
#fun(matrix,3,3)    
