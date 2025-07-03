def factorial(num,fact=1):
    if num>=0:
        for val in range(1,num+1):
            fact*=val
        return fact
    return 'not possible'    
num=int(input('enter a number : '))    
print(factorial(num))
   
    