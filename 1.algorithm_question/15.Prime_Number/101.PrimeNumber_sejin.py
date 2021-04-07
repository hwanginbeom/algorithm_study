import sys
input = sys.stdin.readline

import math
t = int(input())
data = []
for _ in range(t):
    data.append(int(input()))

# def로 풀면 시간초과
# def is_prime_number(x) :
#     if x == 1 :
#         return False
#     else :
#         for i in range(2, int(math.sqrt(x)) + 1) :
#             if x % i == 0 :
#                 return False
#         return True

m = max(data)
array = [False, False] + [True] * m
for i in range(2, int(math.sqrt(m)) + 1):
    if array[i]:
        for j in range(i+i, m+1, i):
            if array[j]:
                array[j] = False

for i in data:
    count = 0
    for j in range(2, (i//2)+1):
        if array[j] and array[i-j]:
            count += 1
    print(count)
