# enter a number: 4

# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 




num=int(input('enter a number: '))
for line in range(num,0,-1):
    for st in range(line,0,-1):
        print(st,end=' ')
    print() 