# 2021-07-28

# 출처 : https://www.acmicpc.net/problem/6603

# 로또
from itertools import combinations

while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break
    else:
        numbers = numbers[1:]

    for i in list(combinations(numbers, 6)):
        for j in i:
            print(j, end=' ')
        print()
    print()