# enter an odd number: 7

#       *       
#     *   *
#   *       *
# *           *
#   *       *
#     *   *
#       *


num=int(input('enter an odd number: '))
if num%2==0:
    print('please enter a odd number')
else:
    center=num//2
    for row in range(num):
        for col in range(num):
            if (row+col==center) or (col-row==center) or (row-col==center) or (row + col==num-1+center):
                print('*',end=' ')    
            else:
                print(' ',end=' ')    
        print()        