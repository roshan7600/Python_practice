# enter a row: 4
# * * * * 
#   * * *
#     * *
#       *


num=int(input("enter a row: "))
space=0
for row in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(num):
        print('*',end=" ")    
    print()    
    space+=1
    num-=1