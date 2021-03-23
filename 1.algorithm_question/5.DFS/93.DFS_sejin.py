n, m = map(int, input().split())
matrix=[[0]*(n+1)for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0]*(n+1)

def bfs(v):
    queue=[v]
    while queue:
        v=queue.pop(0)
        for i in range(1,n+1):
            if matrix[i][v]==1 and visit_list[i]==0:
                visit_list[i]=1
                queue.append(i)
answer=0
for i in range(1,n+1):
    if visit_list[i]==0:
        bfs(i)
        answer+=1