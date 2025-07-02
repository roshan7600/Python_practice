num=int(input("Enter the number of rows: "))
star=1
for row in range(1,num+1):
    for col in range(star):
        print('*',end=' ')
    print()    
    star+=1