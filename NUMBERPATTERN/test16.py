# enter a number: 4

#       1 
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1



num=int(input('enter a number: '))
space=num-1
for line in range(1,num+1):
     for sp in range(space):
        print(' ',end=' ')
     for st in range(1,line+1):
        print(st,end=' ')
     for st in range(line-1,0,-1):
         print(st,end=' ')   
     print()
       
     space-=1 