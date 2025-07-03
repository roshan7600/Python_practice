def sq(num,total=0):
    while num!=0:
        rem=num%10
        total+=rem**2
        num//=10
    return total
def check(num):
    while num>9:
        num=sq(num)
    return 'happy number' if num==1 or num==7 else 'not'  
num=int(input('enter a number: ')) 
print(check(num))


