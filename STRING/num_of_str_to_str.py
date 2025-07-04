s='3q2s4a2h'
rev=''
dig=''
for ind in range(len(s)):
    if s[ind].isdigit():
        dig+=s[ind]
    else:
        rev+=int(dig)*s[ind]    
        dig=''
print(rev)        