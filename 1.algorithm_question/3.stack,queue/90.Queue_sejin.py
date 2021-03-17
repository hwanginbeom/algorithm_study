import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())  # n:큐의크기, m:뽑아내려는수
want = list(map(int, input().split()))
queue = deque(i for i in range(1, n + 1))


def min_count(x, y):
    count = 0
    if x.index(y) <= len(x) - x.index(y):
        count = x.index(y)
        for _ in range(x.index(y)):
            a = x.popleft()
            x.append(a)
    else:
        count = len(x) - x.index(y)
        for _ in range(len(x) - x.index(y)):
            a = x.pop()
            x.appendleft(a)
    return x, count


answer = 0
for i in want:
    queue, count = min_count(queue, i)
    answer += count

    if queue[0] == i:
        queue.popleft()
        pass

print(answer)
