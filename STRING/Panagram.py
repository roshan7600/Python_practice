s='the quick brown for jumps over the lazy dog'

for ch in range(ord('a'),ord('z')+1):
    if chr(ch) not in s:
        print('not panagram')
        break
else:
    print('panagram')    