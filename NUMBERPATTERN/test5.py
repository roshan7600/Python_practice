# enter a number: 4

# 1 1 1 1 
# 2 2 2
# 3 3
# 4



num=int(input('enter a number: '))
for line in range(1,num+1):
    for st in range(line,num+1):
        print(line,end=' ')
    print()   