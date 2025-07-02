# enter a number: 5

# *       * 
#   *   *   
#     *
#   *   *
# *       *


num=int(input('enter a number: '))
for row in range(num):
    for st in range(num):
        if row==st or st==num-1-row:
            print('*',end=' ')
        else:
            print(' ',end=' ')    
    print()        
