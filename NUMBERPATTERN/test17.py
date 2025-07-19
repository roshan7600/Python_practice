# Enter a number: 5



#       1 
#       0 1
#       1 0 1
#       0 1 0 1
#       1 0 1 0 1


num=int(input("Enter a number: "))
for line in range(1,num+1):
    for st in range(line):
        print((line+st)%2, end=' ')
    print()    