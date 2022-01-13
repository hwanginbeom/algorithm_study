import sys
input = sys.stdin.readline

n = int(input()) # n:회원의수
info = []
for _ in range(n):
    a, b = input().split() # a:나이, b:이름
    info.append([a, b])

result = sorted(info, key=lambda x : (int(x[0])))
for i in result:
    print(' '.join(i))