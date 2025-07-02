# enter a number: 4

#       1 
#     2 2
#   3 3 3
# 4 4 4 4




num=int(input('enter a number: '))
space=num-1
for line in range(1,num+1):
     for sp in range(space):
        print(' ',end=' ')
     for st in range(line):
        print(line,end=' ')
     print()
       
     space-=1 