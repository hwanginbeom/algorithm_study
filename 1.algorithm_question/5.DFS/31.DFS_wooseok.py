# 단지번호붙이기
def dfs(x, y) :
    global count

    if x <= -1 or x >= n or y <= -1 or y >= n :
        return False

    if graph[x][y] == 1 :
        graph[x][y] = 0
        count += 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

        return count

    return False


n = int(input())
graph = []

for _ in range(n) :
    line = input()
    temp = []

    for i in line :
        temp.append(int(i))

    graph.append(temp)

answer = []
count = 0
result = 0

for i in range(n) :
    for j in range(n) :
        a = dfs(i, j)

        if a :
            answer.append(a)
            result += 1

        count = 0

answer.sort()

print(result)

for i in answer :
    print(i)
