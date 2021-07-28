from itertools import combinations

while 1:
    data = list(map(str, input().split()))

    if data[0] == '0':
        break

    result = list(combinations(data[1:], 6))
    for i in result:
        print(' '.join(i))
    print()