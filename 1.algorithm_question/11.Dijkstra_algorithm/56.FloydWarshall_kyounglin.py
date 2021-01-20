# 2021-01-20

# 출처 : https://www.acmicpc.net/problem/2458

# 키 순서

INF = int(1e9)

n,m = map(int,input().split())

# 2차원 리스트 만들기
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기자신은 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 키 비교에 대한 정보 받기
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

#플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k]==1 and graph[k][b]==1:
                graph[a][b]=1


# 수행 결과 출력 - 대소관계가 있는 노드들에 대해 횟수를 더해주고 이 값이 전체 학생수 N보다 1이 작은 수이면 해당 노드는 자신이 학급에서 얼마나 큰지 알 수 있게 된다.
cnt=[0]*(n+1)
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==1:
            cnt[a]+=1
            cnt[b]+=1

print(cnt.count(n-1))

