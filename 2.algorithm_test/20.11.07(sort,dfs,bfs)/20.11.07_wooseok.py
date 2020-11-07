# 1
# 11분
def solution1(array, commands):
    answer = []

    for li in commands:
        start_index = li[0] - 1
        end_index = li[1]
        find_index = li[2] - 1

        new_arr = array[start_index:end_index]
        new_arr.sort()

        answer.append(new_arr[find_index])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution1(array, commands))



# 2
#
def dfs2(numbers, target, count):
    global answer

    if count == len(numbers):
        if sum(numbers) == target:
            answer += 1
    else:
        numbers[count] *= 1
        count += 1
        dfs2(numbers, target, count)

        count -= 1

        numbers[count] *= -1
        count += 1
        dfs2(numbers, target, count)


answer = 0


def solution2(numbers, target):
    global answer
    count = 0

    dfs2(numbers, target, count)

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution2(numbers, target))



# 3
# 23분
def dfs3(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs3(graph, i, visited)


def solution3(n, computers):
    answer = 0

    graph = [[] for i in range(n)]

    # 컴퓨터 연결 상태 그래프로 변환
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            elif computers[i][j] == 1:
                if j not in graph[i]:
                    graph[i].append(j)
                    graph[j].append(i)

    # print(graph)

    visited = [False] * n

    for i in range(len(visited)):
        if not visited[i]:
            dfs3(graph, i, visited)
            answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution3(n, computers))
