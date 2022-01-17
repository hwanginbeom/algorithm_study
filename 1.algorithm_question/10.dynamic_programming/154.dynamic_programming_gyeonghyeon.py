import sys
input = sys.stdin.readline

def calc(x, cnt):
    cnt = cnt
    if x % 5 == 0:
        return (x // 5) + cnt
    elif x < 0:
        return -1
    elif x == 0:
        return cnt
    else:
        cnt +=1
        return calc(x - 3, cnt)

def solution():
    n = int(input())
    print(calc(n, 0))

solution()