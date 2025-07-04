s='ros%h*an patel'
rev=''
# print(s.upper())  Using buit-in function 

# Without any built in function

for ch in s:
    if 'a'<=ch<='z':
        rev+=chr(ord(ch)-32)
    else:
        rev+=ch
print(rev)            


# LOWER CASE TO UPPER CASE


for ch in s:
    if 'A'<=ch<='Z':
        rev+=chr(ord(ch)+32)
    else:
        rev+=ch
print(rev)            
