# enter a number: 4
#       * 
#     * * *
#   * * * * *
# * * * * * * *


num=int(input("enter a number: "))
star=1
space=num-1
for row in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        print('*',end=" ")    
    print()    
    star+=2
    space-=1