# enter a number: 4

# 4 
# 3 3
# 2 2 2
# 1 1 1 1



num=int(input('enter a number: '))
for line in range(1,num+1):
    for st in range(line):
        print(num,end=' ')
    print() 
    num-=1  