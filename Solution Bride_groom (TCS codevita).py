import time


length = int(input())
count = 0
brides = input()
grooms = input()
s = time.time()
while length >0 :
    if(brides[0] != grooms[0]):       
        grooms = grooms[1:]+grooms[0]
    else:
        length -= 1
        brides,grooms = brides[1:],grooms[1:]
else:
    print(length)

e = time.time()

print(e-s)
