import sys
input = sys.stdin.readline

import heapq

n = int(input())
nums = []
for _ in range(n) :
    x = int(input())

    if x != 0 :
        heapq.heappush(nums, (abs(x), x)) # (우선순위, 값)
    else :
        if nums :
            print(heapq.heappop(nums)[1])
        else :
            print(0)