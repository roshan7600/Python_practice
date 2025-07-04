s='aaabbccab'
rev=''
count=1
for ind in range(len(s)-1):
    if s[ind]==s[ind+1]:
        count+=1
    else:
        rev+=str(count)+s[ind]    
        count=1
rev+=str(count)+s[ind+1]        
print(rev)