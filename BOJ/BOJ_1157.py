# s = input().strip()
# s = s.upper()
#
# cnt = [0 for i in range(26)]
# res = '?'
# max_cnt = 0
# A_ascii = ord('A')
#
# for c in s:
#     idx = ord(c) - A_ascii
#     cnt[idx] = cnt[idx] + 1
#     if cnt[idx] < max_cnt:
#         continue
#     elif cnt[idx] == max_cnt:
#         res = '?'
#     else:
#         res = c
#         max_cnt = cnt[idx]
#
# print(res)

# s = input().strip()
# s = s.upper()
# cnt = []
#
# for i in range(ord('A'),ord('Z') + 1):
#     cnt.append(s.count(chr(i)))
# if cnt.count(max(cnt)) > 1:
#     print('?')
# else:
#     print(chr(cnt.index(max(cnt)) + ord('A')))

import sys
s = sys.stdin.readline().strip()
s = s.upper()

cnt = [0] * 26
res = '?'
max_cnt = 0
A_ascii = ord('A')

for i in range(ord('A'),ord('Z') + 1):
    cnt_tmp = s.count(chr(i))
    if max_cnt < cnt_tmp:
        max_cnt = cnt_tmp
        res = chr(i)
    elif max_cnt == cnt_tmp:
        res = '?'
    else:
        continue

print(res)

# 문자열 한것 번 다 돌면서 숫자를 세면서 갱신하는게 O(N)으로 제일 빠를 거라 생각했는데,
# 파이썬 문자열의 count함수 쓰는 것이 가장 빠른 듯
# 리스트에 인덱스로 접근해서 하나 더하는 방식이 느린건지 혹은
# 문자열의 count 함수가 문자열의 저장 방식 등에 의해 O(N)보다 빠른건지
# 그리고 upper나 lower함수도 O(N)이 맞는지 찾아볼 것
