from collections import deque

###################

def bfs(x):
    q.append(x)
    c = [-1 for _ in range(num_friend)]
    c[x] = 0
    while q:
        x = q.popleft()
        for i in a[x]:
            if c[i] == -1:
                c[i] = c[x] + 1
                q.append(i)

    cnt = 0
    for i in range(num_friend):
        if c[i] != -1:
            cnt += c[i]
    return cnt

#######################

num_friend, num_relations = map(int, input().split())
a = [[] for _ in range(num_friend)]
q, res, Kevin_Bacon = deque(), [], []

for _ in range(num_relations):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    a[x].append(y)
    a[y].append(x)

for i in range(num_friend):
    res.append(bfs(i))

for i in range(num_friend):
    if res[i] == min(res):
        Kevin_Bacon.append(i)
print(min(Kevin_Bacon)+1)