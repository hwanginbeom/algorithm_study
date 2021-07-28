from itertools import combinations


def solution():
    end = -1
    while end < 0:
        ks = input().split()
        if ks[0] != '0':
            per = combinations(ks[1:], 6)
            for i in per:
                print(' '.join(i))
            print()
        else:
            break

solution()