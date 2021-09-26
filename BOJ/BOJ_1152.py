# str = input().split(' ')
# print(len(str) - str.count(''))

import sys
s = sys.stdin.readline().strip()
if s:
    print(s.count(' ') + 1)
else:
    print('0')
