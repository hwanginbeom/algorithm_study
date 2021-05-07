from collections import deque

N = int(input())
q = deque(enumerate(map(int, input().split())))
answer = []

while True:
    idx, paper = q.popleft()
    answer.append(idx + 1)

    if not q:
        break

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, answer)))


