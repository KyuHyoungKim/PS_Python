# import sys
# N = int(sys.stdin.readline())
# score_list = list(map(int,sys.stdin.readline().split()))

# sum = 0
# max = -1
# sum(score_list)
# for score in score_list:
#     score = int(score)
#     sum += score
#     if max < score:
#         max = score
#
# res = float(sum) / max / N * 100
#
# print(res)
N = int(input())
score_list = list(map(int, input().split()))

print('%.2f' % float(sum(score_list)/max(score_list)/N*100))
