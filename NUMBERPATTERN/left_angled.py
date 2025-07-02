# enter a number: 4

# 1 
# 1 1
# 1 1 1
# 1 1 1 1



num=int(input('enter a number: '))
for line in range(1,num+1):
    for st in range(line):
        print(1,end=' ')
    print()    