s='madam'

for ind in range(len(s)//2):
    if s[ind]!=s[-ind-1]:
        print('not a palindrome')
        break
else:
    print('palindrome')    