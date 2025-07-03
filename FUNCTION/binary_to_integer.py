def binary(num,pos=0,total=0):
    while num !=0:
        rem=num%10
        total+=rem*(2**pos)
        pos+=1
        num//=10
    return total
num=int(input('enter a number: '))    
print(binary(num))