s='hello'
rev=''

# 1st methods

# for ch in range(len(s)-1,-1,-1):
#     rev+=s[ch]
# print(rev)    


# 2nd method

for ch in s :
    rev=ch+rev
print(rev)    