
# enter a number: 5

#         * 
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

num=int(input('enter a number: '))
space=num-1
star=1
for row in range(num):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        if st==0 or row==num-1 or row*2==st:
            print('*',end=' ')    
        else:
            print(' ',end=' ')    
    print()        
    space-=1
    star+=2