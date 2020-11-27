## 4948번: 베르트랑 공준
import math

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for num in range(n, 2*n+1):
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                break
        else:
            cnt += 1


print(cnt)


## 2581번: 소수

import math

m = int(input())
n = int(input())
only = []

for num in range(m, n+1):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            break
    else:
        if num != 1:
            only.append(num)


if only:
    print(sum(only))
    print(min(only))
else:
    print(-1)

