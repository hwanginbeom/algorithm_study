count = 0
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    global count
    count += 1
    # print(count)
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

computer = int(input())
connect_num = int(input())
node = []

for i in range(0,computer+1):
    node.append([])
for i in range(0,connect_num):
    node_num, connect = list(map(int, input().split()))
    node[node_num].append(connect)
    node[connect].append(node_num)

print(node)
visited = [False] * (computer+1)
dfs(node, 1, visited)
count = count-1
print(count)