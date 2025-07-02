# enter a number: 5

# 5 
# 4 5 
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5


num=int(input('enter a number: '))
for line in range(num,0,-1):
    for st in range(line,num+1):
        print(st,end=' ')
    print()  