# N으로 표현
#################
def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        num_set = { int(str(N) * i) }

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    num_set.add(x + y)
                    num_set.add(x - y)
                    num_set.add(x * y)

                    if y != 0:
                        num_set.add(x // y)

        if number in num_set:
            return i

        DP.append(num_set)

    return answer

#################
# 정수 삼각형
#################

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    return max(triangle[-1])


#################
# 가장 먼 노드
#################

def solution(n: int, edge: int) -> int:
    graph = [[] for _ in range(n)]
    distances = [0 for _ in range(n)]
    is_visited = [False for _ in range(n)]
    # 시작 노드 방문
    queue = [0]
    is_visited[0] = True
    # 노드 연결
    for (a, b) in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # queue 이용 distance 계산
    while queue:
        i = queue.pop(0)
        # i에서 갈수 있는 j
        for j in graph[i]:
            if is_visited[j] == False:
                # 갈 수 있으면 앞의 점까지의 거리 + 거리를 1 씩 더한다
                # 시작점의 거리는 0으로 초기화되어 있다.
                is_visited[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    answer = distances.count(max(distances))
    # max 값의 수를 센다
    return answer