n, k = map(int, input().split())

from collections import deque
queue = deque(i for i in range(1, n+1))
result = []

while len(queue) > 1 :
    for _ in range(k-1) :
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))

print("<%s>" %(', '.join(result)))


# 큐 알고리즘이 아닌 코딩
#
# n, k = map(int, input().split())
# circle = [i for i in range(1,n+1)]
# i = 0
#
# result = []
# while len(circle) > 1 :
#     i = i + k
#
#     if i > len(circle) :
#         i = i % len(circle)
#
#         if i == 0 :
#             i = i+ len(circle)
#
#     i = i-1
#     result.append(str(circle.pop(i)))
#
# print("<%s>" %(', '.join(result)))
