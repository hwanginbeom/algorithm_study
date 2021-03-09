n = int(input())
a, b = map(int, input().split())
m = int(input())


def dfs(vertex):
    global result
    if result > 0:  # a -> b 까지 도착했으므로 result 의 값이 변했다. 결과가 나왔기에 다른 모든 함수를 종료
        return

    if vertex == b:  # a -> b 까지 도착
        result = visit.count(True) - 1  # 촌수는 배열의 길이에서 -1 | ex) 나-아빠-할아버지 : 2촌
        return

    for neighbor in adj[vertex]:  # 현재노드와 인접한 노드 중에서
        if visit[neighbor] is False:  # 방문하지 않은 노드가 있으면
            visit[neighbor] = True  # 방문
            dfs(neighbor)  # 노드를 들고 다시 dfs
            visit[neighbor] = False  # 원하는 값에 도달하지 못하고 나오면 방문 목록에서 제거

    return


# 그래프 문제의 기본!! 인접xx 중 하나 작성하기, 여기서는 인접리스트 사용
adj = [[] for _ in range(n+1)]
for _ in range(m):  # 방향이 없는 그래프이므로 s->e, e->s 둘다 넣어준다.
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

result = -1  # 촌수를 따질 수없을 때는 -1 이므로 -1로 두고 시작
visit = [False]*(n+1)  # 방문했는지 아닌지를 확인하기 위해 visit 배열 사용 ( 나중에 이 배열의 길이로 촌수를 계산 )
visit[a] = True  # a 를 시작으로 두고
dfs(a)  # dfs 함수시작!

print(result)