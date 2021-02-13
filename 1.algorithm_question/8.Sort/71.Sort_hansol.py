# 듣보잡
# https://www.acmicpc.net/problem/1764

n, m = map(int, input().split())

group_A = []
group_B = []

for _ in range(n):
    group_A.append(input())

for _ in range(m):
    group_B.append(input())

# A와 B의 union 을 리스트로 저장
result = list(set(group_A) & set(group_B))

print(len(result))
# 사전순으로 정렬한 result 를 출력
for j in sorted(result):
    print(j)
