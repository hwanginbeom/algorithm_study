# heap 자료 구조
# N번째 큰 수
# https://www.acmicpc.net/problem/2075

import heapq

N = int(input())
heap = []
# 첫 줄 입력받기
for n in map(int, input().split()):
    heapq.heappush(heap, n)
# 두 번째 줄부터 N번째 줄까지
for _ in range(N - 1):
    # 길이 N을 유지하면서 원소를 입력받고 최상단 노드(최솟값)을 제거하는 작업을 반복
    for n in map(int, input().split()):
        heapq.heappush(heap, n)
        heapq.heappop(heap)
# 최댓값 5개만 남김
print(heap[0])

# Solution 2
# 한 번에 입력받고 한 번에 N개의 최댓값을 제외하고 제거

# n = int(input())
# arr = []
# for _ in range(n):
#     arr.extend(list(map(int, input().split())))
#     arr.sort(reverse=True)
#     arr = arr[:n]
# print(arr[-1])
