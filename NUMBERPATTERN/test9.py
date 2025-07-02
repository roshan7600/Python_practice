# enter a number: 5

# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1




num=int(input('enter a number: '))
for line in range(1,num+1):
    for st in range(line,0,-1):
        print(st,end=' ')
    print() 