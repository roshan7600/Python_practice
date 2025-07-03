def binary(num):
    if num==0:
        return '0'
    elif num==1:
        return '1'    
    return binary(num//2) + str(num%2)  
num=15
print(binary(num))  