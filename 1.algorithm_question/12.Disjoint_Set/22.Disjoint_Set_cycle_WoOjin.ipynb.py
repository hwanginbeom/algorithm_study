import sys

def Find(x):
    if p[x] == x:
        return x
    else:
        y = Find(p[x])
        p[x] = y  # 시간을 줄이는 요소
        return y

def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x != y:
        p[y] = x  # 루트노드 합치기
        cnt[x] = cnt[y] + cnt[x]  # 루트노드 수합치기


T = int(sys.stdin.readline())
for _ in range(T):
    p = {}
    cnt = {}
    F = int(sys.stdin.readline())
    for _ in range(F):
        f1, f2 = sys.stdin.readline().split()
        if f1 not in p:  # f1이 딕셔너리에 없다면
            p[f1] = f1
            cnt[f1] = 1
        if f2 not in p:  # f2이 딕셔너리에 없다면
            p[f2] = f2
            cnt[f2] = 1

        Union(f1, f2)
        print(cnt[Find(f1)])