# Sieve of Eratosthenes
# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

import math

# 0이 나올때까지 입력값 받기
arr = []
while True:
    arr.append(int(input()))
    if 0 in arr: break

# 최대값 설정
N = 2 * 123456
# 소수가 True 인 에라토스테네스의 체 리스트 생성
array = [False, False] + [True for _ in range(N + 1)]
for i in range(2, int(math.sqrt(N)) + 1):
    if array[i]:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

# 정답을 저장하는 리스트
cnt_lst = []
# 0 이전까지 각각의 수에 대하여
for i in arr[:-1]:
    cnt = 0
    # 입력값보다 크고 2배값 이하인 소수이면 카운트
    for j in array[i + 1:2 * i + 1]:
        if j: cnt += 1
    cnt_lst.append(cnt)

for answer in cnt_lst:
    print(answer)


# Solution 2
# 0 이전까지 입력하는 방식을 while 문을 사용해 작성
# 에라토스테네스의 체 작성 과정 True 리스트에서 합성수를 False 로 바꾸는 방식
# 정답을 0부터 1씩 더하는 식이 아닌 count 로 해결

# N = int(input())
# sieve = [True] * 246913
#
# for i in range(2, int(246913 ** 0.5 + 1)):
#     if sieve[i]:
#         for j in range(i+i , 246913 , i):
#             sieve[j] = False
#
# while N != 0:
#     print(sieve[N+1:2*N+1].count(True))
#     N = int(input())
