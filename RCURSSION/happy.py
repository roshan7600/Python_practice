def sq(num):
    if num==0:
        return 0
    return (num%10)**2+sq(num//10)
def check(num):
    if num <10:
        return num==1 or num==7
    return check(sq(num))
num=13
print('happy' if check(num) else 'not')
    