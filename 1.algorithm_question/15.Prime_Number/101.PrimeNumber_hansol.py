# Prime Number
# 골드바흐 파티션
# https://www.acmicpc.net/problem/17103

import math

# 소수 판별 함수 정의
# def is_prime_number(x):
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

arr = [int(input()) for i in range(int(input()))]
N = max(arr)

array = [False, False] + [True for _ in range(N + 1)]
for i in range(2, int(math.sqrt(N)) + 1):
    if array[i]:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

data = []
for i in range(2, len(array)):
    if array[i]:
        data.append(i)


cnt_lst = []
for n in arr:
    cnt = 0
    for i in range(2, (n//2) + 1):
        if array[i] and array[n - i]:
            cnt += 1
    cnt_lst.append(cnt)

for answer in cnt_lst:
    print(answer)
