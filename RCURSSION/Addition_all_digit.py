def Addition(num):
    if num==0:
        return 0
    return (num%10)+Addition(num//10)
num=123
print(Addition(num))