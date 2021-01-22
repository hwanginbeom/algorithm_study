# 2021-01-22

# 출처 : https://www.acmicpc.net/problem/4386

# 별자리 만들기
#
# 도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.
#
# 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
# 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
# 별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

import sys
input=sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])

    return parent[x]

# 두 원소가 속한 집합을 합치기

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 노드의 수
n=int(input())
parent=[0]*(n+1) # 부모 테이블 초기화


# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges=[]
result=0

# 부모 테이블상에서, 부모 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i]=i


# 모든 점에 대한 정보를 입력 받기
star=[]
for _ in range(n):
    a,b=map(float,input().split())
    star.append([a,b])


for i in range(n):
    for j in range(i+1,n):
        a=star[i]
        b=star[j]
        dist=round(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5, 2)
        edges.append((dist,i,j))

# 거리순으로 정렬
edges.sort()

# 하나씩 확인
for edge in edges:
    dist,a,b=edge
    # 사이클이 발생하지 않은 경우에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=dist

print(result)











#
