n = 10

a1 = 0
a2 = 1

for _ in range(n-1) :
    a3 = a1 + a2
    a1, a2 = a2, a3

print(a3)