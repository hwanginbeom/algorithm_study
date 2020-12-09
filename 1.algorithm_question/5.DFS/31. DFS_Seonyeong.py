## 2667번: 단지번호붙이기


n = int(input())
cnt = 0
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x - 1,y)
        dfs(x, y-1)
        dfs(x +1,y)
        dfs(x,y+1)
        return True
    return False

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

result = 0

cnt_list = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i,j) == True:
            result +=1
            cnt_list.append(cnt)

print(result)

cnt_list.sort()

for i in cnt_list:
    print(i)
