s='madam'
for si in range(len(s)):
    for ei in range(si+1,len(s)+1):
        word=s[si:ei]
        if word==word[::-1]:
            print(word)