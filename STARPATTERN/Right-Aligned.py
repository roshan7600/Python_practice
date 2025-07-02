# enter a row: 4
#       * 
#     * *
#   * * *
# * * * *


num=int(input("enter a row: "))
space=num-1
for row in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(row):
        print('*',end=" ")    
    print()    
    space-=1