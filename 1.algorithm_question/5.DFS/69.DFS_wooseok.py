# 알파벳
r, c = map(int, input().split())

graph = []

# 알파벳과 인덱스 활용
for _ in range(r) :
    alpha_list = list(input())
    for i in range(len(alpha_list)) :
        alpha_list[i] = ord(alpha_list[i]) - 65

    graph.append(alpha_list)

# 초기 단계 세팅
max_value = 1
check_alpha = [0] * 26
check_alpha[graph[0][0]] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, count):
    global max_value

    max_value = max(max_value, count)

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        # 주어진 범위를 벗어나는 경우 다음 단계로 이동
        if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
            continue

        # 현재 노드를 아직 방문하지 않았다면
        if check_alpha[graph[nx][ny]] == 0 :
            check_alpha[graph[nx][ny]] = 1

            dfs(nx, ny, count + 1)

            # 탐색 끝나고 원상복구 -> 백트래킹
            check_alpha[graph[nx][ny]] = 0


dfs(0, 0, max_value)

print(max_value)
