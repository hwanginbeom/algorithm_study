import sys
from collections import deque
input=sys.stdin.readline
inf=sys.maxsize

n=int(input())
arr=[[inf for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1): arr[i][i]=0

while 1:
   a,b=map(int,input().split())
   if a==-1:break
   arr[a][b]=1
   arr[b][a]=1

for k in range(1,n+1):
   for i in range(1,n+1):
      for j in range(1,n+1):
         if arr[i][j]>arr[i][k]+arr[k][j]:
            arr[i][j]=arr[i][k]+arr[k][j]
ans,res=[],[]
for i in range(1,n+1):
   ans.append(max(arr[i][1:n+1]))

MIN=min(ans)
print(MIN, ans.count(MIN))
for i in range(0,n):
   if ans[i]==MIN:res.append(i+1)
print(*res)