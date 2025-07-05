s = 'abcd'
print({s[ind]: s[ind] * (ind + 1) for ind in range(len(s))})
