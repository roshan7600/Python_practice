num = int(input('Enter a number: '))

def prime(num):
    if num < 2:
        return False
    for val in range(2, int(num ** 0.5) + 1):
        if num % val == 0:
            return False
    return True    

def reverse(num, pos):
    rev = 0
    while num != 0:
        rem = num % 10
        rev += rem * pos
        pos //= 10
        num //= 10
    return rev  

pos = 10 ** (len(str(num)) - 1)

def emirp(num):
    rev = reverse(num, pos)
    if num != rev and prime(num) and prime(rev):
        return 'emirp num'
    return 'not a emirp'

print(emirp(num))
