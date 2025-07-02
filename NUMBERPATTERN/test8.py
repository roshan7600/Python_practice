# enter a number: 5

# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1



num=int(input('enter a number: '))
for line in range(num+1,1,-1):
    for st in range(1,line):
        print(st,end=' ')
    print() 