cases = int(input())
areas = {'rectangle':lambda l,b:l*b,'triangle':lambda l,b:l*b,
		'square':lambda l,b:(l*b)//2}
keys = areas.keys()
s = ''
for i in range(cases):
    shape = input()
    length,breadth = int(input()),int(input())
    if shape in keys:
        s = s+str(areas[shape](length,breadth))+'\n'
    else:
        s = s+str(0)+'\n'
print(s)
   
