import sys
input = sys.stdin.readline
N, M = map(int, input().split())
true_people = set(map(int, input().split()[1:]))

party = [set(map(int, input().split()[1:])) for _ in range(M)]
check = [1 for _ in range(M)]

for i in range(M):
    for j in range(len(party)):
        if true_people.intersection(party[j]):
            check[j] = 0
            true_people = true_people.union(party[j])


print(sum(check))
