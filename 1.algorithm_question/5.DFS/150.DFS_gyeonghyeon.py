import sys
input=sys.stdin.readline


computer = {}
n = int(input())
m = int(input())

for i in range(n):
    computer[i+1] = set()

for j in range(m):
    a, b = map(int, input().split())
    computer[a].add(b)
    computer[b].add(a)

def dfs(start, computer):
    for i in computer[start]:
        if i not in infection:
            infection.append(i)
            dfs(i, computer)

infection = []
dfs(1, computer)
print(len(infection) - 1)