import sys, heapq
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = sorted(a + b)
    test = {'ss':'zz'}
    print(*answer)
    print(**test)


solution()