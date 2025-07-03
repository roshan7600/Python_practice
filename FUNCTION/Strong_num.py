def factorial(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
def strong(num,total=0):
    while num!=0:
        rem=num%10
        total+=factorial(rem)
        num//=10
    return total
num=int(input('enter a number: '))        
print('strong' if strong(num)==num else 'not ')