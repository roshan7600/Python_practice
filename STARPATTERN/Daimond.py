num = int(input("Enter number of rows for the diamond: "))

# Top Half (Pyramid)
star = 1
space = num - 1
for row in range(1, num + 1):
    print('  ' * space + '* ' * star)
    star += 2
    space -= 1

# Bottom Half (Inverted Pyramid)
space = 1
star = (num * 2) - 3  
for row in range(1, num):
    print('  ' * space + '* ' * star)
    star -= 2
    space += 1
