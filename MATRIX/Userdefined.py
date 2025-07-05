m=[]
row=int(input('enter a row: '))
col=int(input('enter a col: '))

for r in range(row):
    line=[]
    for c in range(col):
        line.append(int(input('enter a element: ')))
    m.append(line)    
print(m)    