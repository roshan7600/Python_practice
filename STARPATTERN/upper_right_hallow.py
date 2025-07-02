# enter a number: 5
# * * * * * 
#   *     *
#     *   *
#       * *
#         *

num=int(input('enter a number: '))
space=0
for row in range(num):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(num):
        if row==0 or st==0 or st==num-1-row:
            print('*',end=' ')
        else:
            print(' ',end=' ')    
    print()   
    space+=1     