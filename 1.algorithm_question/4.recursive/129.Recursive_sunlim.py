from itertools import combinations
import sys
input=sys.stdin.readline
while 1:
    arr = input().split()

    if arr.pop(0) == '0':
        break

    for i in combinations(arr, 6):

        print(" ".join(i))

    print()
