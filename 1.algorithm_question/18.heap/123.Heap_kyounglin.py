# 2021-07-07

import heapq
import sys

# input=sys.stdin.readlines()

n = int(sys.stdin.readline())

# 1,5,2,10,-99,7,5

max_heap = []
min_heap = []

for _ in range(n):
    number = int(sys.stdin.readline())

    if len(min_heap) == len(max_heap):
        heapq.heappush(min_heap, -number)

    else:
        heapq.heappush(max_heap, number)

    if max_heap and -min_heap[0] > max_heap[0]:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-min_heap[0])
