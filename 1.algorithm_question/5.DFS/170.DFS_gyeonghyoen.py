import sys
import copy

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(x, y, graph, k, n):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] >= k:
        graph[x][y] = 0
        # 상하좌우
        dfs(x - 1, y, graph, k, n)
        dfs(x + 1, y, graph, k, n)
        dfs(x, y - 1, graph, k, n)
        dfs(x, y + 1, graph, k, n)
        return True
    return False


def solution():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    min_num = min(min(graph))
    max_num = max(max(graph))
    answer = []
    for k in range(min_num, max_num + 1):
        cnt = 0
        graph2 = copy.deepcopy(graph)
        for i in range(n):
            for j in range(n):
                if dfs(i, j, graph2, k, n):
                    cnt += 1
        answer.append(cnt)
    return max(answer)


print(solution())
