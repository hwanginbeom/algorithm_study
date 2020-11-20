## 미확인 도착지
##################################
from heapq import heappop, heappush
import sys

INF = sys.maxsize
input = sys.stdin.readline
T = int(input())
graph=None


def dijkstra(start,n):
  result = [INF] * n
  result[start] = 0
  que= list()
  heappush(que,(result[start],start))
  while que:
    result_v,v=heappop(que)
    for fu,fw in graph[v]:
      if result[fu]>result_v+fw:
        result[fu]=result_v+fw
        heappush(que,(result[fu],fu))
  return result



for _ in range(T):

  n,m,t = map(int,input().split())
  s,g,h = map(int,input().split())
  s-=1
  g-=1
  h-=1

  graph=[[] for _ in range(n)]

  for _ in range(m):
    a,b,d = map(int,input().split())
    graph[a-1].append((b-1,d))
    graph[b-1].append((a-1,d))
  d=[]

  for _ in range(t):
    temp = int(input())
    d.append(temp-1)
  d.sort()
  ds,dg,dh=dijkstra(s,n),dijkstra(g,n),dijkstra(h,n)
  for i in range(t):
      if min(ds[g]*2 + (dg[h]*2-1)+dh[d[i]]*2,ds[h]*2+(dh[g]*2-1)+dg[d[i]]*2,ds[d[i]]*2)%2==1:
        print(d[i]+1,end=' ')
  print()



## KCM Travel
##################################

input= sys.stdin.readline
Max = float('INF')

for __ in range(int(input())):
    n,m,k = map(int,input().split())
    D=[[] for _ in range(n+1)]

    for i in range(k):
        u,v,c,d = map(int,input().split())
        D[u].append((v,c,d))

    S=[[Max]*(m+1) for _ in range(n+1)]
    S[1][0]=0

    for e in range(m+1):
        for x in range(1,n+1):
            if S[x][e]==Max:continue
            t=S[x][e]

            for nx,ne,nt in D[x]:
                if ne+e>m:continue
                S[nx][ne+e]=min(S[nx][ne+e],t+nt)

    k = min(S[n])
    print([k,'Poor KCM'][k==Max])