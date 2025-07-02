# enter a number: 5

#         1 
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5





num=int(input('enter a number: '))
space=num-1
for line in range(2,num+2):
     for sp in range(space):
        print(' ',end=' ')
     for st in range(1,line):
        print(st,end=' ')
     print()
       
     space-=1 