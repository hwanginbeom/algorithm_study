# 9. 기타 알고리즘
# Two Pointer
# https://www.acmicpc.net/problem/1644

import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
data = []   # 소수 정렬을 만들어 줄 리스트 생성

# 입력값까지의 소수로 이루어진 리스트를 생성
for _ in range(2, N + 1):
    if is_prime_number(_):
        data.append(_)

# Two Pointer 합 계산 (강의 참고)
count = 0
interval_sum = 0
end = 0

# start 를 차례대로 증가시키며 반복
for start in range(len(data)):
    # end 를 가능한 만큼 이동시키기
    while interval_sum < N and end < len(data):
        interval_sum += data[end]
        end += 1
    # 부분합이 N일 때 카운트 증가
    if interval_sum == N:
        count += 1
    interval_sum -= data[start]

print(count)
