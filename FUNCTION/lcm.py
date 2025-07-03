def lcm(a,b,c):
    # if a >b and a>c:
    #     lcm=a
    # elif b > c:
    #     lcm=b
    # else:
    #     lcm=c
        lcm = max(a, b, c)

        while True:
            if lcm % a==0 and lcm % b==0 and lcm % c==0:
                return lcm
            lcm+=1        
    

a=int(input('enter a number: '))  
b=int(input('enter a number: '))  
c=int(input('enter a number: '))  
print(lcm(a,b,c))
  