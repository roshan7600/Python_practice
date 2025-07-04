s='engineering'
while len(s) !=0:
    print(f'{s[0]} = {s.count(s[0])}')
    s=s.replace(s[0],'')
    