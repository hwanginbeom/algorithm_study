# 1. 별자리 만들기
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution1() :
    n = int(input())

    # 단순 노드번호가 아니라 x, y 좌표가 하나의 노드이기 때문에 리스트 사용X
    # dictionary 생성
    parent = {}

    pos = []

    for _ in range(n) :
        x, y = map(float, input().split())
        pos.append([x, y])

    edges = []

    # 모든 점과 점 사이의 거리 구하기
    for i in range(len(pos)) :
        # 각 노드의 부모노드 초기화
        parent[f'{pos[i][0]}, {pos[i][1]}'] = f'{pos[i][0]}, {pos[i][1]}'

        for j in range(i + 1, len(pos)) :
            cost = math.sqrt((pos[j][0] - pos[i][0]) ** 2 + (pos[j][1] - pos[i][1]) ** 2)
            edges.append((cost, pos[i], pos[j]))

    # print('parent :', parent)
    # print('edges :', edges)

    edges.sort()
    result = 0

    for edge in edges :
        cost, x, y = edge

        if find_parent(parent, f'{x[0]}, {x[1]}') != find_parent(parent, f'{y[0]}, {y[1]}') :
            union_parent(parent, f'{x[0]}, {x[1]}', f'{y[0]}, {y[1]}')
            result += cost

    print(result)


# solution1()



# 2. 골드바흐의 추측
import math


def solution2() :
    t = int(input())
    prime_list = []

    for _ in range(t) :
        n = int(input())

        array = [True for _ in range(n + 1)]

        for i in range(2, int(math.sqrt(n)) + 1) :
            j = 2

            while i * j <= n :
                array[i * j] = False
                j += 1

        a = n // 2
        b = a

        while True :
            if array[a] and array[b] :
                print(a, end = ' ')
                print(b)
                break
            else :
                a -= 1
                b += 1


solution2()



# 3. 문제집
import heapq


def solution3() :
    n, m = map(int, input().split())

    # 각 노드의 진입차수
    indegree = [0] * (n + 1)

    graph = [[] for _ in range(n + 1)]

    for _ in range(m) :
        a, b = map(int, input().split())

        graph[a].append(b)
        indegree[b] += 1

    # print('graph :', graph)

    # 위상 정렬 함수
    def topology_sort():
        # 알고리즘 수행 결과를 담을 리스트
        result = []

        # 우선순위 큐 사용
        q = []

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, n + 1):
            if indegree[i] == 0:
                heapq.heappush(q, i)

        # 큐가 빌 때까지 반복
        while q:

            # print('queue :', q)

            # 큐에서 원소 꺼내기
            now = heapq.heappop(q)
            result.append(now)

            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                indegree[i] -= 1

                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    heapq.heappush(q, i)

        # 위상 정렬을 수행한 결과 출력
        for i in result:
            print(i, end=' ')

    topology_sort()


# solution3()
