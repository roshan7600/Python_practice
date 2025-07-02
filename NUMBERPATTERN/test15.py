# enter a number: 4

#       1 
#     1 2 3
#   1 2 3 4 5
# 1 2 3 4 5 6 7





num=int(input('enter a number: '))
space=num-1
for line in range(1,num+1):
     for sp in range(space):
        print(' ',end=' ')
     for st in range(1,2*line):
        print(st,end=' ')
     print()
       
     space-=1 