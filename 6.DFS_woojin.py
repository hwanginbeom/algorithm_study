num_com = int(input())
num_pair = int(input())
graph = {}


for i in range(num_com):
    graph[i+1] = set()

for j in range(num_pair):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
         node = stack.pop()
         if node not in visit:
             visit.append(node)
             stack.extend(graph[node])

    return (len(visit)-1)

print(dfs(graph, 1))