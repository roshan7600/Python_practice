num=13
print('prime' if len([val for val in range(1,num+1) if num%val==0])==2 else 'not')