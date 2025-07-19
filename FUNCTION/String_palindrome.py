def palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

s = input('Enter a string: ')
print('palindrome' if palindrome(s) else 'not')
