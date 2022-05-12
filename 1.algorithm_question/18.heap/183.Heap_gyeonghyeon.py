import heapq
import sys

input = sys.stdin.readline


def solution():
    q = []
    n = int(input())
    for _ in range(n):
        x = int(input())
        if x != 0:
            heapq.heappush(q, (-x, x))
        else:
            y = 0
            if q:
                _, y = heapq.heappop(q)
            print(y)


solution()
