# 9. 기타 알고리즘
# 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

import math

# 소수 판별 함수 정의
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# N 이하의 소수 리스트를 반환하는 함수
def prime_num_list(N):
    array = [True for i in range(N + 1)]
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
    return data


# 입력값 받기
T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))

for n in lst:
    target = 0
    # n/2 이하의 소수 리스트에서 하나씩 꺼내어
    for i in prime_num_list(n//2):
        # n - 꺼낸 값 이 소수인 경우 target 에 반환
        if is_prime_number(n - i):
            target = max(target, i) # 최댓값 찾기
    print(target, n - target, sep=' ')
