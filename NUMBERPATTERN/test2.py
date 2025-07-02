# enter a number: 5

# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2
# 1



num=int(input('enter a number: '))
for line in range(1,num+1):
    for st in range(num):
        print(num,end=' ')
    print()
    num-=1   