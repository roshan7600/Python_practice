# enter a row: 4
# * * * * 
# * * *
# * *
# *


num=int(input("enter a row: "))

for row in range(1,num+1):
    
    for st in range(num):
        print('*',end=" ")    
    print()   
    num-=1 
    