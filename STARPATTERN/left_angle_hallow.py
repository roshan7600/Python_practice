# enter a number: 4
#       *       
#     * *
#   *   *
# * * * *
num=int(input('enter a number: '))
space=num-1
for row in range(num):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(num):
        if st==0 or row==num-1 or row==st:
            print('*',end=' ')    
        else:
            print(' ',end=' ')
    print()
    space-=1        
