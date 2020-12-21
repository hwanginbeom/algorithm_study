import sys

# 입력부
n, m, k = map(int, sys.stdin.readline().split())
money = list(map(int, sys.stdin.readline().split()))

# 인접리스트 생성|
adj = [[] for _ in range(n)]

ans = []
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    # 양방향 간선
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

# 방문 여부를 확인하는 배열
check = [False] * n

# dfs_list : 친구관계에 속하는 정점을 리턴하는 함수
def dfs_list(x, store):
    check[x] = True
    for i in adj[x]:
        if check[i] == False:
            store.append(i)
            dfs_list(i, store)
    return store

for i in range(n):
    # 만일 정점 i가 False라면 다른 연결 요소에 있기 때문에 dfs_list를 호출한다
    if check[i] == False :
        each = dfs_list(i, [i])
        temp = 999999999999
        # 정점 i와 친구관계인 정점들 중 가장 싼 친구비를 찾는다
        for j in each:
            if temp > money[j]:
                temp = money[j]
        # 연결요소의 최소비용을 정답배열에 추가한다
        ans.append(temp)

# 예산범위에 맞는지 확인한다
if sum(ans) <= k:
    print(sum(ans))
else:
    print('Oh no')