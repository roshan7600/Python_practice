def neven(num,total=0):
    dup=num
    while num!=0:
        rem=num%10
        total+=rem
        num//=10
    return 'neven number' if dup % total==0 else 'not a neven number'     
num=int(input('enter a number: '))    
print(neven(num))