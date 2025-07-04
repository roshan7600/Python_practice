s1='stone'
s2='notes'

if len(s1)==len(s2):
    for ch in s1:
        if (ch not in s2) or (s1.count(ch)!=s2.count(ch)):
            print('not a anagram')
            break
    else:
        print('Anagram')    
else:
    print('not a anagram')        
