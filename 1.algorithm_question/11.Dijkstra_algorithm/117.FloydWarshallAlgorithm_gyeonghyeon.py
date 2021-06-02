def getpt(i):
    visited = [False for _ in range(n+1)]
    q = [i]
    visited[i] = True
    point = -1
    while len(q) > 0:
        qsize = len(q)
        for _ in range(qsize):
            h = q.pop()
            for j in g[h]:
                if visited[j]:
                    continue
                visited[j] = True
                q.insert(0, j)
        point += 1
    return point


n = int(input())
g = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == -1:
        break
        break
    if b not in g[a]:
        g[a].append(b)
    if a not in g[b]:
        g[b].append(a)


p = [0 for _ in range(n+1)]
for i in range(1, n+1):
    p[i] = getpt(i)

m = min(p[1:])
candidates = []
for i, x in enumerate(p):
    if i == 0:
        continue
    if x == m:
        candidates.append(str(i))

print(m, len(candidates))
print(' '.join(candidates))
