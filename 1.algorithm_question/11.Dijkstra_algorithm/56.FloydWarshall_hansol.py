# 최단 경로 알고리즘
# Floyd - Warshall algorithm
# 키 순서
# https://www.acmicpc.net/problem/2458

# 학생들의 키를 비교한 결과가 주어질 때,
# 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명인지 계산하여 출력하는 프로그램을 작성하시오.

# 풀이
# 각 학생을 도시라고 생각하면 자신의 키가 몇 번째인지 알 수 있는 학생은
# 모든 도시와 연결되어 있는 도시라고 할 수 있다.
# 즉, 해당 도시로 오는 도시 + 해당 도시에서 갈 수 있는 도시 = 모든 도시 를 만족하는 도시이다.
# 각 도시로 가는 경로를 카운트하고, 서로에 대해 연결 되어 있는지 확인하는 코드를 작성하여 해결했다.
# 키 비교이기 때문에 편도 경로만 존재함을 주의해야 한다.

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 1라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 각 노드에 대해 모든 노드에 가는 경로를 입력
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 연결 여부를 보기 위해 0으로 이루어진 리스트(graph 변수와 같은 형식)를 가진 리스트를 생성
answer = [[0] * (n + 1) for i in range(n + 1)]
# print(answer)

for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 0이 아니면 이미 처리된 요소이므로 pass
        if answer[a][b] != 0:
            pass
        else:
            # 서로에 대해 길이가 무한이면 연결되지 않았으므로 Not Connected
            if graph[a][b] == graph[b][a] == INF:
                answer[a][b] = 'NC'
                answer[b][a] = 'NC'
            # 연결되었으면 서로에 대해 Connected
            else:
                answer[a][b] = 'C'
                answer[b][a] = 'C'

# print(answer)
result = []
# NC가 없는, 즉, 모든 구간에 대해 Connected 인 노드의 개수를 출력
for i in range(1, n + 1):
    if 'NC' not in answer[i]:
        result.append(i)
    else:
        pass

print(len(result))

