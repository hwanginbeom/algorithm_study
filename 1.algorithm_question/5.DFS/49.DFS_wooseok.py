# 영역 구하기
import sys


# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y) :
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x < 0 or x >= m or y < 0 or y >= n :
        return False

    global count

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        count += 1

        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False


sys.setrecursionlimit(10 ** 7)

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]

# 그래프 그리기
# 모눈종이의 왼쪽 위를 (0, 0)으로, 오른쪽 아래를 (5, 7)로 설정
# 즉 위, 아래를 뒤집은 것
for _ in range(k) :
    y1, x1, y2, x2 = map(int, input().split())

    for i in range(x1, x2) :
        for j in range(y1, y2) :
            graph[i][j] = 1

areas = []
part = 0

# 깊이 우선 탐색
for i in range(m) :
    for j in range(n) :
        count = 0
        area = dfs(i, j)

        if area :
            areas.append(count)
            part += 1

areas.sort()

# 출력
print(part)
for i in areas :
    print(i, end = ' ')
