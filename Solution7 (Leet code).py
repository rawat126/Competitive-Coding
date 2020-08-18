'''def search(num,start,end,list_):
    le = len(list_)
    if(le==1):
        if(num == list_[0]):
            return True
    else:
        ind = (start+end)//2
        if(list_[ind]==num):
            return True
        
        elif(end-start == 0 and list_[ind]!=num or ind>=le):
            return False 

        elif(list_[ind]>num):
            last = ind
            start = 0
            return search(num,start=start,end=last,list_=list_)
            
        elif(list_[ind]<num):
            last = le
            start = ind+1
            return search(num,start=start,end=last,list_=list_)
'''

def fun(t1,t2,m):
    nums = []
    append = nums.append
    i = 2; j=1
    
    while int(t2**0.5)+1:
        num1 = i
        num2 = i+j
        i = i+1
        j = j+1
        if(num1*((2*num1)-1)>=t1):
            val1 = num1*((2*num1)-1)
            val2 = (num2*(num2+1))/2
            if val1 == val2 and val1<=t2:
                nums.append(val1)
            if(val1>=t2):
                break

    try:
        print(nums[int(m)-1])
    except IndexError:
        print("Not Found")
    except ValueError:
        print("Invalid")
 

# Total Test Cases....    
T = int(input())
i = 0
while i<T:        
    t1 = int(input())
    t2 = int(input())
    m = input()
    
    # condition for positive input
    if t1>0 and t2>0:
        fun(t1,t2,m)
    else:
        print("Invalid")
    i = i+1


