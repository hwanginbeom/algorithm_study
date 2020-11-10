# K 번째 수
def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]
        end = command[1]
        select = command[2]

        focus = array[start-1:end]
        focus = sorted(focus)

        a = focus[select-1]
        answer.append(a)

    return answer

# 타겟 넘버
def solution(numbers, target):
    answer = 0
    sum_list = [0]
    temp_list = []

    for number in numbers:
        plus = number
        minus = -1 * number

        for middle_sum in sum_list:
            a , b= middle_sum + plus , middle_sum + minus
            temp_list.extend([a,b])

        sum_list = temp_list
        temp_list = []

    for k in sum_list:
        if k == target:
            answer += 1

    return answer

# 네트워크

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution(n, computers):
    answer = 0
    graph = [[] for i in range(n)]

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            elif computers[i][j] == 1:
                if j not in graph[i]:
                    graph[i].append(j)
                    graph[j].append(i)

    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited)
            answer+= 1

    return answer