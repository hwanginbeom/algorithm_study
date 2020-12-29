from collections import deque

T = int(input())

for tc in range(1,T+1):
    K,M,P = map(int,input().split())

    indeg = [0]*(M+1)
    graph = dict()
    for i in range(1,M+1):
        graph[i] = []

    for _ in range(P):
        a, b = map(int,input().split())
        graph[a].append(b)
        indeg[b] += 1

    maxparent = [[0]*2 for _ in range(M+1)]
    queue = deque([])
    for i in range(1,M+1):
        if indeg[i] == 0:
            queue.append([i,1])

    maxdepth = 0
    while queue:
        index, depth = queue.popleft()
        if maxdepth < depth:
            maxdepth = depth
        for elem in graph[index]:
            spec = maxparent[elem][0]
            if spec < depth:
                maxparent[elem][0] = depth
                maxparent[elem][1] = 1
            elif spec == depth:
                maxparent[elem][1] += 1
            indeg[elem] -= 1
            if indeg[elem] == 0:
                specimen = maxparent[elem][0]
                numspec = maxparent[elem][1]
                if numspec == 1:
                    queue.append([elem,specimen])
                else:
                    queue.append([elem,specimen+1])
    print('{} {}'.format(K,maxdepth))