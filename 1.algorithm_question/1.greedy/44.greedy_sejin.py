n = int(input())
p = list(map(int, input().split()))

p.sort()

tol = 0
list = []

for i in p :
    tol += i
    list.append(tol)

print(sum(list))