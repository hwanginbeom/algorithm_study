import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    for i in range(t):
        n = int(input())
        table = [list(map(int, input().split())) for _ in range(2)]
        if n > 1:
            table[0][1] += table[1][0]
            table[1][1] += table[0][0]
        for i in range(2, n):
            table[0][i] += max(table[1][i-1], table[1][i-2])
            table[1][i] += max(table[0][i-1], table[0][i-2])

        print(''.join(str(max(table[0][-1], table[1][-1]))))

solution()