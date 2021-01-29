import heapq
import sys
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n) :
    list.append(int(input()))

result = 0
heapq.heapify(list)
while len(list) > 1 :
    a = heapq.heappop(list)
    b = heapq.heappop(list)
    heapq.heappush(list, a+b)
    result += (a+b)

print(result)
