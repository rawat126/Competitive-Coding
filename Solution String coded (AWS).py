s = 'AAAAAAABBBBBBDDDDCCCCCDDDABCD'
count = 1
s1 = ''
 
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count = count+1
    else:
        s1 = s1+s[i]+str(count)
        count = 1

s1 = s1+s[i+1]+str(count)
print(s1)
        
