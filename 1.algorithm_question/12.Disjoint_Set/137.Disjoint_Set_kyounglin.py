# 2021-08-25

# 출처 : https://www.acmicpc.net/problem/17352

# 특정 원소가 속한 집합을 찾기

def find_parent(parent,x):
    # 루프 노드를 찾을 때까지 재귀 호출
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N=int(input())
parent=[i for i in range(N+1)]
ist=[]
for _ in range(N-2):
    x,y=map(int,input().split())
    union_parent(parent,x,y)

for i in range(1,N+1):
    ist.append(find_parent(parent,i))
answer=list(set(ist))

print(answer[0],answer[1])


