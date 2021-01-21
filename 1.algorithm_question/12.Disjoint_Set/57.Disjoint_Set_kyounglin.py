# 2021-01-21

# 출처 : https://www.acmicpc.net/problem/20040

# 사이클 게임

# 사이클 게임은 두 명의 플레이어가 차례대로 돌아가며 진행하는 게임으로, 선 플레이어가 홀수 번째 차례를, 후 플레이어가 짝수 번째 차례를 진행한다.
# 게임 시작 시 0 부터 n − 1 까지 고유한 번호가 부여된 평면 상의 점 n 개가 주어지며, 이 중 어느 세 점도 일직선 위에 놓이지 않는다.
# 매 차례 마다 플레이어는 두 점을 선택해서 이를 연결하는 선분을 긋는데, 이전에 그린 선분을 다시 그을 수는 없지만 이미 그린 다른 선분과 교차하는 것은 가능하다.
# 게임을 진행하다가 처음으로 사이클을 완성하는 순간 게임이 종료된다.
# 사이클 C는 플레이어가 그린 선분들의 부분집합으로, 다음 조건을 만족한다.

# C에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다.

# 문제는 선분을 여러 개 그리다 보면 사이클이 완성 되었는지의 여부를 판단하기 어려워 이미 사이클이 완성되었음에도 불구하고 게임을 계속 진행하게 될 수 있다는 것이다.
#  이 문제를 해결하기 위해서 게임의 진행 상황이 주어지면 몇 번째 차례에서 사이클이 완성되었는지,
# 혹은 아직 게임이 진행 중인지를 판단하는 프로그램을 작성하려 한다.

# 입력으로 점의 개수 n과 m 번째 차례까지의 게임 진행 상황이 주어지면 사이클이 완성 되었는지를 판단하고,
# 완성되었다면 몇 번째 차례에서 처음으로 사이클이 완성된 것인지를 출력하는 프로그램을 작성하시오.

# 특정 원소가 속한 집합을 찾기 - pypy3 정답 python3 시간 초과
def find_parent(parent,x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] !=x:
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

# 노드의 수와 union 연산의 수 입력 받기
n,m=map(int,input().split())

# 부모 테이블 초기화
parent=[0]*n

# 부모 테이플에서 자기자신 초기화
for i in range(n):
    parent[i]=i

cycle=False # 사이클 발생여부
check=0 # 사이클이 몇번째에 발생 했는지 확인

for i in range(m):
    a,b=map(int,input().split())
    # 사이클이 발생한 경우 cnt추가
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        check=i+1
        break

    else:
        union_parent(parent,a,b)

if cycle:
    print(check)
else:
    print(0)
