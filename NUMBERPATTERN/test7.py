# enter a number: 4

# 1 
# 1 2
# 1 2 3
# 1 2 3 4




num=int(input('enter a number: '))
for line in range(2,num+2):
    for st in range(1,line):
        print(st,end=' ')
    print() 
    