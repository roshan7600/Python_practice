s='engineering'
vowels=''
for ch in s:
    if ch in "AEIOUaeiou":
        vowels+=ch
print(vowels)        


# PRINT  ALL CONSONENT IN A STRING


s='engineering'
consonent=''
for ch in s:
    if (ch not in "AEIOUaeiou"):
        consonent+=ch
print(consonent) 