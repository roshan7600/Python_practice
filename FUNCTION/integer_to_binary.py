def integer(num,pos=1,total=0):
    while num !=0:
        rem=num%2
        total+=rem*pos
        pos*=10
        num//=2
    return total
num=int(input('enter a number: '))    
print(integer(num))