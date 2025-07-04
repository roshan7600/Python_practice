def Longest_word(s):
    word=s.split()
    longest=max(word,key=len)
    return longest
s=input('enter a any sentence: ')
print(Longest_word(s))