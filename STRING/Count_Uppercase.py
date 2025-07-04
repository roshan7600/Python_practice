s='RosHa&n@P'
count=0
for ch in s:
    if 'A'<=ch<='Z':
        count+=1
print(count)        


# COUNT LOWER CASE LETTER

s='RosHa&n@P'
count=0
for ch in s:
    if 'a'<=ch<='z':
        count+=1
print(count)        


# COUNT SPECIAL CHARACTER


s='Ro#sHa&n@P'
count=0
for ch in s:
    if not('a'<=ch<='z' or 'A'<=ch<='Z'):
        count+=1
print(count)        
