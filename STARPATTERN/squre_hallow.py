# enter a number: 4
# * * * * 
# *     *
# *     *
# * * * *


num=int(input("enter a number: "))
for row in range(num):
    for st in range(num):
        if row==0 or st==0 or row ==num-1 or st==num-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")    
    print()        