import sys
input = sys.stdin.readline

n,m = map(int, input().split())
not_hear = sorted([ input().strip() for i in [n,m] for _ in range(i)])

not_not = []
i = 0
while i<n+m-1:
    if not_hear[i] == not_hear[i+1]:
        not_not.append(not_hear[i])
        i+=2
    else:
        i+=1

print(len(not_not))
print('\n'.join(not_not))