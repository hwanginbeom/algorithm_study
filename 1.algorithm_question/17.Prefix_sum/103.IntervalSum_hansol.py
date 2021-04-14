# Prefix Sum
# 개똥벌레
# https://www.acmicpc.net/problem/3020

import sys

N, H = map(int, sys.stdin.readline().split())
top = [0] * (H + 1) # 종유석
bottom = [0] * (H + 1) # 석순

# 입력값을 종유석과 석순을 구분하여 분류
for i in range(N):
    num = int(input())
    if i % 2:
        top[num] += 1
    else:
        bottom[H - num + 1] += 1

# 종유석은 높이 H부터 하나씩 줄여가며 개수 세기
for i in range(H - 1, 0, -1):
    top[i] += top[i + 1]

# 석순은 높이 1부터 하나씩 늘려가며 개수 세기
for i in range(1, H + 1):
    bottom[i] += bottom[i - 1]

total = [0] * (H + 1)
# 각각의 높이에서 석순과 종유석의 누적합 더해주기
for i in range(1, H + 1):
    total[i] = top[i] + bottom[i]

total = total[1:]
answer = min(total)
print(answer, total.count(answer))