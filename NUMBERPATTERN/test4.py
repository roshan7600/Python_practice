# enter a number: 4

# 4 4 4 4 
#   3 3 3
#     2 2
#       1




num=int(input('enter a number: '))
space=0
for line in range(1,num+1):
     for sp in range(space):
        print(' ',end=' ')
     for st in range(num):
        print(num,end=' ')
     print()
     num-=1 
     space+=1 