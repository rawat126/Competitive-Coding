import time
def fun(sum_,coins_1=0,coins_2=0,coins_5=0):
    if(sum_ == 0):
        return (0,0,0),0

    elif(sum_<=10):
        if(sum_==1):
            sum_ = sum_-1
            return (1,0,0),0

        elif(sum_==2):
            sum_ = sum_-2
            return (2,0,0),0

        elif(sum_==3):
            sum_ = sum_-3
            return (1,1,0),0

        elif(sum_==4):
            sum_ = sum_-4
            return (2,1,0),0

        elif(sum_==5):
            sum_ = sum_-5
            return (1,2,0),0

        elif(sum_==6):
            sum_ = sum_-6
            return (2,2,0),0

        elif(sum_==7):
            sum_ = sum_-7
            return (1,3,0),0

        elif(sum_==8):
            sum_ = sum_-8
            return (1,1,1),0

        elif(sum_==9):
            sum_ = sum_-9
            return (2,1,1),0

        elif(sum_==10):
            sum_ = sum_-10
            return (1,2,1),0

    elif(sum_>10):
        
        sum_ = sum_-10  # 3
        coins_1,coins_2,coins_5 = coins_1+1,coins_2+2,coins_5+1
        (coins_1m,coins_2m,coins_5m),sum_ = fun(sum_)
        coins = coins_1m+coins_1, coins_2m+coins_2, coins_5m+coins_5
        return coins,sum_


start = time.time()
coins_1=0;coins_2=0;coins_5=0
sum_ = int(input())

coins,sum_ = fun(sum_)
print(sum(coins),coins[2],coins[1],coins[0])


