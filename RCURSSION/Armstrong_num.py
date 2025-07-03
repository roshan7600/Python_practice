def Armstrong(num,pow):
    if num==0:
        return 0
    return (num%10)**pow+Armstrong(num//10,pow)
num=153
print('armstrong' if Armstrong(num,len(str(num))) else 'not')