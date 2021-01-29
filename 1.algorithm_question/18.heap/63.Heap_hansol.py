# heap 자료 구조
# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []
# data 에 입력값 받기
for i in range(n):
    data.append(int(input()))

# 누적시키기 위한 result 를 설정하고 data 를 오름차순 정렬로 꺼내어 담기
result = 0
heapq.heapify(data)

# 입력값이 2개 이상일 때 작동
while len(data) > 1:
    # 비교할 가장 작은 값들을 꺼내어 a, b에 저장
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    # data 에 a와 b를 더한 값을 heap 구조로 누적
    heapq.heappush(data, a + b)
    # 계산한 값을 결과값에 누적
    result += (a + b)

print(result)
