import sys

input = sys.stdin.readline
flush = sys.stdout.flush

prime = [True] * 1001
for i in range(2, 40):
    if not prime[i]:
        continue
    for j in range(2 * i, 1001, i):
        prime[j] = False

for _ in range(int(input())):
    k = int(input())
    k -= 3
    for i in range(2, 1001):
        if prime[i] and prime[k - i]:
            ans = [3, i, k - i]
            break
    print(*sorted(ans))
