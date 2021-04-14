import sys
input = sys.stdin.readline

n, h = map(int, input().split())

up = [0] * (h + 1)
down = [0] * (h + 1)
answer = []

for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 1:
        down[num] += 1
    else:
        up[num] += 1

for j in range(h - 1, 0, -1):
    up[j] += up[j + 1]
    down[j] += down[j + 1]

for k in range(1, h + 1):
    answer.append(down[k] + up[h + 1 - k])

result = 0
m = min(answer)
for i in answer:
    if i == m:
        result += 1
print(m, result)

# 시간초과
#
# import sys
# input = sys.stdin.readline
#
# n, h = map(int, input().split()) # n:길이, h:높이
#
# up = [0] * (h)
# down = [0] * (h)
#
# for i in range(n):
#     if i%2:
#         for j in range(h-int(input())+1):
#             down[j] += 1
#     else:
#         for k in range(int(input())):
#             up[k] += 1
#
# result = int(1e9)
# updown = []
# for i in range(len(down)):
#     updown.append(up[i] + down[len(down)-i-1])
#     result = min(result, up[i] + down[len(down)-i-1])
# print(result, updown.count(result))
