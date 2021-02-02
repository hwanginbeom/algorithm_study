T = int(input())
a = []
b = []
for i in range(0,T):
    c = int(input())
    if c >0:
        a.append(c)
    else:
        b.append(c)

a.sort(reverse=True)
b.sort()

sum = 0

for i in range(0, len(a)-1, 2):
    if a[i+1] == 1:
        sum += a[i] + a[i + 1]
    else:
        sum += a[i]*a[i+1]
else:
    if len(a) % 2 != 0:
        sum += a[-1]
for i in range(0, len(b)-1, 2):
    sum += b[i] * b[i + 1]
else:
    if len(b) % 2 != 0:
        sum += b[-1]
print(sum)