# 집합의 표현
########################
import sys
input = sys.stdin.readline


def find(target):
    if target == parent[target]:
        return target

    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    oper, a, b = map(int, input().split())

    if oper:
        findA = find(a)
        findB = find(b)

        if findA == findB:
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)


# 여행가자 !!
########################

import sys
sys.stdin = open("input.txt","r")
n = int(input()) #도시 수
m = int(input()) #여행계획에 속한 도시 수
board=[list(map(int,input().split())) for _ in range(n)]
plan=list(map(int,input().split())) #여행 계획
parent=[0]*(n+1)

for i in range(1,n+1): #부모 초기화
    parent[i] = i
def find_parent(parent,x):
    if parent[x] != x: #자식인 경우 부모를 찾아라
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            union_parent(parent,i+1,j+1)
for i in range(m-1):
    #부모가 다르면  다른 집합
    if find_parent(parent,plan[i]) != find_parent(parent, plan[i+1]):
        print("NO")
        break
else:
    print("YES")