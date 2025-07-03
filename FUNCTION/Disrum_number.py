def Armstrong(num,pos,dup,total=0):
    while num!=0:
        rem=num%10
        total+=rem**pos
        num//=10
        pos-=1
    return 'Disrum number' if dup==total else 'not '    
num=int(input('enter a number: '))    
print(Armstrong(num,len(str(num)),num))