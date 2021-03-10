from collections import deque

n=int(input())
graph={i:[] for i in range(1,n+1)}
parents=[0]*n

for i in range(n-1):
  x,y=map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

queue=deque()
queue.append(1)

while queue:
  temp=queue.popleft()
  for i in graph[temp]:
    if parents[temp-1]!=i:
      parents[i-1]=temp
      queue.append(i)

for i in parents[1:]:
  print(i)