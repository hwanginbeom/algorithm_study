import sys, heapq
input = sys.stdin.readline

n, graph = int(input()), []
for i in range(n):
    for i2 in list(map(int, input().split())):
        heapq.heappush(graph, i2)
        if len(graph) > n:
            heapq.heappop(graph)
print(graph[0])
