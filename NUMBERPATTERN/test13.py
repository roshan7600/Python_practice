# enter a number: 5

#         5 
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5




num=int(input('enter a number: '))
space=num-1
for line in range(num,0,-1):
     for sp in range(space):
        print(' ',end=' ')
     for st in range(line,num+1):
        print(st,end=' ')
     print()
       
     space-=1 