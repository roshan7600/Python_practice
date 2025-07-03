def spy(num,mul=1,total=0):
    while num!=0:
        rem=num%10
        total+=rem
        mul*=rem
        num//=10
    return 'spy number' if total==mul else 'not'    
num=int(input('enter a number: '))    
print(spy(num))