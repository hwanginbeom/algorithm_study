# 설탕 배달
# https://www.acmicpc.net/problem/2839

# 풀이
# 입력값에서 5씩 줄여나가며 count를 세고 3으로 나누어 떨어지는지 여부를 확인한다.
# 단, 5의 배수일 경우. 즉, 5씩 줄여나가다가 0이 되면 count 값을 정답으로 출력한다.

import sys

N = int(sys.stdin.readline())

cnt = 0
answer = -1
while N >= 3:
    if N%3 == 0:
        answer = N/3 + cnt
    N -= 5
    cnt += 1
    if N == 0:
        answer = cnt

print(round(answer))
