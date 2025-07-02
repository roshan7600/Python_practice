# enter a number: 4
# *       
# * *
# *   *
# * * * *

num=int(input('enter a number: '))
for row in range(num):
    for st in range(num):
        if st==0 or row==num-1 or row==st:
            print('*',end=' ')
        else:
            print(' ',end=' ')    
    print()        