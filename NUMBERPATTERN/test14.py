# enter a number: 4

# 1 
# 2 3
# 4 5 6
# 7 8 9 10




num=int(input('enter a number: '))
count=1
for line in range(1,num+1):
    for st in range(line):
        print(count,end=' ')
        count+=1
    print() 