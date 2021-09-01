# 2021-09-01

# 출처 : https://www.acmicpc.net/problem/14567

from collections import deque

# 노드(과목)의 수와 간선(선수 조건)의 수 입력받기
N,M=map(int,input().split())

# 모든 과목과 연결된 선수 조건의 정보를 0으로 초기화
indegree=[0]*(N+1)
# 각 과목에 연결된 선수 조건의 정보를 담기 위한 연결 리스트 초기화
graph=[[] for i in range(N+1)]
# 과목 순서대로 최소 몇 학기에 이수할수 있을지 출력
answer=[0]*(N+1)
# 방향 그래프의 모든 선수 조건의 정보를 입력 받기
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    # 진입차수를 1 증가
    indegree[b]+=1

# 위상 정렬 함수
def topology_sort():
    q=deque()
    # 처음 시작할때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)
            answer[i]=1
    # 큐가 빌때까지 반복
    while q:
        now=q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i]-=1
            answer[i]=answer[now]+1
            #새롭게 진입차수가 0이되는 노드를 큐에 삽입
            if indegree[i]==0:
                q.append(i)

    for i in range(1,len(answer)):
        print(answer[i],end=' ')

topology_sort()

