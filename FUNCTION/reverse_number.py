def reverse(num,pos,rev=0):
    while num!=0:
        rem=num%10
        rev+=rem*pos
        pos//=10
        num//=10
    return rev
num=int(input('enter a number: '))    
print(reverse(num,10**(len(str(num))-1)))