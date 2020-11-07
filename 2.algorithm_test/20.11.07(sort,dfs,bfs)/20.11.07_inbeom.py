# test_number(sort)
def solution(array, commands):
    result=[]
    for i in commands:
        answer = array[i[0]-1:i[1]]
        answer.sort()
        result.append(answer[i[2]-1])
    return result

array = [1, 5, 2, 6, 3, 7, 4]

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array, commands)

# =======================================================
# network 45분
def dfs(graph, v, visited):
    visited[v] = True
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def node(computers):
    node = [[]]
    for i in computers:
        one_node = []
        for j in range(0, len(i)):
            if i[j] == 1:
                one_node.append(j+1)
        else:
            node.append(one_node)
    return node


def solution(n, computers):
    graph = node(computers)
    visited = [False] * (n + 1)
    count = 0
    for i in range(1,n+1):
        if visited[i] == False:
            count += 1
            dfs(graph, i, visited)
    answer = count
    return answer


n = 3

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n, computers)

# ===========================================