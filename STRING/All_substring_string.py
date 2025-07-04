s='abcde'
for si in range(len(s)):
    for ei in range(si+1,len(s)+1):
        print(s[si:ei])