# 2021-04-01

# 출처 : https://www.acmicpc.net/problem/1766

# 문제집
#
# 민오는 1번부터 N번까지 총 N개의 문제로 되어 있는 문제집을 풀려고 한다. 문제는 난이도 순서로 출제되어 있다. 즉 1번 문제가 가장 쉬운 문제이고 N번 문제가 가장 어려운 문제가 된다.
#
# 어떤 문제부터 풀까 고민하면서 문제를 훑어보던 민오는, 몇몇 문제들 사이에는 '먼저 푸는 것이 좋은 문제'가 있다는 것을 알게 되었다. 예를 들어 1번 문제를 풀고 나면 4번 문제가 쉽게 풀린다거나 하는 식이다. 민오는 다음의 세 가지 조건에 따라 문제를 풀 순서를 정하기로 하였다.
#
# N개의 문제는 모두 풀어야 한다.
# 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
# 가능하면 쉬운 문제부터 풀어야 한다.
# 예를 들어서 네 개의 문제가 있다고 하자. 4번 문제는 2번 문제보다 먼저 푸는 것이 좋고, 3번 문제는 1번 문제보다 먼저 푸는 것이 좋다고 하자. 만일 4-3-2-1의 순서로 문제를 풀게 되면 조건 1과 조건 2를 만족한다. 하지만 조건 3을 만족하지 않는다. 4보다 3을 충분히 먼저 풀 수 있기 때문이다. 따라서 조건 3을 만족하는 문제를 풀 순서는 3-1-4-2가 된다.
#
# 문제의 개수와 먼저 푸는 것이 좋은 문제에 대한 정보가 주어졌을 때, 주어진 조건을 만족하면서 민오가 풀 문제의 순서를 결정해 주는 프로그램을 작성하시오.

import heapq

# 노드의 수와 간선의 수를 입력 받기
n,m=map(int,input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree=[0]*(n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph=[[] for i in range(n+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b) # 정점 a->b로 이동
    # 진입 차수를 1 증가
    indegree[b]+=1


# 위상 정렬 함수
def topology_sort():
    result =[] # 알고리즘 수행 결과를 담을 리스트
    q=[]
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,n+1):
        if indegree[i]==0:
            heapq.heappush(q,i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now=heapq.heappop(q)
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i]-=1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i]==0:
                heapq.heappush(q,i)
    # 위상정렬을 수행한 결과 출력
    for i in result:
        print(i,end=' ')

topology_sort()
